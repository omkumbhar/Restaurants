from django import forms
from .models import Table , FoodItem

class AddTable(forms.ModelForm):

    is_ac =     forms.BooleanField(label="Ac Table ",initial = True, required = False)
    capacity = forms.ChoiceField(choices=[   (1,1),(2,2),(4,4),(6,6),(8,8)])
    table_no = forms.IntegerField(label="Table No : ")
    class Meta:
        model = Table
        fields = [ 'is_ac', 'table_no' ,'capacity'  ]


class AddFoodItem(forms.ModelForm):
    foodType = forms.BooleanField( label="Veg item ",initial = True, required = False )
    name    = forms.CharField( label="Item name " )
    description = forms.CharField( label="Item description " ,widget=forms.Textarea(attrs={"rows":5, "cols":20})     )
    class Meta:
        model = FoodItem
        fields = ['foodType', 'name', 'description','price']















