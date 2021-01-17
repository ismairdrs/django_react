from rest_framework.serializers import ModelSerializer
from apps.core.models import Item, List


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'list')


class ListSerializer(ModelSerializer):
    item_set = ItemSerializer(many=True)

    class Meta:
        model = List
        fields = ('id', 'name', 'user', 'item_set')
