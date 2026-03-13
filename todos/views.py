from .models import Todo
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import TodoSerializer, RegisterSerializer
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]  # allow anyone to register
    serializer_class = RegisterSerializer

class SecretView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "تمت المصادقة بنجاح!"})

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return todos for the logged-in user
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the current user
        serializer.save(user=self.request.user)