from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import BreakfastForm
from .models import Breakfast,Nutrients
import datetime
# Create your views here.


today_date = datetime.datetime.today()
def index(request):
    return render(request,'NutritionMangement/index.html')


def breakfast(request):


        if request.method == 'POST':
            break_form = BreakfastForm(request.POST)
            if break_form.is_valid():
                break_form.save(commit=True)
                # if break_form.cleaned_data['add']:
                #     break_form = BreakfastForm()
                #     return render(request, "NutritionMangement/breakfast.html", {"break_form": break_form})
                #print(break_form.cleaned_data['submit'])
                if 'submit' in request.POST:
                    return HttpResponseRedirect('/')
                else:
                    break_form = BreakfastForm()
                    eat_today = Breakfast.objects.filter(date=datetime.datetime.today().date())
                    print(eat_today)
                    return render(request, "NutritionMangement/breakfast.html",
                                  {"break_form": break_form, 'date': today_date, 'eat_today': eat_today})

            else:
                return HttpResponse("Not valid")


        else:
            break_form = BreakfastForm()
            eat_today = Breakfast.objects.filter(date=datetime.datetime.today().date())
            print(eat_today)
            return render(request,"NutritionMangement/breakfast.html",{"break_form":break_form,'date':today_date,'eat_today':eat_today})




def NutrientsCalc(request):
    eat_today= Breakfast.objects.filter(date=datetime.datetime.today().date())
    # nutrients = .objects.all()
    if eat_today :
        total_calorie = 0
        intake_today = []
        for item in eat_today:
            gain_today = Nutrients.objects.get(item_name=item.Item)
            gain_today.calorie = gain_today.calorie * item.quantity
            intake_today.append(gain_today)
            total_calorie = int(gain_today.calorie)+total_calorie
            print(gain_today)


        return render(request, 'NutritionMangement/Calories.html', {'intake_today': intake_today,'total_calorie':total_calorie})
    else:
        length = eat_today.count()
        break_form = BreakfastForm()
        print(length)
        return render(request,'NutritionMangement/breakfast.html',{'eat_nothing':length,"break_form":break_form,'date':today_date})



def breakfast_edit(request,item_id):
    edit_form = Breakfast.objects.get(id = item_id)
    if request.method == 'POST':
        edit_name = request.POST.get('name_item')
        edit_quantity = request.POST.get('quantity')
        if edit_name:
            edit_form.Item=edit_name
        else:
            edit_form.Item = edit_form.Item
        if edit_quantity:
            edit_form.quantity=edit_quantity
        else:
            edit_form.quantity = edit_form.quantity
        edit_form.save()
        break_form = BreakfastForm()
        eat_today = Breakfast.objects.filter(date=datetime.datetime.today().date())
        return render(request,"NutritionMangement/breakfast.html",{"break_form":break_form,'date':today_date,'eat_today':eat_today})



def breakfast_delete(request,item_id):

    try:
        edit_form = Breakfast.objects.get(id=item_id)
        if request.method == 'POST':
            edit_form.delete()
            break_form = BreakfastForm()
            eat_today = Breakfast.objects.filter(date=datetime.datetime.today().date())
            return render(request,"NutritionMangement/breakfast.html",{"break_form":break_form,'date':today_date,'eat_today':eat_today})

    except:
        break_form = BreakfastForm()
        eat_today = Breakfast.objects.filter(date=datetime.datetime.today().date())
        return render(request, "NutritionMangement/breakfast.html",
                      {"break_form": break_form, 'date': today_date, 'eat_today': eat_today})









