import json

from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import FoodTruck
from math import radians, sin, cos, sqrt, atan2
from .serializers import FoodTruckSerializer
import pandas as pd
import numpy as np
from django.http import HttpResponse
import requests

class FoodTruckListAPIView(APIView):
    serializer_class = FoodTruckSerializer

    def get(self, request):
        # Get latitude and longitude from request parameters
        startlat = float(request.query_params.get('latitude'))
        startlng = float(request.query_params.get('longitude'))

        all_foodtrucks = FoodTruck.objects.all()

        # Calculate distance for each food truck
        foodtrucks_with_distances = []
        for foodtruck in all_foodtrucks:
            distance = haversine(startlat, startlng, foodtruck.latitude, foodtruck.longitude)
            foodtruck.distance = distance
            foodtrucks_with_distances.append(foodtruck)

        # Sort food trucks by nearest
        sorted_foodtrucks = sorted(foodtrucks_with_distances, key=lambda x: x.distance)

        # Extract 10 nearest food trucks
        nearest_foodtrucks = sorted_foodtrucks[:10]
        # Return the queryset of FoodTruck objects
        serializer = FoodTruckSerializer(nearest_foodtrucks, many=True)
        return Response({'foodtrucks': serializer.data})

def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = 6371 * c  # Radius of Earth in kilometers
    return distance


def insertData(request):
    df = pd.read_csv('foodtrucks/food-truck-data.csv')
    df.replace({np.nan: None}, inplace=True)
    #Clear the table First
    FoodTruck.objects.all().delete()
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Create a new FoodTruck object with data from the row
        food_truck = FoodTruck(
            locationid=row['locationid'],
            Applicant=row['Applicant'],
            FacilityType=row['FacilityType'],
            cnn=row['cnn'],
            LocationDescription=row['LocationDescription'],
            Address=row['Address'],
            blocklot=row['blocklot'],
            block=row['block'],
            lot=row['lot'],
            permit=row['permit'],
            Status=row['Status'],
            FoodItems=row['FoodItems'],
            X=row['X'],
            Y=row['Y'],
            Latitude=row['Latitude'],
            Longitude=row['Longitude'],
            Schedule=row['Schedule'],
            dayshours=row['dayshours'],
            NOISent=row['NOISent'],
            Approved=row['Approved'],
            Received=row['Received'],
            PriorPermit=row['PriorPermit'],
            ExpirationDate=row['ExpirationDate'],
            Location=row['Location'],
            FirePreventionDistricts=row['Fire Prevention Districts'],
            PoliceDistricts=row['Police Districts'],
            SupervisorDistricts=row['Supervisor Districts'],
            ZipCodes=row['Zip Codes'],
            Neighborhoods_old=row['Neighborhoods (old)'],
        )
        # Save the FoodTruck object to the database
        food_truck.save()

    return HttpResponse("Data inserted successfully!")

def displaylist(request):
    if request.method == 'GET':
        return render(request, 'foodtrucks.html')

    elif request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        current_host = request.get_host()
        url = f"http://{current_host}/api/foodtrucks/?latitude={latitude}&longitude={longitude}"
        response = requests.get(url)
        data = json.loads(response.text)
        return render(request, 'foodtrucks.html', {'food_trucks': data['foodtrucks']})

