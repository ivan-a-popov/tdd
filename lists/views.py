from django.shortcuts import redirect,render
from lists.models import Item, List
from django.core.exceptions import ValidationError
from lists.forms import ItemForm, ExistingListItemForm, NewListForm
from django.contrib.auth import get_user_model

User = get_user_model()


def home_page(request):
   return render(request, 'home.html', {'form': ItemForm()})


def view_list(request, list_id):
    the_list = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=the_list)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=the_list, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(the_list)
    return render(request, 'list.html', {"list": the_list, "form": form})


def new_list(request):
    form = NewListForm(data=request.POST)
    if form.is_valid():
        the_list = form.save(owner=request.user)
        return redirect(the_list)
    return render(request, 'home.html', {'form': form})

def my_lists(request, email):
    owner = User.objects.get(email=email)
    return render(request, 'my_lists.html', {'owner': owner})

