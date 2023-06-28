from rest_framework import serializers
from django.contrib.auth import get_user_model
from tag.serializers import TagSerializer
from blog.serializers import PostSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'bio', 'avatar', 'background', 'tag']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        tag_data = validated_data.pop('tag', [])
        user = self.Meta.model(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        user.tag.set(tag_data)
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'avatar', 'background', 'tag', 'is_staff', 'is_admin']