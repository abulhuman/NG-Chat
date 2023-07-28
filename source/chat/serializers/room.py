from typing import Any

from rest_framework import serializers

from source.chat.models import Room


class RoomReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'

    def to_representation(self, instance: Room) -> Any:
        ret = super().to_representation(instance)
        ret['message_count'] = instance.messages.count()
        ret['user_count'] = instance.users.all()
        return ret


class RoomWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'
        read_only_fields = ('id', 'created_date', 'modified_date')

    def create(self, validated_data: Room) -> Any:
        # request = self.context.get('request')
        room = super().create({
            **validated_data,
        })
        return room

    def validate(self, attrs: object) -> object:
        attrs = super().validate(attrs)

        # TODO: call custom validate() function here

        return attrs
