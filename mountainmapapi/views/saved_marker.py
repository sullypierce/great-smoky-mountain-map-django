from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from ..models import Marker, SavedMarker
from django.contrib.auth.models import User

# for custom sql method
import sqlite3
from django.shortcuts import render
# from .connection import Connection


class SavedMarkerSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for SavedMarker

    Arguments:
        serializers
    """
    class Meta:
        model = SavedMarker
        url = serializers.HyperlinkedIdentityField(
            view_name='saved_marker',
            lookup_field='id'
        )
        fields = ('id', 'user', 'marker')
        depth = 2


class SavedMarkers(ViewSet):

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized Orders instance
        """
        new_saved_marker = SavedMarker()
        new_saved_marker.user_id = request.auth.user.id
        new_saved_marker.marker_id = request.data['marker_id']
        

        new_saved_marker.save()

        serializer = SavedMarkerSerializer(new_saved_marker, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single order_product

        Returns:
            Response -- JSON serialized order_product instance
        """
        try:
            saved_marker = SavedMarker.objects.get(pk=pk)
            serializer = SavedMarkerSerializer(
                saved_marker, context={'request': request})
            return Response(serializer.data)    
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single Order

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            saved_marker_to_delete = SavedMarker.objects.get(pk=pk)
            saved_marker_to_delete.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except SavedMarker.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to saved_markers resource

        Returns:
            Response -- JSON serialized list of a users saved_markers
        """

        try:
            saved_markers = SavedMarker.objects.filter(user_id=request.auth.user.id)
            serializer = SavedMarkerSerializer(
                saved_markers, many=True, context={'request': request})
            return Response(serializer.data)
        except SavedMarker.DoesNotExist as ex:
            return Response([])
