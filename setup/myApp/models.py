from django.db import models

# Create your models here.
class myApp(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f"myApp: {self.title}"
    