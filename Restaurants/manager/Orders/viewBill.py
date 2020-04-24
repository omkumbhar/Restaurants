# noinspection PyUnresolvedReferences
from manager.models import Table ,FinalOrder ,OrderFood ,CustomerOrder ,FoodItem


def Orders():
    Orders =  FinalOrder.objects.all()
    return Orders