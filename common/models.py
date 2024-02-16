from django.db import models

from utils.models import BaseModel


class Region(BaseModel):
    title = models.CharField(max_length=256)
    
    def __str__(self) -> str:
        return self.title


class District(BaseModel):
    title = models.CharField(max_length=256)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='districts')

    def __str__(self) -> str:
        return self.title


class Chapter(BaseModel):
    title = models.CharField(max_length=256)
    
    def __str__(self) -> str:
        return self.title


class Category(BaseModel):
    title = models.CharField(max_length=256)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='categories')
    
    def __str__(self) -> str:
        return self.title


class Subcategory(BaseModel):
    title = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    
    def __str__(self) -> str:
        return self.title
