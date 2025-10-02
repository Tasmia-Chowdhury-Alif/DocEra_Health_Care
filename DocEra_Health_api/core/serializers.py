"""Serializers for user creation and details (extends Djoser)."""
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample

@extend_schema_serializer(
    examples=[OpenApiExample('User Create', value={'username': 'user1', 'email': 'user@example.com', 'password': 'securepass', 'first_name': 'John', 'last_name': 'Doe'})]
)
class UserCreateSerializer(BaseUserCreateSerializer):
    """
    Serializer for user registration(Djoser); triggers email activation.
    """
    class Meta(BaseUserCreateSerializer.Meta):
        model = get_user_model()  # Uses the default User model
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class UserSerializer(BaseUserSerializer):
    """
    Serializer for user profile (Djoser).
    """
    class Meta(BaseUserSerializer.Meta):
        model = get_user_model()
        fields = ('id', 'username', 'email', 'first_name', 'last_name')