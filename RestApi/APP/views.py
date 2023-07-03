from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics

# Create your views here.
# @api_view(['GET'])
# def home(request):

#     student_objs = Student.objects.all()
#     serializer = StudentSerializer(student_objs, many=True)



#     return Response({'status':200, 'payload': serializer.data})



# #post student data
# @api_view(['POST'])

# def add_student(request):

#     data = request.data
#     print(data)
#     serializer = StudentSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'status':200, 'payload':serializer.data, 'message':'Student added successfully'})

#     return Response({'status':400, 'payload': serializer.errors, 'message':'Student not added'})


# #PUT to Update data
# @api_view(['PUT'])

# def update_student(request, id):
#     try:
#         student_obj = Student.objects.get(id=id)
#         serializers = StudentSerializer(student_obj, data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response({'status':200, 'payload': serializers.data, 'message':'Student updated successfully'})
#         return Response({'status':400, 'payload': serializers.errors, 'message':'Student not updated'})
#     except Exception as e:
#         return Response({'status':400, 'payload': e, 'message':'Student not updated'})
    

# # #PATCH to partially update data
# @api_view(['PATCH'])
# def patch_student(request, id):
#     try:
#         student_obj = Student.objects.get(id=id)
#         serializers = StudentSerializer(student_obj, data=request.data, partial=True)
#         if serializers.is_valid():
#             serializers.save()
#             return Response({'status':200, 'payload': serializers.data, 'message':'Student updated successfully'})
#         return Response({'status':400, 'payload': serializers.errors, 'message':'Student not updated'})
#     except Exception as e:
#         return Response({'status':400, 'payload': e, 'message':'Student not updated'})
    


#  # DELETE to delete data
# @api_view(['DELETE'])
# def delete_student(request, id):
#     try:
#         student_obj = Student.objects.get(id=id)
#         student_obj.delete()
#         return Response({'status':200, 'message':'Student deleted successfully'})
#     except Exception as e:
#         return Response({'status':400, 'payload': e, 'message':'Student not deleted'})
    



class RegisterUser(APIView):
    def post(self, request):
        serializers = UserSerializer(data=request.data)
        
        if not serializers.is_valid():
            return Response({'status':400, 'payload': serializers.errors, 'message':'User not created'})

        serializers.save()
        user = User.objects.get(username = serializers.data['username'])
        refresh = RefreshToken.for_user(user)

    
        return Response({'status':200, 'payload': serializers.data, 'refresh': str(refresh),
        'access': str(refresh.access_token), 'message':'User created successfully'})
       
    



















@api_view(['GET'])
def get_book(request):
    try:
        books_obj = Book.objects.all()
        serializers = BookSerializer(books_obj, many=True)
        return Response({'status':200, 'payload': serializers.data, 'message':'Books fetched successfully'})
    except Exception as e:
        return Response({'status':400, 'payload': e, 'message':'Books not fetched'})
    


# class StudentAPI(APIView):

#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [IsAuthenticated]
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self,request):
#         student_objs = Student.objects.all()
#         serializer = StudentSerializer(student_objs, many=True)

#         print(request.user)

#         return Response({'status':200, 'payload': serializer.data})


#     def post(self,request):
#         data = request.data
#         print(data)
#         serializer = StudentSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status':200, 'payload':serializer.data, 'message':'Student added successfully'})

#         return Response({'status':400, 'payload': serializer.errors, 'message':'Student not added'})


#     def put(self,request):
#         try:
#             student_obj = Student.objects.get(id= request.data['id'])
#             serializers = StudentSerializer(student_obj, data=request.data)
#             if serializers.is_valid():
#                 serializers.save()
#                 return Response({'status':200, 'payload': serializers.data, 'message':'Student updated successfully'})
#             return Response({'status':400, 'payload': serializers.errors, 'message':'Student not updated'})
#         except Exception as e:
#             return Response({'status':400, 'payload': e, 'message':'Student not updated'})
    


#     def delete(self,request):
#         try:
#             student_obj = Student.objects.get(id=request.data['id'])
#             student_obj.delete()
#             return Response({'status':200, 'message':'Student deleted successfully'})
#         except Exception as e:
#             return Response({'status':400, 'payload': e, 'message':'Student not deleted'})
        




#     def patch(self, request):
#         try:
#             student_obj = Student.objects.get(id=request.data['id'])
#             serializers = StudentSerializer(student_obj, data=request.data, partial=True)
#             if serializers.is_valid():
#                 serializers.save()
#                 return Response({'status':200, 'payload': serializers.data, 'message':'Student updated successfully'})
#             return Response({'status':400, 'payload': serializers.errors, 'message':'Student not updated'})
#         except Exception as e:
#             return Response({'status':400, 'payload': e, 'message':'Student not updated'})
        


class StudentGeneric(generics.ListAPIView, generics.CreateAPIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    

class StudentGeneric1(generics.DestroyAPIView, generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'


    