from django.shortcuts import render
from subscribe_app.models import Customer
from subscribe_app.forms import NewSubscribe

# Create your views here.
def index(request):
    return render(request, 'subscribe_app/index.html')

def customers(request):
    customer_list = Customer.objects.order_by('first_name')
    customer_dict = {'customers':customer_list}
    return render(request, 'subscribe_app/customers.html', context=customer_dict)

def subscribe(request):
    form = NewSubscribe()
    if request.method == "POST":
        form = NewSubscribe(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return customers(request)
        else:
            print("Error coyyy")
    return render(request, 'subscribe_app/subscribe.html', {'form':form})