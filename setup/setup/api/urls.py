from rest_framework.routers import DefaultRouter
from myApp.api.urls import router as myApp_router
from django.urls import path, include

router = DefaultRouter()

# Posts
router.registry.extend(myApp_router.registry)

# Url patterns
urlpatterns = [
    path('', include(router.urls)),
]
