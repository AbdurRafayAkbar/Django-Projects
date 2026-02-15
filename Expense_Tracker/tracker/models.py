from django.db import models

class expense_model(models.Model):
    Title=models.CharField(max_length=50)
    Amount=models.FloatField()
    Category=models.CharField(max_length=100)
    Date=models.DateField()
    Description=models.TextField()

    def __str__(self):
        return self.Title