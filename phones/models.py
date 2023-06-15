from django.db import models
from django.utils.text import slugify



class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField
    image = models.ImageField
    release_date = models.DateField
    lte_exists = models.BooleanField
    slug = models.SlugField(unique=True, max_length=200)
   
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save()
    