from django.shortcuts import render
from rest_framework import status, generics 
from .serializers import PullRequestSerializers
from .models import PullRequest
from rest_framework.response import Response 

class PullRequestAPIView(generics.ListCreateAPIView):
    queryset = PullRequest.objects.all()
    serializer_class = PullRequestSerializers
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PullRequestUpdatePartialAPIView(generics.UpdateAPIView):
    queryset = PullRequest.objects.all()
    serializer_class = PullRequestSerializers
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "pull rquest updated successfully"})
        else:
            return Response({"message": "failed", "details": serializer.errors})