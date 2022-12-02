from rest_framework.authtoken.models import Token
from users.models import CustomUser
from djoser.serializers import UserCreateSerializer
from djoser.views import User

User = CustomUser


class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('email','password')

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = User.objects.create_user(email=email)
        user.set_password(password)
        user.save()

        return user
