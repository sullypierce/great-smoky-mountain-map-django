from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
import sqlite3
# from ..connection import Connection
from mountainmapapi.models import MarkerType


class MarkerTypeSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Markers

    Arguments:
        serializers
    """
    class Meta:
        model = MarkerType
        url = serializers.HyperlinkedIdentityField(
            view_name='marker',
            lookup_field='id'
        )
        fields = ('id', 'type_name')

class MarkerTypes(ViewSet):
    """Markers for the API"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized Markers instance
        """
        new_marker_type = MarkerType()
        new_marker_type.type_name = request.data["type_name"]
        new_marker_type.save()

        serializer = MarkerTypeSerializer(new_marker_type, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single marker

        Returns:
            Response -- JSON serialized Marker instance
        """
        try:
            marker_type = MarkerType.objects.get(pk=pk)
            serializer = MarkerTypeSerializer(marker_type, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to products resource

        Returns:
            Response -- JSON serialized list of products

        """

        # TODO filter so you only see public and your own!
        markertypes = MarkerType.objects.all()
            
        serializer = MarkerTypeSerializer(
            markertypes, many=True, context={'request': request})
        return Response(serializer.data)
