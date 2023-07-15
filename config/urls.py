from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from testApp.views import CPUViewSet, SoundCardViewSet, MonitorViewSet, RAMViewSet, CategoriesViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoriesViewSet)
router.register(r'cpu', CPUViewSet)
router.register(r'ram', RAMViewSet)
router.register(r'monitor', MonitorViewSet)
router.register(r'soundcard', SoundCardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
