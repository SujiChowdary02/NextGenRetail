from django.db import models

class Prediction(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    dataset = models.ForeignKey('yourapp.Dataset', on_delete=models.CASCADE)
    prediction_result = models.FloatField()
    prediction_date = models.DateTimeField(auto_now_add=True)

    # Add other fields as required
