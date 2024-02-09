from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.contrib.auth.hashers import make_password
import json
from .serializers import UserSerializer, BuyerSerializer, UserDetailSerializer,SellerSerializer,CourseBuyingHistorySerializer, CreateUserSerializer
from ..models import CustomUser,CourseHistory ,Wallet


class AllUsers(APIView):
    def get(self, request):
        try:
            users = CustomUser.objects.filter(is_superuser=False)
            serializer = UserSerializer(users, many=True)
            context={
                'success':True,
                "status" : status.HTTP_200_OK,
                "data":serializer.data
            }
            return Response(context)
        except Exception as error:
            context={
                'success':False,
                "status" : status.HTTP_400_BAD_REQUEST,
                "data":str(error)
            }
            return Response(context)


class AllBuyers(APIView):   
    def get(self, request):
        try:
            buyers = CustomUser.objects.filter(is_superuser=False,is_buyer=True)
            print (buyers)
            serializer = BuyerSerializer(buyers, many=True,context={'request': request})
            context = {
             "success" : True,
             "status" : status.HTTP_200_OK,
             "data" : serializer.data
            }
            # print(serializer.errors)
            return Response(context)
        except Exception as e:
            context = {
             "success" : False,
             "status" : status.HTTP_400_BAD_REQUEST,
             "data" : str(e)
            }
            print(e)
            return Response(context)


class AllSellers(APIView):   
    def get(self, request):
        try:
            sellers = CustomUser.objects.filter(is_seller =  True, is_superuser=False)
            serializer = SellerSerializer(sellers, many=True,context={'request': request})
            context = {
             "success" : True,
             "status" : status.HTTP_200_OK,
             "data" : serializer.data
            }
            # print(serializer.errors)
            return Response(context)
        except Exception as e:
            context = {
             "success" : False,
             "status" : status.HTTP_400_BAD_REQUEST,
             "data" : str(e)
            }
            print(e)
            return Response(context)


class UserDetail(APIView):
    def get(self, request, id):
        try:
            user = CustomUser.objects.get(id=id)
            serializer = UserDetailSerializer(user,context={'request': request})
            context = {
             "success" : True,
             "status" : status.HTTP_200_OK,
             "data" : serializer.data
            }
            # print(serializer.errors)
            return Response(context)
        except Exception as e:
            context = {
             "success" : False,
             "status" : status.HTTP_400_BAD_REQUEST,
             "data" : str(e)
            }
            print(e)
            return Response(context)


class CreateUser(APIView):
    # def post(self, request):
    #     try:
    #         data = request.body
    #         print('+++++++++++++++++++++++++++++++++++++++++++++++')
    #         print(data.get('email'))
    #         serializer = CreateUserSerializer(data = data)
    #         print(serializer)
    #         if serializer.is_valid():
    #             serializer.save()
    #             context = {
    #             'success' : True,
    #             'status':status.HTTP_201_CREATED,
    #             'data' : serializer.data
    #             }
    #             return Response(context)
    #     except Exception as e:
    #         context = {
    #             'success' : False,
    #             'status':status.HTTP_400_BAD_REQUEST,
    #             "data" : str(e)
    #             }
    #         print(e)
    #         return Response(context)


   def post(self, request):
        try:
            print("===============================")
            data = request.data
            data['username'] = data.get("email")
            serializer = CreateUserSerializer(data = data)
            if serializer.is_valid():
                serializer.save(password=make_password(data.get("password")))
                context={
                    "success":True,
                    "status": status.HTTP_201_CREATED,
                    "data":serializer.data
                }
                return Response(context)
            else:
                context={
                    "success":True,
                    "status": status.HTTP_201_CREATED,
                    "data":serializer.errors
                }
                return Response(context)

        except Exception as error:
            context={
                    "success":False,
                    "status": status.HTTP_404_NOT_FOUND,
                    "data":str(error)
                }
            return Response(context)