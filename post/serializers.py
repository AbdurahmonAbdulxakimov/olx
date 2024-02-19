from rest_framework import serializers

from post import models
from common.serializers import DistrictSerializer, CategorySerializer, SubcategorySerializer
from option.serializers import OptionSerializer
from plan.serializers import PlanSerializer



class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Photo
        fields = ("id", "image")


class PostOptionValueSerializer(serializers.ModelSerializer):
    option = OptionSerializer()
    values = serializers.SlugRelatedField(slug_field='title', many=True, read_only=True)
    
    class Meta:
        model = models.PostOptionValue
        fields = ("id", "option", "value", "values")


class PostSerializer(serializers.ModelSerializer):
    district = DistrictSerializer()
    subcategory = SubcategorySerializer()
    photos = PhotoSerializer(many=True, read_only=True)
    options = PostOptionValueSerializer(source="post_option_values", many=True, read_only=True)
    plan = PlanSerializer()
    
    class Meta:
        model = models.Post
        fields = (
            "id", 
            "title", 
            "description",
            "location",
            "user",
            "district",
            "subcategory",
            "photos",
            "options",
            "plan",
            "is_active",
            "created_at",
            "updated_at"
            )


