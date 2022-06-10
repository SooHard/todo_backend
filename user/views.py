from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from user.models import User
from user.serializers import UserSerializer


class ReadOnlyUserViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

