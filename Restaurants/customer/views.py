from django.shortcuts import render,redirect
from .forms import BookForm
# noinspection PyUnresolvedReferences
from manager.models import CustomerOrder
from .CustomerMethods.makeOrder import makeOrder
from .CustomerMethods.CustomerOrders import getCustomerOrders






def bookTable(request):
    context = {}
    if request.POST:
        form = BookForm(request.POST)
        if form.is_valid():
            print( request.POST)
            if request.user.is_authenticated :
                custOrder = CustomerOrder(customer_id = request.user )
                custOrder.save()
                makeOrder(custOrder, request.POST, request.user)
            return redirect('restaurant-home')
        else:
            context['form'] = form
    else:
        form = BookForm()
    context['register_form'] = form
    return  render(request, 'customer/bookTable.html', context)

def customerOrder(request):
    context = {}
    orders = getCustomerOrders(request)
    context['orders'] = orders
    return render(request,'customer/CustomerOrders.html', context)