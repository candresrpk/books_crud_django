from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    image = models.ImageField(upload_to='images/', null=True, verbose_name='Image')
    desciption = models.TextField(null=True, verbose_name='Description')
    
    
    def __str__(self) -> str:
        return f'{self.title}'
    
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()