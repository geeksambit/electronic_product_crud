from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from users.serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.



class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing product instances.
    """
    # permission_classes = [IsAuthenticated|ReadOnly]
    # serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT']:
            return UserUpdateSerializer
        return UserRegistrationSerializer
    
    def get_object(self):
        return self.request.user
    
    def create(self, request):
        print(request.data)
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            data =  serializer.data
            data.update({
                "status" : "Active",
            })
            return Response(
                {
                        "data": { "user" : data },
                        "status" : "ok",
                        "code" : 200,
                        "message" : "Thank you for creating your account with us.",
                        "errors" : []
                },
                status.HTTP_200_OK
            )
            # return Response(serializer.validated_data, status=status.HTTP_200_OK)
        res = {
            # 'message' : str(serializer.errors['non_field_errors'][0]),
            "message": serializer.errors,
            'status' : "Bad Request",
            'code' : status.HTTP_400_BAD_REQUEST,
            'errors' : []
        }
        return Response(res, status=status.HTTP_400_BAD_REQUEST)




class MyTokenObtainPairView(TokenObtainPairView):     
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(email=request.data['email'])
            
            refresh = RefreshToken.for_user(user)                    
            data = UserRegistrationSerializer(instance=user).data
            data['access_token'] = str(refresh.access_token)
            data['status'] = "VERIFIED"
            data['gender'] = "UNKNOWN"
            data['expires_at'] = refresh['exp']

            return Response(
                {
                        "data": { "user" : data },
                        "status" : "ok",
                        "code" : 200,
                        "message" : "Login successfull",
                        "errors" : []
                },
                status.HTTP_200_OK
            )
        # return Response(serializer.validated_data, status=status.HTTP_200_OK)
        res = {
            'message' : serializer.errors,
            'status' : "Bad Request",
            'code' : status.HTTP_400_BAD_REQUEST,
            'errors' : serializer.errors
        }
        return Response(res, status=status.HTTP_400_BAD_REQUEST)


