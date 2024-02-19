from rest_framework import serializers

from common.models import Chapter, Category, Subcategory, Region, District


class SubcategorySerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    
    class Meta:
        model = Subcategory
        fields = ("id", "title", "category")


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ("id", "title", "chapter", "subcategories")


class ChapterSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Chapter
        fields = ("id", "title", "categories")


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ("id", "title", "region")


class RegionSerializer(serializers.ModelSerializer):
    districts = DistrictSerializer(many=True, read_only=True)
    
    class Meta:
        model = Region
        fields = ("id", "title", "districts")