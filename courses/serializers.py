#---------------django imports----------------
from django.db.models import fields
from django.http.response import FileResponse

#---------------restframeworks imports----------------
from  rest_framework import serializers

#---------------models imports----------------
from .models import CourseDetails, CourseWishlist

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseDetails
        fields = ['id', 'name', 'author','price', 'date']

class CourseWishlistSerializer(serializers.ModelSerializer):

    course_name = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()

    def get_course_name(self, instance):
        return instance.course.name

    def get_username(self, instance):
        return instance.user.username


    class Meta:
        model = CourseWishlist
        fields = ['id', 'course_name' ,'username']