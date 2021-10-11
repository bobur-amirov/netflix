from django.http import Http404
from rest_framework import status, permissions, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .models import Movie, Actor, Comment
from .serializers import MovieSerializer, ActorSerializer, CommentSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['imdb']
    search_fields = ['name']
    
    def get_queryset(self):
        queryset = Movie.objects.all()
        genre = self.request.query_params.get('genre')
        if genre is not None:
            queryset = queryset.filter(genre__icontains=genre)
        return queryset

    @action(detail=True, methods=['POST'])
    def add_actor(self, request, pk, *args, **kwargs):
        movies = self.get_object()
        actor_id = request.data["pk"]
        print(request.data["actor_id"])
        actor = Actor.objects.get(pk=actor_id)
        movies.actors.add(actor)
        movies.save()

        return Response({"status": "Add success"})

    @action(detail=True, methods=['DELETE'])
    def remove_actor(self, request, pk, *args, **kwargs):
        movies = self.get_object()
        actor_id = request.data["pk"]
        actor = Actor.objects.get(pk=actor_id)
        movies.actors.remove(actor)
        movies.save()

        return Response({"status": "Delete success"})

    @action(detail=True, methods=['GET'])
    def actors(self, request, *args, **kwargs):
        movie = self.get_object()
        serializer = ActorSerializer(movie.actors.all(), many=True)

        return Response(serializer.data)


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CommentAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        # serializer.validated_data["user"] = self.request.user
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data)

class CommentDeleteAPIView(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()

        return Response({"message": "Delete"})


# class CommentListAPI(ListAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#
#
# class CommentCreateAPI(CreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = (TokenAuthentication)
