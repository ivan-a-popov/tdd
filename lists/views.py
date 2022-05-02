from django.shortcuts import redirect,render
from django.http import HttpResponse
from lists.models import Item, List
from django.core.exceptions import ValidationError

# Create your views here.

def home_page(request):
   return render(request, 'home.html')

def view_list(request, list_id):
    display_list = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': display_list})

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

def add_item(request, list_id):
    current_list = List.objects.get(id=list_id)
    item = Item.objects.create(text=request.POST['item_text'], list=current_list)
    item.full_clean()
    return redirect(f'/lists/{current_list.id}/')
