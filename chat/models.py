from django.db import models
from ckeditor.fields import RichTextField

from utils.models import BaseModel
from users.models import User


class Message(BaseModel):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    
    content = RichTextField()

    def __str__(self):
        return self.content


