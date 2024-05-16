from django.urls import path
from .views import FoodTruckListAPIView, insertData, displaylist

urlpatterns = [
    path('foodtrucks/', FoodTruckListAPIView.as_view(), name='foodtrucks-list'),
    path('insert_from_csv_to_sql/', insertData, name='csvtosql'),
    path('', displaylist, name='display-list')
]