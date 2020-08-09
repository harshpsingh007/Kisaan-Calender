from django.shortcuts import render
from .models import Payment
from anuj.PayTm import Checksum
from django.views.decorators.csrf import csrf_exempt

MERCHANT_KEY = 'txb0#@zEx6%vNU@6'
# Create your views here.
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        order = request.POST.get('order_id','')
        contact = Payment(name=name,order_id=order)
        contact.save()
        param_dict = {

                'MID': 'eQnNxY96458227361378',
                'ORDER_ID': str(order),
                'TXN_AMOUNT': str(5),
                'CUST_ID': name,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'paytm.html', {'param_dict': param_dict})
    return render(request, 'pricing.html')

@csrf_exempt
def handlerequest(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})