from rest_framework import serializers
from posttag.models import Tag,Post,PostsTags


class TagSerializer(serializers.ModelSerializer):

    class Meta():
        model = Tag
        fields = ('id', 'name')

# class PostTagSerializer(serializers.ModelSerializer):
#     id = serializers.ReadOnlyField(source='tag.id')
#     name = serializers.ReadOnlyField(source='tag.name')
#
#     class Meta():
#         model = PostTag
#         fields = ('id', 'title')


class PostSerilaizer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = PostsTags
        fields = (
            'id', 'title', 'tags',
        )

    def create(self, validated_data):
        tags = self.validated_data.pop('tags')
        post = Post.objects.create(**validated_data)
        post.set_tags(*tags)
        return post

    def _get_or_create_tags(self, tag_names):
        if tag_names:
            result = []
            for name in tag_names:
                tag, _ = Tag.objects.get_or_create(name=name)
                result.append(tag)
            return result
        return []

    def to_internal_value(self, data):
        tags = data.pop('tags', None)
        tags = self._get_or_create_tags(tags)
        data = super().to_internal_value(data)
        data.update({
            'tags': tags,
        })
        return data