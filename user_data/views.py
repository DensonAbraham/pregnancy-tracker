from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_data.models import User_Data
from user_data.serializer import UserSerializer
from sqlite3 import IntegrityError
from random import randint


# Create your views here.
@api_view(["GET"])
def get_all_user(request):
    query_parameters = request.query_params
    user_data = User_Data.objects.all()

    serialzer = UserSerializer(user_data, many=True)
    print('serialzer', serialzer.data)

    return Response(
        dict(
            results = serialzer.data
        )
    )

# Create your views here.
@api_view(["GET"])
def get_user(request):
    query_parameters = request.query_params
    id = query_parameters.get("id")
    user_data = User_Data.objects.get(id=id)

    serialzer = UserSerializer(user_data)

    return Response(
        dict(
            results = serialzer.data
        )
    )

@api_view(["POST"])
def add_user(request):
    name = request.data.get("name")
    phone_number = request.data.get("phone_number")
    last_menstural_date = request.data.get("last_menstural_date") 

    user_data = User_Data.objects.create(
        name=name, phone_number=phone_number, last_menstural_date=last_menstural_date
    ) 
    user_data.save()

    serialzer = UserSerializer(user_data)

    data = serialzer.data
    return Response(
        {
            "status": 200,
            'user_id': data["id"]
        }
    )
