from rest_framework import serializers

from . import models


class GitRepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GitRepository
        fields = ('id', 'name', 'is_connected', 'code_style_name')


class GitRepositoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GitRepositoryUpdate
        fields = ('datetime', 'status')


class GitRepositoryConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GitRepositoryConnection
        fields = ('code_style', 'repository')
