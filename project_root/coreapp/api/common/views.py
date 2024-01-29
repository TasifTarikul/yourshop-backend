from django.utils import timezone
from django.contrib.auth import get_user_model, login
from django.contrib.auth.signals import user_logged_in  

from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView
from knox.models import AuthToken

from .serializers import UserSignUpSerializer, UserSigninSerializer

class SignUpView(APIView):
    http_method_names = ['post']

    def post(self, *args, **kwargs):
        serializer = UserSignUpSerializer(data=self.request.data)
        if serializer.is_valid():
            get_user_model().objects.create_user(**serializer.validated_data)
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
   
class SignInView(LoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = UserSigninSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(SignInView, self).post(request, format=None)