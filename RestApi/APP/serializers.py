
from rest_framework import serializers

from .models import *

from django.contrib.auth.models import User





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

    def  create(self, validate_data):
        user = User.objects.create(username = validate_data['username'])
        user.set_password(validate_data['password'])
        user.save()

        return user 






















class StudentSerializer(serializers.ModelSerializer):
    """Serializer for student object"""
    class Meta:
        model = Student
        fields = '__all__'
#adding coustum validation rules
    def validate(self, data):
        
        if data['age'] <18:
            raise serializers.ValidationError({'Error': "Age should be greater then 18"})
        
        for n in data['name']:
            if n.isdigit():
                raise serializers.ValidationError({'Error': "Name Cannot contain Numbers"})
        
        return data 
    




class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category object"""
    class Meta:
        model = Category
        fields = ['category_name']



class BookSerializer(serializers.ModelSerializer):
    """Serializer for book object"""
    category = CategorySerializer(read_only=True) #can use any costume field while using this
    class Meta:
        model = Book
        fields = '__all__'
        # depth = 1 can't use costume field on category model

