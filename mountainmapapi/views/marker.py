from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
import sqlite3
# from ..connection import Connection
from mountainmapapi.models import Marker


class MarkerSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Markers

    Arguments:
        serializers
    """
    class Meta:
        model = Marker
        url = serializers.HyperlinkedIdentityField(
            view_name='marker',
            lookup_field='id'
        )
        fields = ('id', 'created_at', 'lat', 'long', 'is_public', 'description', 'picture_url', 'marker_type_id', 'user_id')
        depth = 2

class Markers(ViewSet):
    """Markers for the API"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized Markers instance
        """
        new_marker = Marker()
        new_marker.lat = request.data["lat"]
        new_marker.long = request.data["long"]
        new_marker.user_id = request.auth.user.id
        new_marker.description = request.data["description"]
        new_marker.is_public = request.data["is_public"]
        new_marker.picture_url = request.data["picture_url"]
        new_marker.marker_type_id = request.data["marker_type_id"]
        new_marker.save()

        serializer = MarkerSerializer(new_marker, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single marker

        Returns:
            Response -- JSON serialized Marker instance
        """
        try:
            marker = Marker.objects.get(pk=pk)
            serializer = MarkerSerializer(marker, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for a product

        Returns:
            Response -- Empty body with 204 status code
        """
        new_marker = Marker()
        new_marker.lat = request.data["lat"]
        new_marker.long = request.data["long"]
        new_marker.customer_id = request.auth.user.customer.id
        new_marker.description = request.data["description"]
        new_marker.is_public = request.data["is_public"]
        new_marker.picture_url = request.data["picture_url"]
        new_marker.marker_type_id = request.data["marker_type_id"]
        new_marker.save()

        serializer = MarkerSerializer(new_marker, context={'request': request})
        return Response(serializer.data)


    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single marker

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            marker = Marker.objects.get(pk=pk)
            marker.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Marker.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to products resource

        Returns:
            Response -- JSON serialized list of products

        """

        # TODO filter so you only see public and your own!
        markers = Marker.objects.all()
            
        serializer = MarkerSerializer(
            markers, many=True, context={'request': request})
        return Response(serializer.data)
