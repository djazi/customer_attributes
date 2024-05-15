import pytest
from faker import Faker
from rest_framework.test import APIClient
from test.loyalty_attributes.factories import (
    UserFactory,
    CustomerFactory,
    LoyaltyAttributeFactory,
    CustomerLoyaltyAttributeFactory,
)


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def faker():
    return Faker()


@pytest.fixture
def user_factory(faker):
    def factory(**kwargs):
        return UserFactory(**kwargs)

    return factory


@pytest.fixture
def customer_factory(faker):
    def factory(**kwargs):
        return CustomerFactory(**kwargs)

    return factory


@pytest.fixture
def loyalty_attribute_factory(faker):
    def factory(**kwargs):
        return LoyaltyAttributeFactory(**kwargs)

    return factory


@pytest.fixture
def customer_loyalty_attribute_factory(faker):
    def factory(**kwargs):
        return CustomerLoyaltyAttributeFactory(**kwargs)

    return factory
