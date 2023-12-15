# dataset/views.py
'''from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from dataset.models import Dataset
from dataset.serializers import DatasetSerializer
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.db.models import Q

class DatasetUploadView(generics.CreateAPIView):
    serializer_class = DatasetSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, email=self.request.user.email)

class UserDatasetsView(generics.ListAPIView):
    serializer_class = DatasetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Dataset.objects.filter(user=self.request.user)

class DatasetDownloadView(APIView):
    def get(self, request, pk):
        dataset = get_object_or_404(Dataset, pk=pk)
        file_path = dataset.file.path
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{dataset.file.name}"'
        return response

class DatasetDeleteView(generics.DestroyAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class DatasetSearchView(generics.ListAPIView):
    serializer_class = DatasetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        dataset_name = self.kwargs.get('dataset_name')
        user_datasets = Dataset.objects.filter(user=self.request.user)
        return user_datasets.filter(name__icontains=dataset_name)

class DatasetDetailView(generics.RetrieveAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    permission_classes = [IsAuthenticated]
'''
'''
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from dataset.models import Dataset
from dataset.serializers import DatasetSerializer
from django.shortcuts import get_object_or_404
from django.http import FileResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.db.models import Q

class DatasetUploadView(generics.CreateAPIView):
    serializer_class = DatasetSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, email=self.request.user.email)
        return Response({"message": "Dataset uploaded successfully"}, status=201)

class UserDatasetsView(generics.ListAPIView):
    serializer_class = DatasetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        datasets = Dataset.objects.filter(user=self.request.user)
        if datasets.exists():
            return datasets
        return Response({"message": "No datasets found for this user"}, status=404)

class DatasetDownloadView(APIView):
    def get(self, request, pk):
        dataset = get_object_or_404(Dataset, pk=pk)
        file_path = dataset.file.path
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{dataset.file.name}"'
        return response

class DatasetDeleteView(generics.DestroyAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            self.perform_destroy(instance)
            return Response({"message": "Dataset deleted successfully"}, status=204)
        return Response({"message": "Dataset not found or could not be deleted"}, status=404)

class DatasetSearchView(generics.ListAPIView):
    serializer_class = DatasetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        dataset_name = self.kwargs.get('dataset_name')
        user_datasets = Dataset.objects.filter(user=self.request.user)
        datasets = user_datasets.filter(name__icontains=dataset_name)
        if datasets.exists():
            return datasets
        return Response({"message": "No datasets found with this name"}, status=404)

class DatasetDetailView(generics.RetrieveAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    permission_classes = [IsAuthenticated]
'''

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from dataset.models import Dataset
from dataset.serializers import DatasetSerializer
from django.shortcuts import get_object_or_404
from django.http import FileResponse

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def dataset_upload_view(request):
    serializer = DatasetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, email=request.user.email)
        return Response({"message": "Dataset uploaded successfully"}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_datasets_view(request):
    datasets = Dataset.objects.filter(user=request.user)
    if datasets.exists():
        serializer = DatasetSerializer(datasets, many=True)
        return Response(serializer.data, status=200)
    return Response({"message": "No datasets found for this user"}, status=404)

@api_view(['GET'])
def dataset_download_view(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk)
    file_path = dataset.file.path
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{dataset.file.name}"'
    return response

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def dataset_delete_view(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk)
    if dataset.user == request.user:
        dataset.delete()
        return Response({"message": "Dataset deleted successfully"}, status=204)
    return Response({"message": "Dataset not found or could not be deleted"}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dataset_search_view(request, dataset_name):
    user_datasets = Dataset.objects.filter(user=request.user)
    datasets = user_datasets.filter(name__icontains=dataset_name)
    if datasets.exists():
        serializer = DatasetSerializer(datasets, many=True)
        return Response(serializer.data, status=200)
    return Response({"message": "No datasets found with this name"}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dataset_detail_view(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk)
    serializer = DatasetSerializer(dataset)
    return Response(serializer.data, status=200)
