from rest_framework import serializers
from restApi.models import Items


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('id', 'SKU', 'name', 'category', 'tags', 'stock_status', 'available_stock')