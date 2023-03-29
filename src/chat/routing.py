from django.urls import path
from . import consumers

websocket_urlpatterns = [
    # re_path(r'ws/room/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer.as_asgi())
    path('ws/room/<str:room_name>/', consumers.ChatRoomConsumer.as_asgi())
]
