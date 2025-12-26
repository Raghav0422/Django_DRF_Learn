from django.shortcuts import render
from django.http import Http404
# from django.http import JsonResponse

from students.models import Student
from employee.models import EmployeeModel

from .serializers import StudentSerializer
from .serializers import EmployeeSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics



# Create your views here.
# def studentView(request):
#     student=Student.objects.all()
#     student_list=list(student.values())
#     return JsonResponse(student_list,safe=False)

@api_view(['GET','POST'])
def studentView(request):
    if request.method=='GET':
        student=Student.objects.all()
        serializer=StudentSerializer(student,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def studentDetailsView(request,pk):
    try:
        student=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method=='PUT':
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#BELOW CLASS IS CBV WITH MIXINS TO VIEW ALL EMPLOYEE DATA
class EmployeeView(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=EmployeeModel.objects.all()
    serializer_class=EmployeeSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)



#BELOW CLASS IS DONE TO VIEW ALL DATA ON THE BASISC OF CBV
# class EmployeeView(APIView):
#     def get(self,reqyest):
#         employee=EmployeeModel.objects.all()
#         serializer=EmployeeSerializer(employee,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     def post(self,request):
#         serializer=EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

#BELOW CLASS IS CBV WITH MIXINS TO VIEW SINGLE EMPLOYEE DATA
class EmployeeDetailsView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=EmployeeModel.objects.all()
    serializer_class=EmployeeSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)

#BELOW CLASS IS DONE TO Get UPDATE DELETE SINGLE EMPLOYEE DATA ON THE BASISC OF CBV
# class EmployeeDetailsView(APIView):
#     def get_object(self,pk):
#         try:
#             return EmployeeModel.objects.get(pk=pk)
#         except EmployeeModel.DoesNotExist:
#             raise Http404

#     def get(self,request,pk):
#         employee=self.get_object(pk)
#         serializer=EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self,request,pk):
#         employee=self.get_object(pk)
#         serializer=EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,pk):
#         employee=self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

