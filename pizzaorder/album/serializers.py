from rest_framework import serializers

from album.models import Album,Track

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id','duration','title')

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'tracks')

    def create(self, validated_data):
        track_data=validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)
        for tracks in track_data:
            Track.objects.create(album=album,**tracks)
        return album
