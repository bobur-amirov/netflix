from datetime import date

from rest_framework import serializers

from .models import Movie, Actor, Comment


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'birthdate', 'gender']

    def validate_birthdate(self, value):
        if value.year < 1950:
            raise serializers.ValidationError("1950-01-01 dan kichik yosh kiritdiz")
        return value


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'movie', 'text', 'created_date']