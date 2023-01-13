from rest_framework import serializers


class NoteSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
