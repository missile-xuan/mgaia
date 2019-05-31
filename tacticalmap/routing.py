from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/tacticalmap/<room_name>/', consumers.TacticalMapConsumer),
]