from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def planning(request):
    return render(request, 'planning/planning.html')

def coords(request):
    data = {
        'name': request.body.GET.get(),
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data)