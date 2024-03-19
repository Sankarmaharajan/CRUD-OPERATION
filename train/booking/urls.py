from django.urls import path
from .views import *
urlpatterns = [
    path('detail/',TrainDetail),
    path('detail/<int:id>',OneTrainDetail),
]