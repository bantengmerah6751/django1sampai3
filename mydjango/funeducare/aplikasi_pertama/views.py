from django.shortcuts import render
from django.http import HttpResponse
from aplikasi_pertama.models import Topic,Webpage, AccessRecord

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dic = {'access_records': webpages_list}
    return render(request, 'aplikasi_pertama/index.html', context=date_dic)
