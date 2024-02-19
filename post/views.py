from rest_framework.generics import ListAPIView, RetrieveAPIView 

from post import models
from post import serializers


class VipPostsAPIView(ListAPIView):
    queryset = models.Post.objects.all().filter(plan__detail__code="VIP")
    serializer_class = serializers.PostSerializer


class PostAPIView(ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    filterset_fields = ("subcategory__category", "subcategory", 'district', "subcategory__category__options__values")


class PostRetrieveAPIView(RetrieveAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer