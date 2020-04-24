from django.shortcuts import render ,redirect
from .forms import AddTable ,AddFoodItem
from .models import CustomerOrder, FinalOrder
from .Orders.viewBill import Orders


def home(request):
    return render(request, "manager/managerHome.html")

def addTable(request):
    context = {}
    if request.POST:
        form = AddTable(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manager-addTable')
        else:
            context['table_form'] = form
    else:
        form = AddTable()
    context['table_form'] = form
    return  render(request, 'manager/addTable.html', context)




def addFoodItem(request):
    context = {}
    if request.POST:
        form = AddFoodItem(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manager-addFoodItem')
        else:
            context['item_form'] = form
    else:
        form = AddFoodItem()
    context['item_form'] = form
    return render(request, 'manager/addMenu.html', context)




def viewOrders(request):
    context = {}
    orders = CustomerOrder.objects.filter(is_complted = True)

    return render(request, 'manager/viewOrders.html', context)



def viewBill(request):
    context = {}
    orders = Orders()
    context['orders'] = orders
    return render(request, 'manager/viewBill.html', context)








