from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .serializers import VendorSerializers, ConsumerSerializers
from .models import Vendor, Consumer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from .filters import VendorFilterSet, ConsumerFilterSet
from .models import Movies, Viewers
from django.db.models import F, Q, Prefetch, When, Case


class Vendor_data(ModelViewSet):
    serializer_class = VendorSerializers
    queryset = Vendor.objects.all()

    filterset_class = VendorFilterSet

    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # filterset_fields = ['name','email']
    # search_fields = ['name','email']
    # ordering_fields = ['name']

    # for understand purpose only
    def get_queryset(self):
        return Vendor.objects.all()


class Consumer_data(ModelViewSet):
    serializer_class = ConsumerSerializers
    queryset = Consumer.objects.all()

    filter_class = ConsumerFilterSet
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["name", "email", "age"]
    search_fields = ["name", "email"]
    ordering_fields = ["name", "email", "age"]

    @action(detail=True, methods=["DELETE"])
    def remove_data(self, request, pk=None):
        try:
            Consumer.objects.filter(pk=pk).delete()
            return Response({"data": "Data Deleted"}, status=status.HTTP_200_OK)
        except Consumer.DoesNotExist:
            return False


def homepage(request):
    # data = Viewers.objects.select_related("movies").annotate(
    #     name=F("movies__name"), hero=F("movies__hero")
    # )

    # movie_data = Movies.objects.select_related(
    #     Prefetch("movie_data", queryset=Viewers.objects.all(), to_attr="movie_data")
    # )
    # print(movie_data,'###############')
    # context = {"data": movie_data}

    # data = Movies.objects.filter(Case(types=When(name="fan", then=F("movies__vname"))))
    data = Movies.custome_obj.all()
    print('my all result over here', data)
    context = {"data": data}
    return render(request, "home.html", context)
