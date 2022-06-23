from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from rest_framework import serializers, viewsets

from .enums import SentencesContentTypes
from .models import Sentence, Question, Statement
from .question_api import QuestionSerializer
from .statement_api import StatementSerializer


class ContentObjectRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        if isinstance(value, Question):
            serializer = QuestionSerializer(value)
        elif isinstance(value, Statement):
            serializer = StatementSerializer(value)
        else:
            raise Exception('Unexpected type of tagged object')

        return serializer.data


class SentenceSerializerRead(serializers.ModelSerializer):
    content_object = ContentObjectRelatedField(read_only=True)

    class Meta:
        model = Sentence
        fields = "__all__"


class SentenceSerializerWrite(serializers.ModelSerializer):

    def to_internal_value(self, data):
        transformed_data = data
        content_type = transformed_data.pop("content_type", None)

        if content_type not in SentencesContentTypes:
            raise ValidationError(
                f"requestedFor.type needs to be 'user' or 'department', got {content_type}."
            )
        transformed_data["content_type"] = ContentType.objects.get(model=content_type).id
        return super(SentenceSerializerWrite, self).to_internal_value(transformed_data)

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
