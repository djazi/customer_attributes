from django.db import models
from django.utils import timezone

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Customer(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    birthday = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)
    registration_date = models.DateTimeField(default=timezone.now)
    loyalty_points = models.IntegerField(default=0)
    loyalty_level = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class LoyaltyAttribute(BaseModel):
    loyalty_level = models.IntegerField(default=0)
    points_balance = models.IntegerField(default=0)
    reward_status = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.loyalty_level} - {self.points_balance}"


class CustomerLoyaltyAttribute(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    attribute = models.ForeignKey(LoyaltyAttribute, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("customer", "attribute"),)

    def __str__(self):
        return f"{self.customer} - {self.attribute}"
