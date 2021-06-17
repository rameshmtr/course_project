#---------------------rest frameworks imports----------------------
from rest_framework import  viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.authtoken.serializers import AuthTokenSerializer

#---------------------Models Import--------------------------------
from .models import User
from knox.models import AuthToken

#---------------------Serializers Imports---------------------------
from .serializers import UserSerializer, RegisterSerializer

#---------------------Django Imports---------------------------
from knox.views import LoginView as  KnoxLoginView
from django.core.exceptions import ValidationError
from django.contrib.auth import login


class UserInfoView(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):

        if self.request.query_params.get('id'):
            courses = self.queryset.filter(id = self.request.query_params.get('id'))
            
        else:
            courses = self.queryset.all()

        response = self.serializer_class(courses, many=True)
        return (response.data)

    def create(self, request):
        
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        

        user_obj = User.objects.create_user(username, email, password)
        user_obj.first_name = self.request.data.get('first_name')
        user_obj.last_name = self.request.data.get('last_name')
        user_obj.phone = self.request.data.get('phone')
        user_obj.secret_question = self.request.data.get('secret_question')
        user_obj.secret_answer = self.request.data.get('secret_answer')
        user_obj.save()
                                       
        return Response(self.serializer_class(user_obj).data)

    def update(self, request, *args, **kwargs):
        instance = User.objects.get(id = kwargs.get('pk'))

        if self.request.data.get('email'):
            instance.email = self.request.data.get('email')

        if self.request.data.get('username'):
            instance.username = self.request.data.get('username')

        if self.request.data.get('first_name'):
            instance.first_name = self.request.data.get('first_name')

        if self.request.data.get('last_name'):
            instance.last_name = self.request.data.get('last_name')

        if self.request.data.get('password'):
            instance.set_password(self.request.data.get('password'))

        if self.request.data.get('phone'):
            instance.phone = self.request.data.get('phone')        

        if self.request.data.get('secret_question'):
            instance.secret_question = self.request.data.get('secret_question')

        if self.request.data.get('secret_answer'):
            instance.secret_answer = self.request.data.get('secret_answer')

        instance.save()

        return Response(self.serializer_class(instance).data)

    def destroy(self, request, *args, **kwargs):

        instance = User.objects.get(id = kwargs.get('pk'))
        instance.delete()

        return Response(status=200)

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        user_obj = User.objects.create_user(username, email, password)
        user_obj.save()

        user_queryset = self.serializer_class(user_obj).data

        return Response({
            "user":user_queryset,
            'token':AuthToken.objects.create(user_obj)[1]
        })

class LoginView(KnoxLoginView):

    def post(self, request):

        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)

        return super(LoginView, self).post(request)     

class ForgotEmailView(APIView):

    def get(self, request):

        username = request.data.get('username')
        phone = request.data.get('phone')
        secret_question = request.data.get('secret_question')
        secret_answer = request.data.get('secret_answer')

        user_obj = User.objects.get(username=username, phone=phone, secret_question=secret_question, secret_answer=secret_answer)
    
        return Response(user_obj.email)


   

