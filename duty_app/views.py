from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import PersonModel
# import django
# import datetime
from django.utils import timezone


@login_required
def home(request):
    if request.user.username != 'ordenmeny':
        return redirect('clubs_app:home_page')

    person_model = PersonModel.objects.all()

    context = {
        'person_model': person_model,
    }

    return render(request, template_name='duty_app/index.html', context=context)


def action_duty(request, type_action, id_person):
    person_model = PersonModel.objects.get(pk=id_person)
    context = {

    }
    if type_action == 'to_duty':
        # установить, что человек подежурил
        person_model.active = True
        person_model.date_duty = timezone.now()
        print(timezone.now())
        person_model.save()
        return redirect('duty_app:home')
    elif type_action == 'from_duty':
        person_model.active = False
        person_model.date_duty = None
        person_model.save()
        # установить, что человек НЕ подежурил
        return redirect('duty_app:home')
