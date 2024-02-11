from django.http.response import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from restApi.models import Items
from restApi.serializer import ItemSerializer

# Create your views here.

class ItemsView(APIView):
    permission_classes = [IsAuthenticated]

    # def get(self, request):
    #     items = Items.objects.all()
    #     items_ser = ItemSerializer(items, many=True)
    #     return JsonResponse(items_ser.data, safe=False)
    
    def get(self, request):
        # Get query parameters from request
        query_params = request.query_params
        
        # Exclude 'id' from query parameters
        query_params = {k: v for k, v in query_params.items() if k != 'id'}
        
        # Filter queryset based on query parameters using regex
        queryset = Items.objects.all()
        for param, value in query_params.items():
            queryset = queryset.filter(**{f"{param}__iregex": value})
        
        # Serialize queryset and return response
        items_ser = ItemSerializer(queryset, many=True)
        return JsonResponse(items_ser.data, safe=False)