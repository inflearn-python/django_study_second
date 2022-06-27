from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from .models import Post

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username']

class PostSerializer(ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model= Post
        fields = '__all__'
