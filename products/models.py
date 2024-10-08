from django.db import models


class Category(models.Model):
    """
    Model for Category of Products
    """
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Model for Products
    """
    category = models.ForeignKey(
        "Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    sku = models.CharField(max_length=12, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    shoe_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        null=True,
        blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
