from rest_framework import serializers

from .models import *
from django.contrib.auth.models import User

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'
        