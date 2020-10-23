from django.shortcuts import render

from django.contrib.auth.decorators import login_required


@login_required
def planning(request):
    return render(request, 'planning/planning.html')