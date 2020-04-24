# noinspection PyUnresolvedReferences
from manager.models import Table ,FinalOrder ,OrderFood ,CustomerOrder ,FoodItem


def Orders(request):
    Orders =  FinalOrder.objects.filter( customer_id = request.user)
    return Orders