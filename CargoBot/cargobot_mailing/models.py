from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.TextField()
    email = models.EmailField(null=True)
    telegram = models.TextField()
    telegram_id = models.PositiveIntegerField(unique=True)
    phone_number = models.TextField()
    paid_to = models.DateField()
    comments = models.TextField()


class Customer(models.Model):
    external_id = models.PositiveIntegerField(unique=True)
    telegram = models.TextField(null=True)


class CustomerRequest(models.Model):
    city_from = models.TextField()
    city_to = models.TextField()
    cargo_description = models.TextField()
    cargo_weight = models.FloatField()
    cargo_volume = models.FloatField()
    box_amount = models.PositiveIntegerField()

    class TransportChoices(models.TextChoices):
        AVIA = 'Авиа-доставка'
        RAILWAY = 'Жд-доставка'
        SEA = 'Морская доставка'
        AVTO = 'Авто-доставка'

    transport = models.CharField(
        choices=TransportChoices.choices,
        max_length=50
    )
    cargo_value = models.FloatField()


class CompanyReply(models.Model):
    price = models.FloatField()
    delivery_time = models.PositiveIntegerField()
    comment = models.TextField(max_length=300, null=True)
    reply_to = models.ForeignKey(CustomerRequest, on_delete=models.CASCADE)
