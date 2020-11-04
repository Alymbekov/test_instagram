from django.shortcuts import render, redirect

from applications.insta.forms import NewFormApplication
from .models import (
    InstaPost, HashTag,
    InstaImage, ApplicationForm)


def index(request):
    return render(request, 'insta/index.html', {})


def get_all_posts(request):
    #all( ) select * from table
    posts = InstaPost.objects.all()
    return render(request, 'insta/posts.html', locals())


def get_details(request, id):
    post = InstaPost.objects.get(pk=id)
    return render(request, 'insta/post_details.html', locals())


def success_message(request):
    return render(request, 'insta/success_msg.html', locals())


def create_app_form(request):
    print("Types of method: ", request.method)
    if request.method == "GET":
        return render(request, 'insta/applications_form.html', locals())

    elif request.method == "POST":
        # print(request.method)
        # print(request.path)
        # print(request.FILES)
        # print(request.body)
        # print(request.build_absolute_uri())
        # print(request.get_full_path_info())
        # print(request.get_host())
        # print(request.get_port())
        # print(request)

        # print(request.POST)
        email = request.POST.get("email")
        address = request.POST.get("address")
        city = request.POST.get("city")
        is_check = request.POST.get("check")
        klass = ApplicationForm
        if email and address and city and is_check:
            if klass.is_check_true(is_check):
                obj = klass(
                    email=email, address=address,
                    city=city, check=klass.is_check_true(is_check)
                )
                obj.save()
                #PRG - pattern /PostRedirectGet/
                return redirect('success_msg')

        return render(request, 'insta/applications_form.html', locals())


def new_application_form(request):
    form = NewFormApplication()
    if request.method == 'POST':
        form = NewFormApplication(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            phones = form.cleaned_data['phone_numbers']
            print(email, address, city, phones)
            app_form = ApplicationForm.objects.create(
                address=address, city=city,
                email=email, phone_number=phones
            )
            return redirect('new_form')
    return render(request, 'insta/new_form.html', locals())


