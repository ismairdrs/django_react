from rest_framework import permissions, authentication
from rest_framework.viewsets import ModelViewSet
from apps.core.models import List, Item
from .serializers import ListSerializer, ItemSerializer


class ListViewSet(ModelViewSet):
    #queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    def get_queryset(self):
        user = self.request.user
        return List.objects.filter(user=user)


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
