from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer


class RegisterUserView(CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()
