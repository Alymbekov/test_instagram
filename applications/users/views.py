from django.db.models import Q
from django.forms import forms
from django.shortcuts import render, redirect
from applications.users.forms import (
    UserSearchForm, NewSearchForm, PersonModelForm
)
from .models import (
    User, Profile
)


def get_user(request, user_id):
    print(user_id)
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        user = None
    print(user)
    # print(locals())
    return render(request, 'users/profile.html', locals())


def search_users(request):
    # name = "asdasd"
    # hello = "asdasd"
    # print(locals())
    # request.GET.get("name", None)
    name_fragment = request.GET.get("name", None)
    users = None
    if name_fragment:
        users = User.objects.filter(
            Q(first_name__icontains=name_fragment) |
            Q(last_name__icontains=name_fragment)
        )
    if not users:
        print("ok")
        users = User.objects.all()
        # John john
    form = UserSearchForm()

    return render(request, 'users/search_results.html', locals())


def search(request):
    form = NewSearchForm()
    search = request.GET.get("text", None)
    users = User.objects.none()
    if search:
        first_name = Q(first_name__icontains=search)
        last_name = Q(last_name__icontains=search)
        search_test = None
        search_by = request.GET.getlist('search_by')
        if 'first_name' in search_by and 'last_name' in search_by:
            search_test = first_name | last_name
            print("both", search_test)
        elif 'first_name' in search_by:
            search_test = first_name
            print("first", search_test)
        elif 'last_name' in search_by:
            search_test = last_name
            print("second", search_test)
        else:
            checkbox_error = 'Чебоксы должны быть не пустыми'
            raise forms.ValidationError(checkbox_error)
        users = User.objects.filter(search_test)
        print("result", users)
    return render(request, 'users/new_search.html', locals())

#ModelForm
def add_person(request):
    form = PersonModelForm()
    if request.method == 'POST':
        form = PersonModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:test_model_form')
    return render(request, 'users/test_model_form.html', locals())









