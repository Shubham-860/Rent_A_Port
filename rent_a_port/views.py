from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from rent_a_port.models import ContactForm, Property, NewsLetter
from datetime import datetime
from django.core.mail import send_mail


# Create your views here.

def index(request):
    if request.method == "POST":
        mail = request.POST["email"]
        news = NewsLetter(news_mail=mail)
        news.save()
        messages.success(request, "E-mail submitted successfully")

    return render(request, "index.html")


def loginu(request, previous_url=0):
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
    previous_url = int(previous_url)
    if previous_url == 0:
        return render(request, "login.html")
    else:
        return HttpResponseRedirect(previous_url)


def logoutu(request):
    logout(request)
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        username = request.POST["username"]
        contact_number = request.POST["number"]
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
            myuser.contact_number = contact_number

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
    user = request.user
    if not user.id:
        return redirect('login')

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
                                mail=mail, uid=user.id, in_img=in_img, out_img=out_img)
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
        return render(request, "propertys.html", context)
    else:

        return render(request, "propertys.html")


# def propertys(request):
#     all_property = Property.objects.filter()
#     context = {'all_property': all_property}
#
#     return render(request, "propertys.html", context)


def base(request):
    return render(request, "base.html")


def my_property(request):
    user = request.user
    my_property = Property.objects.filter(uid=uid)
    context = {"my_property": my_property, "uid": user.id}
    return render(request, "my_property.html", context)


def del_property(request, Property_id):
    del_property = Property.objects.get(id=Property_id)
    del_property.delete()
    return redirect("my_property")


def profile(request):
    user = request.user
    context = {"user": user}
    return render(request, "profile.html", context)


def contactInfoMail(request, pid):
    user = request.user
    pid = int(pid)
    product = Property.objects.get(id=pid)
    context = {"product": product}
    send_mail("Property you request", "body", "team.rentaport@gmail.com",
              [user.email], fail_silently=True)
    return render(request, "contactInfoMailSent.html", context)


def rough(request, pid, abcd):
    print("ia : ", pid)
    pid = int(pid)
    product = Property.objects.get(id=pid)
    context = {"product": product, "rent": request.get_full_path()}
    return render(request, "Rough.html", context)
    # return HttpResponseRedirect("/propertys")


def profile_update(request):
    user = request.user
    uid = user.id
    if request.method == "POST":

        fname = request.POST["fname"]
        lname = request.POST["lname"]
        username = request.POST["username"]
        if (user.first_name == fname) and (user.last_name == lname) and (user.username == username):
            messages.error(request, "Nothing changed")
        elif User.objects.filter(username=username):
            messages.error(request, "This username is taken")
        else:
            User.objects.filter(id=uid).update(first_name=fname, last_name=lname, username=username)
            messages.success(request, "Profile Updated successfully")
            user = request.user
            context = {"user": user}
            return render(request, "profile.html", context)
    user = request.user
    context = {"user": user}
    return render(request, "profile_update.html", context)
