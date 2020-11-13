from django.shortcuts import render
from .models import SAV
from customers.models import Customer
from django.contrib.auth.decorators import login_required
from rest_framework_datatables_editor.viewsets import (
    DatatablesEditorModelViewSet)
from rest_framework_datatables_editor.filters import DatatablesFilterBackend
from rest_framework_datatables_editor.pagination import (
    DatatablesPageNumberPagination)
from rest_framework_datatables_editor.renderers import (DatatablesRenderer)
from rest_framework import viewsets
from .serializers import SAVSerializer
from customers.serializers import CustomerSerializer
from rest_framework.response import Response


@login_required
def index(request):
    print([{'label': obj[1], 'value': obj[0]} for obj in SAV.States.choices])
    return render(request, 'SAV/SAV.html')


def get_SAV_options():
    return "options", {
        "customer.id": [{'label': obj.lastName, 'value': obj.id} for obj in Customer.objects.all()],
        "state": [{'label': obj[1], 'value': obj[0]} for obj in SAV.States.choices]
    }


class SAVViewSet(DatatablesEditorModelViewSet):
    queryset = SAV.objects.all()
    serializer_class = SAVSerializer

    def get_options(self):
        return get_SAV_options()

    class Meta:
        datatables_extra_json = ('get_options',)


class CustomerViewSet(viewsets.ViewSet):
    queryset = Customer.objects.all().order_by('lastName')
    serializer_class = CustomerSerializer

    filter_backends = (DatatablesFilterBackend,)
    pagination_class = DatatablesPageNumberPagination
    renderer_classes = (DatatablesRenderer,)

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def get_options(self):
        return get_SAV_options()

    class Meta:
        datatables_extra_json = ('get_options',)
