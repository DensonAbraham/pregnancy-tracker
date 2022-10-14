from rest_framework import serializers
from user_data.models import User_Data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Data
        fields = '__all__'
        
