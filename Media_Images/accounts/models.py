from django.db import models

class Images(models.Model):
    name=models.CharField(max_length=100)
    images=models.ImageField(upload_to="gallery/")

    def __str__(self):
        return self.name