from django.db import models
from ckeditor.fields import RichTextField

from utils.models import BaseModel
from common.models import District, Subcategory
from option.models import Option, Value
from users.models import User


class Photo(BaseModel):
    image = models.ImageField(upload_to='post/')


class Post(BaseModel):
    title = models.CharField(max_length=256)
    description = RichTextField(null=True, blank=True)
    location = models.CharField(max_length=256)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="posts")
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name="posts")
    photo = models.ManyToManyField(Photo, related_name="posts", null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    
    json = models.JSONField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title


class PostOptionValue(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_option_values")
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="post_option_values")
    values = models.ForeignKey(Value, on_delete=models.CASCADE, related_name="post_option_values", null=True, blank=True)
    
    value = models.CharField(max_length=256, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.post.title +' ' + self.option.title


class UserFavoritePost(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_favorite_posts")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="user_favorite_posts")
    
    def __str__(self) -> str:
        return self.user.username + ' ' + self.post.title