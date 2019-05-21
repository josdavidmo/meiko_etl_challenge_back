from rest_framework import serializers

from movies.models import Movie, MoviesByActor, MoviesByDirector, MoviesByGender


class MovieSerializer(serializers.ModelSerializer):
    """
    Movie serializer.
    """

    class Meta:
        model = Movie
        fields = '__all__'


class MovieByActorSerializer(serializers.Serializer):
    """
    Serializer for MovieByActor.
    """

    actor_1_name = serializers.CharField(max_length=50)
    movie_titles = serializers.ListField()
    total = serializers.IntegerField()

    def create(self, validated_data):
        """
        Creates an instance of MovieByActor
        :param validated_data: data.
        :return: MovieByActor.
        """
        return MoviesByActor(id=None, **validated_data)

    def update(self, instance, validated_data):
        """
        Updates instance MovieByActor.
        :param instance: MovieByActor.
        :param validated_data: data.
        :return: MovieByActor.
        """
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance


class MovieByDirectorSerializer(serializers.Serializer):
    """
    Serializer for MovieByDirector.
    """

    director_name = serializers.CharField(max_length=50)
    movie_titles = serializers.ListField()
    total = serializers.IntegerField()

    def create(self, validated_data):
        """
        Creates an instance of MovieByDirector
        :param validated_data: data.
        :return: MovieByDirector.
        """
        return MoviesByDirector(id=None, **validated_data)

    def update(self, instance, validated_data):
        """
        Updates instance MovieByDirector.
        :param instance: MovieByDirector.
        :param validated_data: data.
        :return: MovieByDirector.
        """
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance


class MovieByGenderSerializer(serializers.Serializer):
    """
    Serializer for MovieByGender.
    """

    genre = serializers.CharField(max_length=50)
    movie_titles = serializers.ListField()
    total = serializers.IntegerField()

    def create(self, validated_data):
        """
        Creates an instance of MovieByGender
        :param validated_data: data.
        :return: MovieByGender.
        """
        return MoviesByGender(id=None, **validated_data)

    def update(self, instance, validated_data):
        """
        Updates instance MovieByGender.
        :param instance: MovieByGender.
        :param validated_data: data.
        :return: MovieByGender.
        """
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance
