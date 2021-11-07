from django.db import models

# Create your models here.
class Bank(models.Model):
    ifsc = models.CharField(max_length=11)
    bank_id = models.IntegerField()
    branch = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    district = models.CharField(max_length=256)
    state = models.CharField(max_length=256)

    def __str__(self):
        return self.ifsc
