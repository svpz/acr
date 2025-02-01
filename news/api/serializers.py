from rest_framework import serializers

from news.models import ModelNews

class ModelNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelNews
        fields = "__all__"