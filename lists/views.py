from django.shortcuts import redirect,render
from django.http import HttpResponse
from lists.models import Item, List
from django.core.exceptions import ValidationError

# Create your views here.

def home_page(request):
   return render(request, 'home.html')

def view_list(request, list_id):
    the_list = List.objects.get(id=list_id)
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'], list=the_list)
        return redirect(f'/lists/{the_list.id}/')
    return render(request, 'list.html', {'list': the_list})

def new_list(request):
    the_list = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=the_list)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        the_list.delete()
        error="You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect(f'/lists/{the_list.id}/')

