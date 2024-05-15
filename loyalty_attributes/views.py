from rest_framework.views import APIView
from rest_framework import status
from loyalty_attributes.models import Customer, LoyaltyAttribute
from loyalty_attributes.serializers import (
    CustomerSerializer,
    NextTargetCustomerSerializer,
    LoyaltyAttributeViewSerializer,
    UpdateLoyaltyAttributeSerializer,
)
from rest_framework.response import Response
from django.utils import timezone
from dateutil.relativedelta import relativedelta


class CustomerDetailView(APIView):
    """
    Retrieve details of a specific customer by ID..
    """

    serializer_class = CustomerSerializer

    def get(self, request, id):
        try:
            customer = Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerSerializer(customer)
        return Response(serializer.data)


class NextTargetCustomerView(APIView):
    """
    Retrieve a list of customers who is PAYBACK’s
    member for more than 10 years, his/her birthday is next month (Jun) and his loyalty
    level is more than 5.
    """

    serializer_class = NextTargetCustomerSerializer

    def get(self, request):

        today = timezone.now().date()
        next_month = today + relativedelta(months=1)
        ten_years_ago = today - timezone.timedelta(days=365 * 10)
        qualified_customers = Customer.objects.filter(
            registration_date__lte=ten_years_ago,
            birthday__month=next_month.month,
            loyalty_level__gt=5,
        )

        serializer = NextTargetCustomerSerializer(qualified_customers, many=True)
        return Response(serializer.data)


class ListCreateLoyaltyAttributeView(APIView):
    """
    Retrieve/Create a list of all available loyalty attributes.
    """

    serializer_class = LoyaltyAttributeViewSerializer

    def get(self, request):
        loyalty_attributes = LoyaltyAttribute.objects.all()
        serializer = LoyaltyAttributeViewSerializer(loyalty_attributes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LoyaltyAttributeViewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteLoyaltyAttributeView(APIView):
    """
    Update/ Delete an existing loyalty attribute by ID.
    """

    serializer_class = UpdateLoyaltyAttributeSerializer

    def put(self, request, id):
        try:
            loyalty_attribute = LoyaltyAttribute.objects.get(id=id)
        except LoyaltyAttribute.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UpdateLoyaltyAttributeSerializer(
            loyalty_attribute, data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            loyalty_attribute = LoyaltyAttribute.objects.get(id=id)
        except LoyaltyAttribute.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        loyalty_attribute.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
