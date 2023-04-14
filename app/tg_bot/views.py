from django.http import HttpRequest
def sender(HttpRequest):
    phone = HttpRequest.POST.get('phone')
    #name_user = request.POST.get('name_user')
    #text = request.POST.get('text_otpravki').replace(' ', '')
    print(phone)
