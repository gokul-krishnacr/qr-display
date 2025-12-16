from django.db import models

# Create your models here.
class QrCodeModel(models.Model):
    data = models.CharField(max_length=255)
    url = models.URLField(max_length=200)
    qr_image = models.ImageField(upload_to='qrcodes/')

    def __str__(self):
        return self.data