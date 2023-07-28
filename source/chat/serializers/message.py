from typing import Any

from rest_framework import serializers

from source.chat.models import Message


class MessageReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'


class MessageWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('id', 'created_date', 'modified_date', 'sender', 'room')

    def create(self, validated_data: Message) -> Any:
        request = self.context.get('request')
        message = super().create({**validated_data, 'sender': request.user})
        return message

    def validate(self, attrs: object) -> object:
        attrs = super().validate(attrs)

        # TODO: call custom validate() function here

        return attrs
