from rest_framework.views import APIView
from rest_framework import generics, mixins, permissions
from accounts.api.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from status.models import Status
from .serializers import StatusSerializer
from django.shortcuts import get_object_or_404
import json


def is_json(json_data):
    try:
        real_json = json.loads(json_data)
    except ValueError:
        is_valid = False
    return is_valid


class StatusAPIView(mixins.CreateModelMixin,
                    generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = StatusSerializer
    passed_id = None
    search_fields = ('user__username', 'content', 'user__email')
    ordering_fields = ('user__username', 'timestamp')
    queryset = Status.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StatusDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
