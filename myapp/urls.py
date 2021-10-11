from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import MovieViewSet, ActorViewSet, CommentAPIView,CommentDeleteAPIView

router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('comment/', CommentAPIView.as_view(), name='comment'),
    path('comment/<int:pk>/', CommentDeleteAPIView.as_view(), name='comment-delete'),
    path('auth/', obtain_auth_token),
    # path('comment/list', CommentListAPI.as_view(), name='comment'),
    # path('comment/create', CommentCreateAPI.as_view(), name='comment-create'),
]
