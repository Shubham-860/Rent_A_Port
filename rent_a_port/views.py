import uuid

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from rent_a_port.models import ContactForm, NewsLetter, Appointment
from rent_a_port.models import Site as Property
from datetime import datetime
from django.core.mail import send_mail
from django.template.loader import render_to_string


# from django.contrib.auth import get_user_model

# Create your views here.

def index(request):
    # user = request.user
    # print(f"Hostname: {request.get_host()}/index")
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
        # Property
        Description = request.POST.get('Description')
        address = request.POST.get('Address')

        # General information
        rent = request.POST.get("Rent")
        deposit = request.POST["Deposit"]
        Maintenance = request.POST["Maintenance"]
        BHK = request.POST["BHK"]
        Floor = request.POST["Floor"]
        Pet = request.POST["Pet"]
        Parking = request.POST["Parking"]
        Type = request.POST["Type"]
        Posted_by = request.POST["Posted_by"]
        Agreement_duration = request.POST["Agreement_duration"]
        Available_from = request.POST["Available_from"]
        Electricity_water = request.POST["Electricity_water"]

        # Contact details
        phone = request.POST["Phone"]
        mail = request.POST["email"]
        in_img = request.FILES["in_img"]
        out_img = request.FILES["out_img"]

        add_property = Property(
            address=address, Message=Description, rent=rent, deposit=deposit, maintenance=Maintenance, BHK=BHK,
            Floor_number=Floor, Pet_allowed=Pet, Parking=Parking, Property_type=Type, Posted_by=Posted_by,
            Agreement_duration=Agreement_duration, Available_from=Available_from, Electricity_water=Electricity_water,
            phone=phone, mail=mail, uid=user.id, in_img=in_img, out_img=out_img)
        add_property.save()
        messages.success(request, "Property Added  successfully")
        print("saved")
        return render(request, "property/add-property.html")

    return render(request, "property/add-property.html")


def propertys(request):
    print('hello')
    if request.method == "POST":

        searched = request.POST["search"]
        print(searched)
        serched_property = Property.objects.filter(address__contains=searched)

        print(serched_property)
        context = {'serched_property': serched_property, 'searched': searched}
        return render(request, "property/propertys.html", context)
    else:

        return render(request, "property/propertys.html")


# def propertys(request):
#     all_property = Property.objects.filter()
#     context = {'all_property': all_property}
#
#     return render(request, "propertys.html", context)


def base(request):
    return render(request, "base/base.html")


def my_property(request):
    user = request.user
    my_property = Property.objects.filter(uid=user.id)
    context = {"my_property": my_property, "uid": user.id}
    return render(request, "property/my_property.html", context)


def del_property(request, Property_id):
    del_property = Property.objects.get(id=Property_id)
    del_property.delete()
    messages.warning(request, "Profile Updated successfully")
    return HttpResponseRedirect("/my_property")


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
    return render(request, "Temp/contactInfoMailSent.html", context)


def rough(request, pid, abcd):
    print("ia : ", pid)
    pid = int(pid)
    product = Property.objects.get(id=pid)
    context = {"product": product, "rent": request.get_full_path()}
    return render(request, "Temp/Rough.html", context)
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


def site(request, pid):
    user = request.user
    log_in = False
    if user.is_authenticated:
        log_in = True
    pid = int(pid)
    product = Property.objects.get(id=pid)

    context = {"p": product, "rent": request.get_full_path(), "log_in": log_in}
    return render(request, "property/property.html", context)


def edit_property(request, pid):
    pid = int(pid)
    product = Property.objects.get(id=pid)
    context = {"p": product, "path": request.get_full_path()}
    user = request.user
    if request.method == "POST":
        # Property
        Description = request.POST.get('Description')
        address = request.POST.get('Address')

        # General information
        rent = request.POST.get("Rent")
        deposit = request.POST["Deposit"]
        Maintenance = request.POST["Maintenance"]
        BHK = request.POST["BHK"]
        Floor = request.POST["Floor"]
        Pet = request.POST["Pet"]
        Parking = request.POST["Parking"]
        Type = request.POST["Type"]
        Posted_by = request.POST["Posted_by"]
        Agreement_duration = request.POST["Agreement_duration"]
        Available_from = request.POST["Available_from"]
        Electricity_water = request.POST["Electricity_water"]

        # Contact details
        phone = request.POST["Phone"]
        mail = request.POST["email"]
        in_img = request.FILES["in_img"]
        out_img = request.FILES["out_img"]

        Property.objects.filter(id=pid).update(
            address=address, Message=Description, rent=rent, deposit=deposit, maintenance=Maintenance, BHK=BHK,
            Floor_number=Floor, Pet_allowed=Pet, Parking=Parking, Property_type=Type, Posted_by=Posted_by,
            Agreement_duration=Agreement_duration, Available_from=Available_from, Electricity_water=Electricity_water,
            phone=phone, mail=mail, uid=user.id, in_img=in_img, out_img=out_img)

        messages.success(request, "Property Updated successfully")
        print("saved")
        return render(request, "property/my_property.html")

    return HttpResponseRedirect("/my_property")


def appointment(request, pid):
    user = request.user
    if request.method == "POST":
        product = Property.objects.get(id=pid)
        owner = User.objects.get(id=product.uid)

        owner_id = product.uid
        appointment_date_time = request.POST["date_time"]
        message = request.POST["message"]
        user_id = user.id
        pid = pid
        uid = uuid.uuid1()

        appointment_save = Appointment(owner_id=owner.id, appointment_date_time=appointment_date_time, message=message,
                                       user_id=user_id, property_id=pid, uuid=uid, appointment_set=False)
        appointment_save.save()
        print("appointment saved successfully!")

        # print(f"owner_id: {owner_id},appointment_date_time: {appointment_date_time},message: {message},user_id:{user_id},product:{product} and uid : {uid} ,owner : {owner}")
        # mail to ownee
        body = f'''
Regards, {owner.first_name},

wants to schedule a meeting at {appointment_date_time}.

message: {message}

To confirm, go to the following link: 

http://127.0.0.1:8000/confirm_appointment/{uid}/

OR

For further conversation, you can also email the Customer.

E-Mail : {user.email}

Team Rent A Port
        '''
        send_mail("Schedule a meeting", body, "team.rentaport@gmail.com",
                  [owner.email], fail_silently=False)
    return render(request, "appointment/appointment_mail_sent.html")


def confirm_appointment(request, uid):
    meeting = Appointment.objects.get(uuid=uid)
    if not meeting.appointment_set:
        owner = User.objects.get(id=int(meeting.owner_id))
        user = User.objects.get(id=int(meeting.user_id))

        Appointment.objects.filter(uuid=uid).update(appointment_set=True)
        body = f'''
Dear {user.first_name}
    
On {meeting.appointment_date_time}, has been confirmed by {owner.first_name} as the meeting time.
    
You may also email the owner for more discussion.
    
E-Mail : {owner.email}
    
Group Rent A Port
                '''
        send_mail("Meeting confirmed", body, "team.rentaport@gmail.com",
                  [user.email], fail_silently=False)
    content = {"already_set": meeting.appointment_set}
    return render(request, "appointment/confirm appointment.html",content)
