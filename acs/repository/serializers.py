from rest_framework import serializers

from . import models


class GitRepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GitRepository
        fields = ('id', 'name', 'is_connected')
