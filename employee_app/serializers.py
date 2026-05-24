from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Department, Employee


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:

        model = User

        fields = ['username', 'email', 'password']

    def create(self, validated_data):

        user = User.objects.create_user(

            username=validated_data['username'],

            email=validated_data['email'],

            password=validated_data['password']
        )

        return user


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Employee

        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):

    employees = EmployeeSerializer(
        many=True,
        read_only=True
    )

    class Meta:

        model = Department

        fields = [
            'id',
            'name',
            'location',
            'employees'
        ]