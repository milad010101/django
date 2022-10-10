from multiprocessing import context
from django.shortcuts import render
from . import models
from django.views import generic

# def Index(request):
#    A = models.Daste_Bandi_Ketab.objects.all().count()
#   B = models.Nevisandeh.objects.all().count()
#   C = models.Book.objects.all().count()
#   D = models.user.objects.all().count()
#   E = models.Book.objects.filter(status__exact='d').count()
#   return render(request, 'index.html', {'a': A, 'b': B, 'c': C, 'd': D, 'e': E})


class Index(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['a'] = models.Daste_Bandi_Ketab.objects.all().count()
        context['b'] = models.Nevisandeh.objects.all().count()
        context['c'] = models.Book.objects.all().count()
        context['d'] = models.user.objects.all().count()
        context['e'] = models.Book.objects.filter(status__exact='d').count()
        return context


class BookListView(generic.ListView):
    model = models.Daste_Bandi_Ketab
    context_object_name = 'my_favorite_publishers'

    template_name = 'book.html'


class Toozihat(generic.TemplateView):
    template_name = 'namebook.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fbook'] = models.Daste_Bandi_Ketab.objects.filter(
            Name__exact='v').count()
        return context
