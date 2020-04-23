from django import forms
# noinspection PyUnresolvedReferences
from  manager.models import FoodItem



class DateInput(forms.DateTimeInput):
    input_type = 'date'


class BookForm(forms.Form):
    nonVegItems = FoodItem.objects.filter(foodType=False)
    vegItems = FoodItem.objects.filter(foodType=True)

    nonVeg = []
    vegMenu = []

    for i in nonVegItems: nonVeg.append(( str(i.pk), str( i.name ) ))

    for j in vegItems: vegMenu.append(( str(j.pk), str( j.name ) ))

    allowedFromTime = [     ( "9"  , "9.00 am"),
                        ("10" ,"10.00 am"),
                        ("11","11.00 am"),
                        ("12","12.00 pm"),
                        ("1","1.00 pm"),
                        ( "2","2.00 pm"),
                        ("3","3.00 pm"),
                        ("4" ,"4.00 pm"),
                        ("5","5.00 pm "),
                        ("6","6.00 pm"),
                        ("7","7.00 pm"),
                        ("8","8.00 pm"),
                        ("9","9.00 pm"),
                        ("10" ,"10.00 pm"),    ]


    allowedPeople = [  ( "2",2 ), ( "4",4 ),( "6",6 ),( "8",8 ),( "10",10 ),( "20",20 ) ]


    # Fields
    my_date_field = forms.DateField(widget=DateInput)
    table_type = forms.BooleanField( label="Ac table ",initial = True, required = False  )
    order_from_time = forms.CharField(label='Select Time for booking ', widget=forms.Select(choices=allowedFromTime) )

    people_count = forms.IntegerField(label='Table for ', widget=forms.Select(choices=allowedPeople))
    non_veg_menu = forms.MultipleChoiceField( required=False,widget=forms.CheckboxSelectMultiple, choices=nonVeg)

    veg_menu = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple, choices=vegMenu)







