from django.db import models
from datetime import datetime
from creators.models import Creator


class Creation(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    category = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
