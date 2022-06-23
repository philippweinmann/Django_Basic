from rest_framework import serializers, viewsets

from .models import Sentence


class SentenceSerializerRead(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = "__all__"


class SentenceSerializerWrite(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = "__all__"


class SentenceViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return SentenceSerializerRead
        else:
            return SentenceSerializerWrite

    queryset = Sentence.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, pk=None, *args, **kwargs):
        return super().retrieve(request, pk=None, *args, **kwargs)
