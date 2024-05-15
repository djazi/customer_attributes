import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from loyalty_attributes.models import (
    Customer,
    LoyaltyAttribute,
    CustomerLoyaltyAttribute,
)


@pytest.mark.django_db
def test_customer_detail_view(api_client, customer_factory, user_factory):
    user = user_factory()
    api_client.force_authenticate(user=user)
    customer = customer_factory()
    url = reverse("customer_detail", args=[customer.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_next_target_customer_view(api_client, user_factory, customer_factory):
    user = user_factory()
    # create a customer manually
    customer1 = customer_factory(
        name="Khalid",
        email="test@test.com",
        birthday="1997-06-01",
        address="Lagos",
        registration_date="2000-01-01",
        loyalty_points=100,
        loyalty_level=10,
    )
    customer2 = customer_factory(
        name="Musa",
        email="test2@test.com",
        birthday="1997-06-01",
        address="Lagos",
        registration_date="2000-01-01",
        loyalty_points=100,
        loyalty_level=4,
    )
    customer3 = customer_factory(
        name="Ahmed",
        email="test3@test.com",
        birthday="1997-09-01",
        address="Lagos",
        registration_date="2000-01-01",
        loyalty_points=100,
        loyalty_level=10,
    )
    customer4 = customer_factory(
        name="Ali",
        email="test4@test.com",
        birthday="1997-06-01",
        address="Lagos",
        registration_date="2023-01-01",
        loyalty_points=100,
        loyalty_level=10,
    )
    api_client.force_authenticate(user=user)
    url = reverse("next_target_customer")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["name"] == "Khalid"


@pytest.mark.django_db
def test_list_create_loyalty_attribute_view(
    api_client, user_factory, loyalty_attribute_factory
):
    user = user_factory()
    api_client.force_authenticate(user=user)
    loyalty_attribute = loyalty_attribute_factory()
    url = reverse("list_create_loyalty_attribute")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["loyalty_level"] == loyalty_attribute.loyalty_level
    data = {"loyalty_level": 10, "points_balance": 100, "reward_status": "Active"}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["loyalty_level"] == 10
    assert response.data["points_balance"] == 100


@pytest.mark.django_db
def test_update_delete_loyalty_attribute_view(
    api_client, user_factory, loyalty_attribute_factory
):
    user = user_factory()
    api_client.force_authenticate(user=user)
    loyalty_attribute = loyalty_attribute_factory()
    url = reverse("update_delete_loyalty_attribute", args=[loyalty_attribute.id])
    data = {"loyalty_level": 9, "points_balance": 500, "reward_status": "Active"}
    response = api_client.put(url, data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["loyalty_level"] == 9
    assert response.data["points_balance"] == 500
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert LoyaltyAttribute.objects.count() == 0
