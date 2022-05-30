from rest_framework import serializers
from watchlist.models import Watchlist, StreamPlatform


def is_active(value):
    if value == False:
        raise serializers.ValidationError("Movies must be active")


class WatchlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Watchlist
        fields = "__all__"

    def create(self, validated_data):
        return Watchlist.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchlistSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"