from django.db.models import Q
from django.shortcuts import render
from applications.users.forms import (
    UserSearchForm, NewSearchForm
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
        first_name = ''
        last_name = ''
        search_by = request.GET.getlist('search_by')

        if 'first_name' in search_by:
            users = users.union(User.objects.filter(
                Q(first_name__icontains=search)
            ))
            print(users)
            print("FN")
        if 'last_name' in search_by:
            users = users.union(User.objects.filter(
                Q(last_name__icontains=search)
            ))
            print(users)
            print("LN")
    print(users)
    return render(request, 'users/new_search.html', locals())