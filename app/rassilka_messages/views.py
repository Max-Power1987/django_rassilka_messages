from django.shortcuts import render
import csv
    
def send_message(request):
    phone = request.POST.get('phone')
    #print(phone)
    name_user = request.POST.get('name_user')
    text = request.POST.get('text_otpravki')#replace(' ', '')
    #print(f'{text.strip()}')
    return render(request=request, template_name='index.html',context={})

def writer(request):
    phone = request.POST.get('phone')
    #print(phone)
    name_user = request.POST.get('name_user')
    text = request.POST.get('text_otpravki')#replace(' ', '')
    #print(f'{text.strip()}')
    with open('data.csv', 'a') as f:
        writ = csv.writer(f)
        writ.writerow(phone, name_user, text)

