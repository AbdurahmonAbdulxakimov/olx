from rest_framework.generics import ListAPIView

from common import models
from common import serializers


class ChapterAPIView(ListAPIView):
    queryset = models.Chapter.objects.all()
    serializer_class = serializers.ChapterSerializer

