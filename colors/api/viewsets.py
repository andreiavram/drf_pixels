from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from colors.api.permissions import IsOwnerOrReadOnly
from colors.api.serializers import ColorBoxSerializer
from colors.models import ColorBox


class ColorBoxViewSet(viewsets.ModelViewSet):
    queryset = ColorBox.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = ColorBoxSerializer

    def get_exception_handler(self):
        pass
