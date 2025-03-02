from rest_framework import routers


from user.viewsets import UserViewSet


router = routers.DefaultRouter()


router.register("users", UserViewSet, basename="user")
