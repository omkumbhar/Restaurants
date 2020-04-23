from django.contrib import admin
from  .models import Table ,FoodItem , CustomerOrder, OrderFood , FinalOrder

class TableAdmin(admin.ModelAdmin):
    list_display = [ 'table_no' ,'is_ac','is_empty','capacity', ]
    search_fields = ['table_no','capacity']
    readonly_fields = [ 'table_id','start_reservation_time','end_reservation_time',]


    filter_horizontal = []
    list_filter = []
    fieldsets = []
    ordering = []

admin.site.register(Table,TableAdmin)

class FoodItemAdmin(admin.ModelAdmin):
    list_display = [ 'food_id' ,'name','foodType','description','price' ]
    search_fields = ['foodType','name']
    readonly_fields = [ 'food_id','foodType','price',]


    filter_horizontal = []
    list_filter = []
    fieldsets = []
    ordering = []

admin.site.register(FoodItem,FoodItemAdmin)

class CustomerOrderAdmin(admin.ModelAdmin):
    list_display = [ 'order_id' ,'customer_id', 'is_complted']
    search_fields = ['order_id']
    readonly_fields = [ 'order_id' ,]

    filter_horizontal = []
    list_filter = []
    fieldsets = []
    ordering = []

admin.site.register(CustomerOrder,CustomerOrderAdmin)


class OrderFoodAdmin(admin.ModelAdmin):
    list_display = [ 'id','food_order_id' ,'quantity','cost' ]
    search_fields = ['food_order_id']
    readonly_fields = [ ]

    filter_horizontal = []
    list_filter = []
    fieldsets = []
    ordering = []

admin.site.register(OrderFood,OrderFoodAdmin)


class FinalOrderAdmin(admin.ModelAdmin):
    list_display = [ 'order','table_id' ,'order_final_id',  'customer_id' ,'total_prize' ]
    search_fields = ['order','customer_id','table_id']
    readonly_fields = ['order' ]

    filter_horizontal = []
    list_filter = []
    fieldsets = []
    ordering = []

admin.site.register(FinalOrder,FinalOrderAdmin)
