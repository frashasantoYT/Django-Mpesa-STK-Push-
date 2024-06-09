from django.shortcuts import render
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_daraja.mpesa.exceptions import MpesaInvalidParameterException
from django.urls import reverse
from .models import Transaction 
import json
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def index(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        amount = request.POST.get('amount')

        # Validation for the amount field
        try:
            amount = int(amount)
        except ValueError:
            error = 'Amount must be a valid integer kindly'
            return render(request, 'main/index.html', {'error': error})

        # Initiating the STK push
        cl = MpesaClient()
        account_reference = 'reference'
        transaction_desc = 'Description'

        callback_url = request.build_absolute_uri(reverse('stk_push_callback'))

        try:
            response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
            success = "STK Push Initiated successfully"
            return render(request, 'main/index.html', {'success': success})
        except MpesaInvalidParameterException as e:
            error = f'Failed to initiate STK push. {e}'
            return render(request, 'main/index.html', {'error': error})

    return render(request, 'main/index.html')

@csrf_exempt
def stk_push_callback(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"ResultCode": 1, "ResultDesc": "Invalid JSON payload received"}, status=400)

        logger.info(f"Received callback data: {json.dumps(data, indent=4)}")

        result_code = data['Body']['stkCallback']['ResultCode']
        result_desc = data['Body']['stkCallback']['ResultDesc']

        if result_code == 0:
            # Successful transaction
            callback_metadata = data['Body']['stkCallback']['CallbackMetadata']['Item']
            transaction = Transaction(
                transaction_id=next(item['Value'] for item in callback_metadata if item['Name'] == 'MpesaReceiptNumber'),
                amount=next(item['Value'] for item in callback_metadata if item['Name'] == 'Amount'),
                phone_number=next(item['Value'] for item in callback_metadata if item['Name'] == 'PhoneNumber'),
                account_reference=next(item['Value'] for item in callback_metadata if item['Name'] == 'AccountReference'),
                transaction_desc=result_desc,
                status='Success'
            )
            transaction.save()
        else:
            # Failed transaction
            transaction = Transaction(
                transaction_id='',
                amount=0,
                phone_number='',
                account_reference='',
                transaction_desc=result_desc,
                status='Failed'
            )
            transaction.save()

        return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})
    else:
        return JsonResponse({"ResultCode": 1, "ResultDesc": "Invalid request method"}, status=405)
