# noinspection PyUnresolvedReferences
from manager.models import Table ,FinalOrder ,OrderFood ,CustomerOrder ,FoodItem



def availableTable(peopleCount,tableType):
    if tableType == None:
        freeTable = Table.objects.filter(capacity__gte = int(peopleCount), is_ac= False, is_empty = True).first()
    else:
        freeTable = Table.objects.filter(capacity__gte = int(peopleCount) ,is_ac= True , is_empty=True  ).first()
    return freeTable


def makeOrder( custOrder , formData,user ):
    print( formData)
    totalPrice = 0

    if formData.getlist('veg_menu'):
        for orderItemsid in formData.getlist('veg_menu'):
            foodInstance = FoodItem.objects.filter(food_id=orderItemsid).first()
            itemPrice = (foodInstance.price * 1)
            totalPrice += itemPrice
            order = OrderFood(food_order_id=custOrder, food_id=foodInstance, quantity=1, cost=itemPrice)
            order.save()


    if formData.getlist('non_veg_menu'):
        for orderItemsid in formData.getlist('non_veg_menu'):
            foodInstance = FoodItem.objects.filter(food_id=orderItemsid).first()
            itemPrice = (foodInstance.price * 1)
            totalPrice += itemPrice
            order = OrderFood(food_order_id=custOrder, food_id=foodInstance, quantity=1, cost=itemPrice)
            order.save()

    freeTable = availableTable(formData.get('people_count'), formData.get('table_type'))
    finalOrder = FinalOrder( table_id = freeTable, order_final_id = custOrder, customer_id = user,
                             date =  formData.get('my_date_field') ,order_time = '09:12:45' ,total_prize = totalPrice )
    finalOrder.save()



    freeTable = Table.objects.filter( table_id = freeTable.table_id  ).first()

    freeTable.is_empty = False
    freeTable.save()
