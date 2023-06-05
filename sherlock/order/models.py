from django.db import models


class CreditApplication(models.Model):
    contract = models.OneToOneField('Contract', on_delete=models.CASCADE, related_name='credit_applications')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Credit Application {self.pk}"


class Contract(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contract {self.pk}"


class Product(models.Model):
    credit_application = models.ForeignKey('CreditApplication', on_delete=models.CASCADE, related_name='products')
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE,related_name="products")
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Product {self.pk}"


class Manufacturer(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Manufacturer {self.pk}"
