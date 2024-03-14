from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Item
from .forms import ItemCreationForm

# Create your views here.


def index(request):
    item_list = Item.objects.all()
    return render(request, "food/index.html", {
        "item_list": item_list,
    })


def item(request):
    return HttpResponse("This is an item view")


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(request, "food/detail.html", {
        "item": item,
    })


def create_item(request):
    form = ItemCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, "food/item-form.html", {
        "form": form,
    })


def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemCreationForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect("food:index")
    return render(request, "food/item-form.html", {
        "item": item,
        "form": form,
    })


def delete_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == "POST":
        item.delete()
        return redirect("food:index")

    return render(request, "food/item-delete.html", {
        "item": item
    })
