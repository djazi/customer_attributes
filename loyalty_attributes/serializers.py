from rest_framework import serializers
from loyalty_attributes.models import Customer, LoyaltyAttribute


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class NextTargetCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "id",
            "name",
            "email",
            "birthday",
            "registration_date",
            "loyalty_points",
            "loyalty_level",
        )


class LoyaltyAttributeViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoyaltyAttribute
        fields = "__all__"


class UpdateLoyaltyAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoyaltyAttribute
        fields = "__all__"
