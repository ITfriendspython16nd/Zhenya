from django.db import models


# Create your models here
class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    # photo = models.ImageField(upload_to="photos/%Y/%m/%d")

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name