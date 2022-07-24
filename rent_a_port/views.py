from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from rent_a_port.models import ContactForm, Property
from datetime import datetime
import PIL


# Create your views here.

def index(request):
    return render(request, "index.html")


def loginu(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            global uid
            uid = int(user.id)
            return render(request, "index.html", {'fname': fname, "username": username})
        else:
            messages.error(request, "bad credentials")

    return render(request, "login.html")


def logoutu(request):
    logout(request)
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        username = request.POST["username"]
        number = request.POST["number"]
        email = request.POST["email"]
        password = request.POST["pass"]
        password2 = request.POST["passc"]

        # if User.objects.filter(username=username):
        #     messages.error(request, "This username is taken")
        #     return redirect('signup')

        if password != password2:
            messages.error(request, "Passwords do not match.")
            # return redirect('/signup')
        elif User.objects.filter(email=email):
            messages.error(request, "This username is taken")
        elif User.objects.filter(username=username):
            messages.error(request, "This username is taken")
        else:

            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.contact_number = number

            myuser.save()

            messages.success(request, "Account created successfully")

            return redirect('login')

    return render(request, "signup.html")


def contactu(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mail = request.POST.get("email")
        message = request.POST["message"]
        contact = ContactForm(name=name, email=mail, message=message, date=datetime.today())
        contact.save()
        messages.success(request, "submitted successfully")
        print("saved")
    return render(request, "contacts.html")


def about(request):
    return render(request, "about.html")


def add_p(request):
    if uid < 0:
        return render(request, "login.html")

    if request.method == "POST":
        address = request.POST.get('Address')
        rent = request.POST.get("Rent")
        deposit = request.POST["Deposit"]
        maintenance = request.POST["Maintenance"]
        phone = request.POST["Phone"]
        mail = request.POST["email"]
        in_img = request.FILES["in_img"]
        out_img = request.FILES["out_img"]

        add_property = Property(address=address, rent=rent, deposit=deposit, maintenance=maintenance, phone=phone,
                                mail=mail, uid=uid, in_img=in_img, out_img=out_img)
        add_property.save()
        messages.success(request, "Property Added  successfully")
        print("saved")
        return render(request, "add-property.html")

    return render(request, "add-property.html")


def propertys(request):
    print('hello')
    if request.method == "POST":

        searched = request.POST["search"]
        print(searched)
        serched_property = Property.objects.filter(address__contains=searched)

        print(serched_property)
        context = {'serched_property': serched_property, 'searched': searched}
        return render(request, "property.html", context)
    else:

        return render(request, "property.html")


# def propertys(request):
#     all_property = Property.objects.filter()
#     context = {'all_property': all_property}
#
#     return render(request, "property.html", context)


def base(request):
    return render(request, "base.html")
