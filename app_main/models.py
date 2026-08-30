from django.db import models

class CourseModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    duration = models.PositiveIntegerField(default=12)