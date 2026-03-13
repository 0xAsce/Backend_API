from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Todo

# Serializer for todos
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'isCompleted', 'createdAt')
        read_only_fields = ('id', 'createdAt')
        def validate_title(self, value):
            if len(value) < 3:
                raise serializers.ValidationError("Title must be at least 3 characters long")
            return value
        def validate_description(self, value):
            if value and len(value) > 200:
                raise serializers.ValidationError("Description too long")
            return value

# Serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=6)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already registered")
        return value
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user