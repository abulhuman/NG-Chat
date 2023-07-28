from django.db import models

from source.general.models import created_modified as general_models


# TODO(Adem): move to somewhere sensible in time
class User(general_models.CreatedModified):
    name = models.CharField(max_length=20)
    icon = models.CharField(max_length=15)

    def __str__(self) -> str:
        return str(self.name)


class Room(general_models.CreatedModified):
    name = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=50)
    icon = models.CharField(max_length=15)
    color = models.CharField(max_length=10)

    def __str__(self) -> str:
        return str(self.name)

    # TODO(Adem): implement when you find out about "how to do aggregates in Django"
    # user_count aggregate


class Message(general_models.CreatedModified):
    content = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    roomId = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages', default=None, null=True)
    senderId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages', default=None, null=True)

    def __str__(self) -> str:
        if len(str(self.content)) > 10:
            return f'{str(self.content[:10])}...'
        else:
            return str(self.content)
