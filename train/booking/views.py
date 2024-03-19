from django.shortcuts import render
from .serializers import DetailSerializers
from .models import Details
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
@api_view(["GET","POST"])
def TrainDetail(request):
    if(request.method=="GET"):
        detail = Details.objects.all()
        serializer = DetailSerializers(detail,many=True)
        return Response(serializer.data)
 
    elif(request.method=="POST"):
        serializer = DetailSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_201_CREATED)

@api_view(["GET","PUT"])
def OneTrainDetail(request,id):
    try:
        detail = Details.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if(request.method=="GET"):
        serializer = DetailSerializers(detail,many=False)
        return Response(serializer.data)

    if(request.method=="PUT"):
        serializer = DetailSerializers(detail,data=request.data)
        if(serializer.is_valid()):
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_304_NOT_MODIFIED)