from django.shortcuts import render
from . import models


def Index(request):
    A = models.Daste_Bandi_Ketab.objects.all().count()
    B = models.Nevisandeh.objects.all().count()
    C = models.Book.objects.all().count()
    D = models.user.objects.all().count()
    E = models.Book.objects.filter(status__exact='d').count()
    return render(request, 'index.html', {'a': A, 'b': B, 'c': C, 'd': D, 'e': E})
