from django.urls import path, include
from rest_framework import routers

from user.views import UserEditViewSet, UserListViewSet, ChangePasswordView, LoginAPIView, UserDetailView, \
    LogoutAPIView, RegisterView

router = routers.SimpleRouter()

urlpatterns = [
    # URLS for Users
    path('accounts/<int:pk>/', UserDetailView.as_view(), name='account_detail'),
    path('account/<int:pk>/', UserEditViewSet.as_view(), name='account_update'),
    path('accounts/', UserListViewSet.as_view({'get': 'list'}), name='account_list'),
    path('', include(router.urls)),
    path('change-password/<int:pk>/', ChangePasswordView.as_view()),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register')
]
