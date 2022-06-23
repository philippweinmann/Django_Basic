from rest_framework import serializers, viewsets

from .models import Sentence


class SentenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sentence
        fields = "__all__"


class SentenceViewSet(viewsets.ModelViewSet):
    serializer_class = SentenceSerializer
    queryset = Sentence.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, pk=None, *args, **kwargs):
        return super().retrieve(request, pk=None, *args, **kwargs)
