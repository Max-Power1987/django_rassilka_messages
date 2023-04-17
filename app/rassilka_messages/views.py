from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import TemplateView
from .tg_send_message import Tg_sender


class pars_message(View):
    def request_text(self, request, *args, **kwargs):
        sender = Tg_sender()
        phone = request.POST.get('phone')
        name_user = request.POST.get('name_user')
        text = request.POST.get('text_otpravki')#replace(' ', '')
        sender.send_phone(phone, text)

def get_context_data(request):
    return render(request=request, template_name='index.html',context={})
