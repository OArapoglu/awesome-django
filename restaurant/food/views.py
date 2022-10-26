from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


# Create your views here.
def index(request):
    items = Item.objects.all()
    context = {"item_list": items}
    return render(request, "food/index.html", context=context)


def detail(request, id):
    item = Item.objects.get(id=id)
    context = {"item": item}
    return render(request, "food/detail.html", context=context)


def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("food:index")
    return render(request, "food/item-form.html", {"form": form})


def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("food:index")
    return render(request, "food/item-form.html", {"form": form, "item": item})


def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect("food:index")
    return render(request, "food/item-delete.html", {"item": item})