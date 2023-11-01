from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

router = routers.DefaultRouter()
router.register(r'api/room', views.ApartmentViewSet, basename='room')

urlpatterns = [
    path("", include(router.urls)),
    path('api-auth', include('rest_framework.urls')),
    path('api/register/', views.RegisterView.as_view(), name="sign_up"),
    path('api/user/', views.UserList.as_view()),
    path('api/user/<int:pk>/', views.UserDetail.as_view()),
    path('api/user/update/<int:pk>/', views.UserUpdate.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
]    