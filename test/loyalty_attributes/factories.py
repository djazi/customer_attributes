import factory
from factory.django import DjangoModelFactory
from faker import Faker

from django.contrib.auth.models import User
from loyalty_attributes.models import (
    LoyaltyAttribute,
    CustomerLoyaltyAttribute,
    Customer,
)


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.Faker("password")


class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = Customer

    name = factory.Faker("name")
    email = factory.Faker("email")
    birthday = factory.Faker("date_of_birth")
    address = factory.Faker("address")
    registration_date = factory.Faker("date_time")
    loyalty_points = factory.Faker("random_int")
    loyalty_level = factory.Faker("random_int")


class LoyaltyAttributeFactory(DjangoModelFactory):
    class Meta:
        model = LoyaltyAttribute

    loyalty_level = factory.Faker("random_int")
    points_balance = factory.Faker("random_int")
    reward_status = factory.Faker("word")


class CustomerLoyaltyAttributeFactory(DjangoModelFactory):
    class Meta:
        model = CustomerLoyaltyAttribute

    customer = factory.SubFactory(CustomerFactory)
    attribute = factory.SubFactory(LoyaltyAttributeFactory)
