import pytest
from loyalty_attributes.models import (
    Customer,
    LoyaltyAttribute,
    CustomerLoyaltyAttribute,
)


@pytest.mark.django_db
def test_customer_model(customer_factory):
    customer = customer_factory()
    assert isinstance(customer, Customer)
    assert customer.__str__() == customer.name


@pytest.mark.django_db
def test_loyalty_attribute_model(loyalty_attribute_factory):
    loyalty_attribute = loyalty_attribute_factory()
    assert isinstance(loyalty_attribute, LoyaltyAttribute)
    assert loyalty_attribute.__str__() == f"{loyalty_attribute.loyalty_level} - {loyalty_attribute.points_balance}"


@pytest.mark.django_db
def test_customer_loyalty_attribute_model(customer_loyalty_attribute_factory):
    customer_loyalty_attribute = customer_loyalty_attribute_factory()
    assert isinstance(customer_loyalty_attribute, CustomerLoyaltyAttribute)
