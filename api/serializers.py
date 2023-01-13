from rest_framework import serializers

from web.models import Note, User, NoteComment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteComment
        fields = ('id', 'text')


class NoteSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    comments = CommentSerializer(many=True)

    class Meta:
        model = Note
        fields = ('id', 'title', 'user', 'comments', 'created_at')
