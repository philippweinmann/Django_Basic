from rest_framework import serializers, viewsets
from .models import Statement


class StatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statement
        fields = "__all__"


class StatementViewSet(viewsets.ModelViewSet):
    serializer_class = StatementSerializer
    queryset = Statement.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, pk=None, *args, **kwargs):
        return super().retrieve(request, pk=None, *args, **kwargs)