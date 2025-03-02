from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets


from user.models import User
from user.serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """

    def list(self, request: Request) -> Response:
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request: Request, pk=None) -> Response:
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
