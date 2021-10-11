from django.test import TestCase, Client

from myapp.models import Movie, Actor
from myapp.serializers import MovieSerializer, ActorSerializer


class TestMovieSerializer(TestCase):
    def setUp(self) -> None:
        self.movie = Movie.objects.create(name="Example Movie", year='2021-08-18', imdb=2)
        self.movie1 = Movie.objects.create(name="Example Movie1", year='2021-08-18', imdb=1)
        self.actors = self.movie.actors.create(name="actor1", birthdate='1990-01-01')
        self.actors.save()

        self.client = Client()

    def test_data(self):
        data = MovieSerializer(self.movie).data
        assert data['id'] is not None
        assert data['name'] == "Example Movie"
        assert data['year'] == '2021-08-18'
        assert data['imdb'] == 2
        assert data['genre'] == ''
        self.assertEqual(self.movie.actors.all()[0], self.actors)

    def test_movie_search(self):
        response = self.client.get('/movies/?search=Example Movie')
        data = response.data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2)
        self.assertIsNotNone(data[0]['id'])
        self.assertEqual(data[0]['name'], 'Example Movie')


    def test_movie_imdb_order_by(self):
        data = self.client.get('/movies/?ordering=imdb').data
        self.assertEqual(data[0]['name'], "Example Movie1")
        self.assertEqual(data[1]['name'], "Example Movie")

