from .models import Vendor, Consumer

from django_filters import rest_framework as filters
from django.db.models import Q

class VendorFilterSet(filters.FilterSet):
    merge = filters.CharFilter(method="name_and_city")
    class Meta:
        model = Vendor
        fields = {
            "id": ["exact", "in"],
            "name": ["exact","icontains"],
            "email": ["exact","icontains"],
            "city": ["exact", "icontains"]
        }

    def name_and_city(self, queryset, name, value):
        "I want to understand this function how does function work sir"  
        filters = {}
        if value:
            data = Vendor.objects.filter( Q(name=value) | Q(city=value) )
        return queryset.filter(**filters)


class ConsumerFilterSet(filters.FilterSet):

    class Meta:
        model = Consumer
        fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
            "email": ["exact", "icontains"],
            "age": ['exact',"lte","lt","gt","gte"]
        }
