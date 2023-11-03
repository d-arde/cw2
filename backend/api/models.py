from django.db import models

# Create your models here.
class CarBrand(models.Model):
    brand_name = models.CharField(max_length = 200)
    date_founded = models.DateField("Date Founded")
    email = models.EmailField(max_length = 254)
    revenue = models.FloatField()

    def __str__(self):
        return self.brand_name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.brand_name,
            'date_founded': self.date_founded,
            'email': self.email,
            'revenue': self.revenue,
        }