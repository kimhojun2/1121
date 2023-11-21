from rest_framework import serializers
from .models import Article
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'user')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)
