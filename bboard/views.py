from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bb, Rubric
from django.views.generic.edit import CreateView
from .forms import BbForm
from django.template import loader
from django.urls import reverse_lazy


# Пример низкоуровненго рендера страницы
# def index(request):
#    template = loader.get_template('bboard/index.html')
#    bbs = Bb.objects.order_by('-published')
#    context = {'bbs': bbs}
#    return HttpResponse(template.render(context, request))


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}

    return render(request, 'bboard/by_rubric.html', context)


class BbCreateView(CreateView):
    """ Создание новой записи с помощью CreateView """
    template_name = 'bboard/create.html' # Пусть к HTML
    form_class = BbForm # Форма из .forms
    success_url = reverse_lazy('index') # Перенаправление после удачного сохранения записи

    def get_context_data(self, **kwargs): # Функция создания контекста для прередачи в HTML
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all() # тоже самое, что rubrics = Rubric.objects.all() {'rubrics': rubrics}
        return context # добавлять в HTML не стал
