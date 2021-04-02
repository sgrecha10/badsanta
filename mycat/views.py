from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

# from rest_framework.views import APIview
#
#
# class PrepareDataViews(rest_framework.views)
def test_button(request):
    messages.set_level(request, messages.SUCCESS)
    messages.success(request, f'Вот такое сообщение тут!')
    return redirect(reverse('admin:index'))