from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=150, null=True)
    product_type = models.CharField(max_length=25, null=True)
    product_description = models.TextField()
    affliate_url = models.SlugField(blank=True, null=True)
    product_image = models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return f"{self.product_name}"
