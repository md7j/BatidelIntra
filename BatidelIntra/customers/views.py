from django.shortcuts import render
from customers.models import Customer
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def customers(request):
    fields = Customer._meta.get_fields()[1:]
    return render(request, 'customers/customers.html', {'fields':fields})

@login_required
def customersJson(request):
    draw = int(request.GET['draw'])
    start = int(request.GET['start'])
    length = int(request.GET['length'])
    order_column = int(request.GET['order[0][column]'])
    order_direction = '' if request.GET['order[0][dir]'] == 'desc' else '-'
    column = [i.name for n, i in enumerate(Customer._meta.get_fields()) if n == order_column][0]
    global_search = request.GET['search[value]']
    all_objects = Customer.objects.all()

    columns = [i.name for i in Customer._meta.get_fields()][1:]
    objects = []
    for i in all_objects.order_by(order_direction + column)[start:start + length].values():
        ret = [i[j] for j in columns]
        objects.append(ret)
    filtered_count = all_objects.count()
    total_count = Customer.objects.count()
    return JsonResponse({
        "sEcho": draw,
        "iTotalRecords": total_count,
        "iTotalDisplayRecords": filtered_count,
        "aaData": objects,
    })

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
