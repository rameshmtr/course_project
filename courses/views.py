from django.shortcuts import render

# Create your views here.
#--------------------rest framework imports-----------------------
from rest_framework import  viewsets
from rest_framework.response import Response

#--------------------Django Model imports-----------------------
from .models import CourseDetails, CourseWishlist
from authorization.models import User

#--------------------Django Serializers imports-----------------------
from .serializers import CourseSerializer, CourseWishlistSerializer

# Create your views here.

class CourseDetailsViews(viewsets.ModelViewSet):

    '''
    CRUD requests for the courses
    '''

    queryset = CourseDetails.objects.all()
    serializer_class = CourseSerializer
    
    def get_queryset(self):
        
        if self.request.query_params.get('id'):
            courses = self.queryset.filter(id = self.request.query_params.get('id'))
            
        else:
            courses = self.queryset.all()

        response = self.serializer_class(courses, many=True)
        return (response.data)

    def create(self, request):
        instance = self.queryset.create(name = request.data.get('name'),
                                        author = request.data.get('author'),
                                        date = request.data.get('date'),
                                        price = request.data.get('price'))
        instance.save()

        response = self.serializer_class(instance).data
        return Response(response)
        
    def update(self, request, *args, **kwargs):

        instance = self.queryset.get(id = kwargs.get('pk'))

        if request.data.get('name'):
            instance.name = request.data.get('name')

        if request.data.get('author'):
            instance.author = request.data.get('author')

        if request.data.get('price'):
            instance.price = request.data.get('price')

        if request.data.get('date'):
            instance.date = request.data.get('date')

        instance.save()

        response = self.serializer_class(instance).data

        return Response(response)

    def destroy(self, request, *args, **kwargs):

        instance = self.queryset.get(id = kwargs.get('pk'))
        instance.delete()

        return Response(status=200)

class CourseWishlistView(viewsets.ModelViewSet):

    '''
    CRUD requests for the wishlists
    '''

    queryset = CourseWishlist.objects.all()
    serializer_class = CourseWishlistSerializer

    def get_queryset(self):

        if self.request.query_params.get('user_id'):
            return self.queryset.filter(user=self.request.query_params.get('user_id'))

        if self.request.query_params.get('course_id'):
            return self.queryset.filter(course=self.request.query_params.get('course_id'))
        
        if self.request.query_params.get('id'):
            return self.queryset.filter(id = self.request.query_params.get('id'))

        else:
            return self.queryset.all()

    def create(self, request):

        instance = self.queryset.create(user = User.objects.get(id=request.data.get('user_id')),
                                        course = CourseDetails.objects.get(id = request.data.get('course_id')))

        instance.save()
        response = self.serializer_class(instance).data
        return Response(response)

    def update(self , request, *args, **kwargs):
        
        instance = self.queryset.get(id = kwargs.get('pk'))

        if request.data.get('course_id'):
            instance.course = CourseDetails.objects.get(id = request.data.get('course_id'))

        if request.data.get('user_id'):
            instance.user = User.objects.get(id=request.data.get('user_id'))

        instance.save()
        response = self.serializer_class(instance).data
        return Response(response)

    def destroy(self , request, *args, **kwargs):
        
        instance = self.queryset.get(id = kwargs.get('pk'))
        instance.delete()

        return Response(status=200)



