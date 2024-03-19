from rest_framework import serializers
from .models import Details

class DetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ['id','name','number']