from rest_framework import serializers
from students.models import Student
from employee.models import EmployeeModel

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeModel
        fields='__all__'