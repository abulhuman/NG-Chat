from typing import Any, Type

from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from ..models import Message, Room
from ..serializers.message import MessageReadSerializer, MessageWriteSerializer
from ..serializers.room import RoomReadSerializer, RoomWriteSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomWriteSerializer

    def create(self, request: Request, *args: object, **kwargs: object) -> Response:
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        room = serializer.save()
        read_serializer = RoomReadSerializer(room)

        return Response(read_serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self) -> Any:
        return Room.objects.all()

    def get_serializer_class(self) -> Type[RoomWriteSerializer | RoomReadSerializer]:
        if self.action in ['create', 'update', 'partial_update']:
            return RoomWriteSerializer
        return RoomReadSerializer

    def update(self, request: Request, *args: object, **kwargs: object) -> Response:
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, context={'request': request}, partial=partial)
        serializer.is_valid(raise_exception=True)
        recipe = serializer.save()
        read_serializer = RoomReadSerializer(recipe)

        return Response(read_serializer.data)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageWriteSerializer

    def create(self, request: Request, *args: object, **kwargs: object) -> Response:
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        sender = request.user
        room = Room.objects.get(id=request.data['roomId'])
        message = serializer.save(sender=sender, room=room)
        read_serializer = MessageReadSerializer(message)

        return Response(read_serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self) -> Any:
        return Message.objects.select_related('sender').order_by('-modified_date')

    def get_serializer_class(self) -> Type[MessageWriteSerializer | MessageReadSerializer]:
        if self.action in ['create', 'update', 'partial_update']:
            return MessageWriteSerializer
        return MessageReadSerializer

    def update(self, request: Request, *args: object, **kwargs: object) -> Response:
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, context={'request': request}, partial=partial)
        serializer.is_valid(raise_exception=True)
        message = serializer.save()
        read_serializer = MessageReadSerializer(message)

        return Response(read_serializer.data)
