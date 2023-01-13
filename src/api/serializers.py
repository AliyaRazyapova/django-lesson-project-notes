from rest_framework import serializers

from src.api.fields import StdImageField
from src.web.models import Note, User, NoteComment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteComment
        fields = ('id', 'text')


class NoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    text = serializers.CharField(write_only=True)
    image = StdImageField(allow_null=True, required=False)
    text2 = serializers.CharField(source='text', read_only=True)

    def validate_title(self, value):
        return value.strip()

    def validate(self, attrs):
        attrs['user_id'] = self.context['request'].user.id
        return attrs

    class Meta:
        model = Note
        fields = ('id', 'title', "text", "text2", 'user', 'comments', 'image', 'created_at')
        read_only_fields = ('title',)