from django.shortcuts import redirect
from rest_framework import generics, status, filters
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User
from user.serializers import UserCardSerializer, UserEditSerializer, ChangePasswordSerializer, \
    LoginSerializer, UserDetailSerializer, LogoutSerializer, RegisterSerializer
from .permissions import IsOwnUserOrReadOnly


# Foydalanuvchining ma'lumotlarini o'zgartirish
class UserEditViewSet(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserEditSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnUserOrReadOnly]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]


# Boshqa foydalanuvchining barcha ma'lumotlarini ko'rish
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


# Barcha foydalanuvchilarni ko'rish
class UserListViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserCardSerializer
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['username', 'first_name', 'last_name', 'region__region']


# Foydalanuvchi parolini o'zgartish
class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Successfully set new password'}, status=status.HTTP_200_OK)


# Shaxsiy kabinetga kirish (Login qilish)
class LoginAPIView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return redirect('account_list')


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'message': 'Ro`yhatdan muvaffaqiyatli o`tdingiz'},
                        status=status.HTTP_201_CREATED)
