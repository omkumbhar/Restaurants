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

    print(  "Time " +   formData.get('order_from_time') )
    freeTable = availableTable(formData.get('people_count'), formData.get('table_type'))
    finalOrder = FinalOrder( table_id = freeTable, order_final_id = custOrder, customer_id = user,
<<<<<<< HEAD
                             date =  formData.get('my_date_field') ,order_time = formData.get('order_from_time')+':00:00' ,total_prize = totalPrice )
    finalOrder.save()
=======
                             date =  formData.get('my_date_field') , order_time = formData.get('order_from_time')+':00:00' ,total_prize = totalPrice )
>>>>>>> 20227b6ee14f9eec87657f54545ef94dc2b704dc



    finalOrder.save()
    freeTable = Table.objects.filter( table_id = freeTable.table_id  ).first()

    freeTable.is_empty = False
    freeTable.save()
