from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from library.views import AuthorModelViewSet, BookModelSerializer

router = routers.DefaultRouter()
router.register(r'authors', AuthorModelViewSet)

router.register(r'books', BookModelSerializer)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
