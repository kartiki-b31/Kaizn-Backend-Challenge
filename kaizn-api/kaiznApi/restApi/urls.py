from django.urls import path
from restApi.views import ItemsView

urlpatterns = [
    path('items/', ItemsView.as_view(), name='items-api'),
]
