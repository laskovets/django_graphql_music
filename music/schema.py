from graphene_django import DjangoObjectType
import graphene
from music.models import Artist, Track, Album


class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist


class AlbumType(DjangoObjectType):
    class Meta:
        model = Album


class TrackType(DjangoObjectType):
    class Meta:
        model = Track


class Query(graphene.ObjectType):
    get_tracks_by_artist_name_and_track = graphene.List(
        TrackType,
        artist=graphene.String(required=True),
        track=graphene.String(required=True)
    )
    get_tracks_by_album_name = graphene.List(
        TrackType,
        album=graphene.String(required=True)
    )
    get_tracks_by_genre = graphene.List(
        TrackType,
        genre=graphene.String(required=True)
    )
    get_tracks_by_artist = graphene.List(
        TrackType,
        artist=graphene.String(required=True)
    )

    def resolve_get_tracks_by_artist_name(self, info, artist, track):
        return Track.objects.filter(artist__name=artist, name=track).select_related()

    def resolve_get_tracks_by_album_name(self, info, album):
        return Track.objects.filter(album__name=album).select_related()

    def resolve_get_tracks_by_genre(self, info, genre):
        return Track.objects.filter(genre__contains=[genre]).select_related()

    def resolve_get_tracks_by_artist(self, info, artist):
        return Track.objects.filter(artist__name=artist).select_related()


schema = graphene.Schema(query=Query)
