from django.db import models


# Create your models here
class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name