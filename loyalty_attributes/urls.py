from django.urls import path
from loyalty_attributes.views import (
    CustomerDetailView,
    NextTargetCustomerView,
    ListCreateLoyaltyAttributeView,
    UpdateDeleteLoyaltyAttributeView,
)

urlpatterns = [
    path("customers/<int:id>/", CustomerDetailView.as_view(), name="customer_detail"),
    path(
        "customers/nexttarget/",
        NextTargetCustomerView.as_view(),
        name="next_target_customer",
    ),
    path(
        "loyaltyattributes/",
        ListCreateLoyaltyAttributeView.as_view(),
        name="list_create_loyalty_attribute",
    ),
    path(
        "loyaltyattributes/<int:id>/",
        UpdateDeleteLoyaltyAttributeView.as_view(),
        name="update_delete_loyalty_attribute",
    ),
]
