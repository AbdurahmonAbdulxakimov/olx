from django.db import models

from utils.models import BaseModel
from common.models import Category


class OptionType(BaseModel):
    title = models.CharField(max_length=256)
    
    def __str__(self) -> str:
        return self.title


class Option(BaseModel):
    title = models.CharField(max_length=256)
    field_type = models.ForeignKey(OptionType, on_delete=models.CASCADE, related_name='options')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title


class Value(BaseModel):
    title = models.CharField(max_length=256)
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='values')
    
    def __str__(self) -> str:
        return self.title


