from rest_framework import serializers
from .models import Ad, Comment


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(source='author.id', read_only=True)
    ad_id = serializers.IntegerField(source='ad.id', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_image = serializers.ImageField(source='author.image', read_only=True)

    # TODO сериалайзер для модели
    class Meta:
        model = Comment
        fields = (
            'pk',
            'text',
            'author_id',
            'ad_id',
            'author_first_name',
            'author_last_name',
            'author_image',
        )


class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    class Meta:
        model = Ad
        fields = ('pk', 'title', 'price', 'author')


class AdDetailSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)

    class Meta:
        model = Ad
        fields = ('pk', 'title', 'price', 'author', 'author_first_name')
