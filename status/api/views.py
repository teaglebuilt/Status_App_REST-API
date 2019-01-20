from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from status.models import Status
from .serializers import StatusSerializer
from django.shortcuts import get_object_or_404


class StatusAPIView(mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs =  Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None)
        qs = self.get_queryset()
        if passed_id is not None:
            obj = get_object_or_404(qs, id=passed_id)
        return obj

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



# class StatusDetailAPIView(generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

# class StatusDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


