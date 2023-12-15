from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Dataset(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='created_datasets')
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='datasets/')
    uploaded_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='uploaded_datasets', editable=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_download_url(self):
        return reverse('download-dataset', kwargs={'pk': self.pk})
    
    def delete_dataset(self):
        self.delete()
