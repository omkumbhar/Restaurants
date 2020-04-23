from django.db import models
# noinspection PyUnresolvedReferences
from account.models import Account

class Table(models.Model):
    table_id                        = models.AutoField(primary_key=True)
    table_no                        = models.IntegerField()
    is_ac                           = models.BooleanField(default=False)
    is_empty                        = models.BooleanField(default=True)
    capacity                        = models.IntegerField()
    start_reservation_time          = models.DateTimeField( null= True )
    end_reservation_time            = models.DateTimeField( null= True )
    def __str__(self):
        return  str(self.table_id)

class FoodItem(models.Model):
    food_id                         = models.AutoField(primary_key = True)
    name                            = models.CharField(max_length = 60)
    description                     = models.CharField(max_length = 100)
    foodType                        = models.BooleanField(default = True )   # value  is True for veg dishes
    price                           = models.IntegerField()

    def __str__(self):
        return str(self.food_id)

class CustomerOrder(models.Model):
    order_id                        = models.AutoField(primary_key=True)
    customer_id                     = models.ForeignKey(Account, on_delete=models.CASCADE)
    is_complted                     = models.BooleanField(default = False)

    def __str__(self):
        return str(self.order_id)

class OrderFood(models.Model):
    food_order_id                   = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE)
    food_id                         = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity                        = models.IntegerField()
    cost                            = models.IntegerField()

    def __str__(self):
        return str(self.food_order_id)

class FinalOrder(models.Model):
    order                           = models.AutoField(primary_key=True)
    table_id                        = models.ForeignKey(Table,on_delete=models.CASCADE)
    order_final_id                  = models.ForeignKey(CustomerOrder,on_delete=models.CASCADE)
    customer_id                     = models.ForeignKey(Account, on_delete=models.CASCADE)
    date                            = models.DateField()
    order_time                      = models.TimeField()
    # order_till_time = models.TimeField()
    # order_from_time = models.TimeField()
    total_prize                     = models.IntegerField()

    def __str__(self):
        return str(self.order)

