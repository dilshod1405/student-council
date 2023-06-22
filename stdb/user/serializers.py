from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _

from user.models import User, Region


# Viloyatlar
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('region',)


# Foydalanuvchi profilini ko'rish
class UserDetailSerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('username',
                  'profile_photo',
                  'first_name',
                  'last_name',
                  'region',
                  'telegram_username',
                  'instagram_username',
                  'facebook_username', 'university', 'about', 'course')


# Foydalanuvchini card elementlarda ko'rish
class UserCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'profile_photo', 'first_name', 'last_name')


# Yangi foydalanuvchi ro'yhatdan o'tishi
# class UserCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username',
#                   'password',
#                   'profile_photo',
#                   'first_name',
#                   'last_name',
#                   'phone',
#                   'region',
#                   'district',
#                   'telegram_username',
#                   'instagram_username',
#                   'facebook_username', 'university', 'course', 'about',)
#
#     def create(self, validated_data):
#         del validated_data['password']
#         return User.objects.create_user(**validated_data)


# Foydalanuvchi ma'lumotlarini o'zgartirish
class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'phone',
            'region',
            'district',
            'telegram_username',
            'instagram_username',
            'facebook_username', 'university', 'course', 'about'
        )


# Foydalanuvchi parolini o'zgartirish

class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(min_length=6, max_length=64, write_only=True)
    password = serializers.CharField(min_length=6, max_length=64, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=64, write_only=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        old_password = attrs.get('old_password')
        password = attrs.get('password')
        password2 = attrs.get('password2')
        request = self.context.get('request')
        user = request.user
        if not user.check_password(old_password):
            raise serializers.ValidationError(
                {'success': False, 'message': 'Parol avvalgisi bilan bir xil bo`lmasligi lozim'})

        if password != password2:
            raise serializers.ValidationError(
                {'success': False, 'message': 'Yangi parollar bir xil kiritilmadi!'})

        user.set_password(password)
        user.save()
        return attrs

    def create(self, validated_data):
        del validated_data['password']
        return User.objects.create_user(**validated_data)


# Shaxsiy kabinetga kirish
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=100, write_only=True)
    token_class = RefreshToken

    default_error_messages = {
        "no_active_account": _("No active account found with the given credentials")
    }

    def validate(self, attrs):
        authenticate_kwargs = {
            'username': attrs['username'],
            "password": attrs["password"],
        }
        try:
            authenticate_kwargs["request"] = self.context["request"]
        except KeyError:
            pass

        user = authenticate(**authenticate_kwargs)
        print(1111, user)
        if not user:
            raise AuthenticationFailed({
                'message': 'Login yoki parol xato !'
            })
        if not user.is_active:
            raise AuthenticationFailed({
                'message': 'Profil aktiv emas'
            })
        refresh = self.get_token(user)

        attrs["refresh"] = str(refresh)
        attrs["access"] = str(refresh.access_token)
        attrs['user_id'] = user.id

        del attrs['username'], attrs['password']

        return attrs

    @classmethod
    def get_token(cls, user):
        return cls.token_class.for_user(user)


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        token = RefreshToken(attrs['refresh'])
        try:
            token.blacklist()
        except AttributeError:
            pass
        return {}


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'profile_photo',
            'first_name',
            'last_name',
            'phone',
            'region',
            'district',
            'telegram_username',
            'instagram_username',
            'facebook_username', 'university', 'course', 'about',
        )

    def create(self, validated_data):
        del validated_data['password']
        return User.objects.create_user(**validated_data)
