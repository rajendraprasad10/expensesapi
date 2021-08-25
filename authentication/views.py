from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import RegisterSerializer, EmailVerificationSerializer, LoginSerializer, SetNewPasswordSerializer, LogoutSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import jwt
from django.conf import settings
from .renderers import UserRenderer
from .serializers import ResetPasswordEmailSerializer
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, DjangoUnicodeDecodeError, smart_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util 


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    renderer_classes = [UserRenderer, ]
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        
        current_site = get_current_site(request).domain
        relativeLink = reverse('verify-mail')
        aburl = 'http://'+current_site+relativeLink+"?token="+str(token)
        email_body = "Hi "+user.username+' Use link below to verify your mail \n' + aburl
        data = {"email_body":email_body, "email_to":user.email, "email_subject": "verufy your email"}
        Util.send_mail(data)
        return Response(user_data, status.HTTP_201_CREATED)


class VerifyEmail(APIView):
    token_param_config = openapi.Parameter('token', in_=openapi.IN_QUERY, description='verify the token',
    type=openapi.TYPE_STRING)
    @swagger_auto_schema(manual_parameters=[token_param_config] )
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload =  jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload["user_id"])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email':'Sucessfully activated'}, status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error':'activation link expired'},status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error':'invalid token'}, status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailSerializer
    
    def post(self, request):
        email = request.data['email']
        data = {'request': request, 'data':request.data}
        serializer = self.serializer_class(data=data)

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)     
            current_site = get_current_site(
                request=request).domain
            relativeLink = reverse(
                'password-reset-confirm', kwargs={'uidb64':uidb64, 'token':token})
            absurl = 'http://'+current_site + relativeLink 
            email_body = 'Hello, \n Use link below to reset your password \n' + absurl
            data = {"email_body":email_body, "email_to":user.email, 
                    "email_subject": "reset your password"}
            Util.send_mail(data)

        return Response({"success": "We have sent you a link to reset you password"}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    def get(self, request, uidb64, token):
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': "Token is not valid, please request a new one"}, status=status.HTTP_401_UNAUTHORIZED)

            return Response({"success": True, "message": "Creadentials valid", "uidb64":uidb64, "token":token}, status=status.HTTP_200_OK)
            
        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response({'error': "Token is not valid, please request a new one"}, status=status.HTTP_401_UNAUTHORIZED)


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        return Response({"success": True, "message": "Creadentials valid"}, status=status.HTTP_200_OK)



class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)