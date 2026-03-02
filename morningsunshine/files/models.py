from django.db import models

class uploadDocuments(models.Model):
    pdf = models.FileField(upload_to='pdfs') 
    photo = models.FileField(upload_to='photos')