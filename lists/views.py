from django.shortcuts import redirect,render
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.

def home_page(request):
   return render(request, 'home.html')

def view_list(request, list_id):
    display_list = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': display_list})

def new_list(request):
    the_list = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=the_list)
    return redirect(f'/lists/{the_list.id}/')

def add_item(request, list_id):
    current_list = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=current_list)
    return redirect(f'/lists/{current_list.id}/')
