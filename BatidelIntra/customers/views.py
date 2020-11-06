from django.shortcuts import render
from .models import Customer
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from rest_framework_datatables_editor.filters import DatatablesFilterBackend
from rest_framework_datatables_editor.pagination import (
    DatatablesPageNumberPagination)
from rest_framework_datatables_editor.renderers import (DatatablesRenderer)
from rest_framework_datatables_editor.viewsets import (
    DatatablesEditorModelViewSet)

from .serializers import CustomerSerializer


@login_required
def index(request):
    return render(request, 'customers/customers.html')


# @login_required
# def customers(request):
#    fields = Customer._meta.get_fields()[1:]
#    return render(request, 'customers/customers.html', {'fields': fields})

# @login_required
# def create(request):
#     if request.method == "POST":
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('/show')
#             except:
#                 pass
#     else:
#         form = EmployeeForm()
#     return render(request, 'create.html', {'form': form})


# from django.shortcuts import render, redirect
# from employee.forms import EmployeeForm
# from employee.models import Employee

#    def emp(request):
#         if request.method == "POST":
#             form = EmployeeForm(request.POST)
#             if form.is_valid():
#                 try:
#                     form.save()
#                     return redirect('/show')
#                 except:
#                     pass
#         else:
#             form = EmployeeForm()
#         return render(request, 'index.html', {'form': form})

#     def show(request):
#         employees = Employee.objects.all()
#         return render(request, "show.html", {'employees': employees})

#     def edit(request, id):
#         employee = Employee.objects.get(id=id)
#         return render(request, 'edit.html', {'employee': employee})

#     def update(request, id):
#         employee = Employee.objects.get(id=id)
#         form = EmployeeForm(request.POST, instance=employee)
#         if form.is_valid():
#             form.save()
#             return redirect("/show")
#         return render(request, 'edit.html', {'employee': employee})

#     def destroy(request, id):
#         employee = Employee.objects.get(id=id)
#         employee.delete()
#         return redirect("/show")


class CustomerViewSet(DatatablesEditorModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
#    permission_classes = [permissions.IsAuthenticated]

#    filter_backends = (DatatablesFilterBackend,)
#    pagination_class = DatatablesPageNumberPagination
#    renderer_classes = (DatatablesRenderer,)
