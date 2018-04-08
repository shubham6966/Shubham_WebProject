from django.forms import ModelForm
from NutritionManagement.models import Breakfast

class BreakfastForm(ModelForm):
    class Meta:
        model = Breakfast
        exclude=['date']



