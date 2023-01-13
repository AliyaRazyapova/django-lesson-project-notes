from rest_framework import serializers

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
    thumbnail_src = serializers.SerializerMethodField()

    def get_thumbnail_src(self, instance):
        return self.context['request'].build_absolute_uri(instance.image.thumbnail.url)

    def validate_title(self, value):
        return value.strip()

    def validate(self, attrs):
        attrs['user_id'] = self.context['request'].user.id
        return attrs

    class Meta:
        model = Note
        fields = ('id', 'title', "text", 'user', 'comments', 'image', 'thumbnail_src', 'created_at')
