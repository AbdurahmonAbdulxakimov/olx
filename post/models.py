from django.db import models
from ckeditor.fields import RichTextField

from utils.models import BaseModel
from common.models import District, Subcategory, Chapter, Category
from option.models import Option, Value
from users.models import User
from plan.models import Plan


class Photo(BaseModel):
    image = models.ImageField(upload_to='post/')
    
    def __str__(self) -> str:
        return self.image.path


class Post(BaseModel):
    title = models.CharField(max_length=256)
    description = RichTextField(null=True, blank=True)
    location = models.CharField(max_length=256)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="posts")
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name="posts")
    photos = models.ManyToManyField(Photo, related_name="posts")
    
    is_active = models.BooleanField(default=True)
    
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True, blank=True)
    
    json = models.JSONField(null=True, blank=True)
    # options = models.JSONField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title


class PostOptionValue(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_option_values")
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="post_option_values")
    values = models.ManyToManyField(Value, related_name="post_option_values", null=True, blank=True)
    
    value = models.CharField(max_length=256, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.post.title +' ' + self.option.title


class UserFavoritePost(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_favorite_posts")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="user_favorite_posts")
    
    def __str__(self) -> str:
        return self.user.username + ' ' + self.post.title


