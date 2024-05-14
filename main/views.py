from django.shortcuts import render
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse
from django_daraja.mpesa.exceptions import MpesaInvalidParameterException



def index(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        amount = request.POST.get('amount')


        #Validation for the amount field
        try:
            amount = int(amount)
        except ValueError:
            error = 'Amount must be a valid integer kindly'
            return render(request, 'index.html', {'error': error})
        
        
        # initiating the STK push 
        cl = MpesaClient()
        account_reference = 'reference'
        transcation_desc = 'Description'
       
        callback_url = '' #enter your callback url here

        try:
            response = cl.stk_push(phone_number, amount, account_reference, transcation_desc, callback_url)
            success = "STK Push Initiated successfully"
        except MpesaInvalidParameterException as e:
            error = f'Failed to initiate STK push. {e}'
            return render(request, 'index.html', {'error':error})

    return render(request, 'main/index.html')
  

def stk_push_callback(request):
    return HttpResponse("🔥STK Push callback received successfully")

