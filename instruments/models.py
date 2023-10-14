from django.db import models

# Create your models here.

class Instrument(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    type = models.CharField(max_length=255)
    photo = models.ImageField()

    def __str__(self):
        return self.name

class Order(models.Model):
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order for {self.instrument.name} by {self.customer_name}"
