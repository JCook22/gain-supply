from django.db import models


class Testimonial(models.Model):
    customer_name = models.CharField(max_length=254) 
    customer_age = models.IntegerField(max_digits=3, null=True, blank=True)
    customer_county = models.CharField(max_length=80, null=True, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    headline = models.Charfield(max_length=254)
    body = models.TextField()

    def __str__(self):
        return self.customer_name
