# dataset/urls.py
'''from django.urls import path
from dataset.views import DatasetUploadView, UserDatasetsView, DatasetDownloadView, DatasetDeleteView, DatasetSearchView, DatasetDetailView

urlpatterns = [
    path('upload/', DatasetUploadView.as_view(), name='upload-dataset'),
    path('', UserDatasetsView.as_view(), name='user-datasets'),
    path('<int:pk>/download/', DatasetDownloadView.as_view(), name='download-dataset'),
    path('<int:pk>/delete/', DatasetDeleteView.as_view(), name='delete-dataset'),
    path('search/<str:dataset_name>/', DatasetSearchView.as_view(), name='search-datasets'), 
    path('<int:pk>/', DatasetDetailView.as_view(), name='view-dataset'),
]
'''

from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.dataset_upload_view, name='dataset-upload'),
    path('user_datasets/', views.user_datasets_view, name='user-datasets'),
    path('download/<int:pk>/', views.dataset_download_view, name='dataset-download'),
    path('delete/<int:pk>/', views.dataset_delete_view, name='dataset-delete'),
    path('search/<str:dataset_name>/', views.dataset_search_view, name='dataset-search'),
    path('detail/<int:pk>/', views.dataset_detail_view, name='dataset-detail'),
]
