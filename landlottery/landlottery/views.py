from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as mylogin
from land.models import Room
from booking.models import Book
from contact.models import Contact
from service.models import Service
import pgeocode
  



def index(request):
    s=Service.objects.all()
    r = Room.objects.all()
    # return HttpResponse('Hello')
    return render(request, 'index.html', {'r':r, 's':s})

def about(request):
    # return HttpResponse('Hello')
    return render(request, 'about.html')

def service(request):
    # return HttpResponse('Hello')
    s=Service.objects.all()
    return render(request, 'service.html', {'s':s})

def show_service(request):
    # return HttpResponse('Hello')
    if request.method=='POST':
        pk=request.POST.get('pk')
        s=Service.objects.get(pk=pk)
        return render(request, 'show_service.html', {'s':s})    

def contact(request):
    # return HttpResponse('Hello')
    return render(request, 'contact.html')

def handle_contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        msg=request.POST.get('msg')
        c= Contact(name=name, email=email, subject=subject, message=msg)
        c.save()
        return redirect('contact')    

def all_flats(request):
    r = Room.objects.all()
    # return HttpResponse('Hello')
    return render(request, 'all_flats.html', {'r':r})    

def detail(request):
    if request.method=="POST":
        pk=request.POST.get('pk')
        r=Room.objects.get(pk=pk)
        eir=r.eircode
        nomi=pgeocode.Nominatim('ie')
        lat=nomi.query_postal_code(eir).latitude
        long=nomi.query_postal_code(eir).longitude
    # return HttpResponse('Hello')
        return render(request, 'detail.html', {'r':r, 'lat':lat, 'long':long})

def location(request):
    return render(request, 'location.html')        

# def index(request):
#     # return HttpResponse('Hello')
#     return render(request, 'index.html')

# def index(request):
#     # return HttpResponse('Hello')
#     return render(request, 'index.html')                    

def login(request):
    return render(request, "seller/login.html") 

def signup(request):
    return render(request, "seller/register.html")

def error(request):
    return render(request, 'seller/404.html')    

def handle_signup(request):
    if request.method=='POST':
        f_name = request.POST.get('fname')
        l_name = request.POST.get('lname')
        # l_name = request.POST.get('l_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        # r_username = request.POST.get('r_username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1!=pass2:
            e='Passwords are not matched'
            return render(request, 'seller/404.html', {'e':e})

        if len(f_name)<3:
            e='First name Should Be Greater Than 2 Characters'
            return render(request, 'seller/404.html', {'e':e})

        if len(l_name)<3:
            e='Last name Should Be Greater Than 2 Characters'
            return render(request, 'seller/404.html', {'e':e})    

        if len(username)<5:
            e='Username Should Be Greater Than 4 Characters'
            return render(request, 'seller/404.html', {'e':e})

        if len(pass1)<8:
            e='Password Should Be Greater Than 7 Characters'
            return render(request, 'seller/404.html', {'e':e})    

        user_confirm =  User.objects.all()
        for user in user_confirm:
            if username == user.get_username():
                return redirect('contact')
                          

        user = User.objects.create_user(username ,email, pass1)
        user.first_name= f_name
        user.last_name= l_name 
        user.save()
    return redirect('home')    




def handle_login(request):
    if request.method=='POST':
        u_name = request.POST.get('username')
        password = request.POST.get('pass')
        
        myuser= authenticate(username=u_name, password=password)
        if myuser is not None:
            mylogin(request, myuser)
            # return render(request, 'seller/index.html')
            return redirect('seller_panel')
        else:
            e='Enter Valid Creditentials'
            return render(request, 'seller/404.html', {'e':e}) 
    
    else:
        return redirect('contact') 

def mylogout(request):
    logout(request)
    return redirect('home')

def seller_change_pass(request):
    return render(request, 'seller/change_pass.html')


def seller_panel(request):
    if request.user.is_authenticated:
        try:
            r=Book.objects.filter(user_id=request.user.pk)
            return render(request, "seller/index.html", {'r':r})
        except:         
            return render(request, "seller/index.html")
    else:
        return redirect('home')

def post_ad(request):
    if request.user.is_authenticated:
        # a=Activation.objects.get(user_id=request.user.pk)
        return render(request, "seller/post_ad.html")    
    else:
        return redirect('home')


def handle_post_ad(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            r_t = request.POST.get('r_t')
            street=request.POST.get('street')
            r_a = request.POST.get('r_a')
            eir=request.POST.get('eir')
            mobile = request.POST.get('mobile')
            image = request.FILES['image']
            rent = request.POST.get('rent')
            desc = request.POST.get('desc')
            if len(mobile)>10:
                e='Enter Correct Mobile Number'
                return render(request, 'seller/404.html', {'e':e})

            r= Room(user_id=request.user.pk, room_type=r_t, street=street, room_address=r_a, eircode=eir, number=mobile, image=image, rent=rent, desc=desc)
            r.save()
            # myuser= authenticate(username=u_name, password=password)
            # if myuser is not None:
            #     mylogin(request, myuser)
            #     # return render(request, 'seller/index.html')
            #     return redirect('seller_panel')
            # else:
            return redirect('seller_panel')
        
        else:
            return redirect('contact')
        # a=Activation.objects.get(user_id=request.user.pk)
        # return render(request, "seller/post_ad.html")    
    else:
        return redirect('home')                


def my_ads(request):
    if request.user.is_authenticated:
        r = Room.objects.filter(user_id=request.user.pk)
        return render(request, "seller/my_ads.html", {'r':r})    
    else:
        return redirect('home')

def delete_ads(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            pk=request.POST.get('pk')
            r = Room.objects.get(pk=pk)
            r.delete()
            return redirect('my_ads')    
    else:
        return redirect('home')      

def edit_ads(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            pk=request.POST.get('pk')
            r = Room.objects.get(pk=pk)
            return render(request, "seller/edit_ads.html", {'r':r})    
    else:
        return redirect('home')

def handle_edit_ads(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            pk=request.POST.get('pk')
            r_t = request.POST.get('r_t')
            street=request.POST.get('street')
            r_a = request.POST.get('r_a')
            eir=request.POST.get('eir')
            mobile = request.POST.get('mobile')
            image = request.FILES['image']
            # print(image)
            rent = request.POST.get('rent')
            desc = request.POST.get('desc')
            if len(mobile)>10:
                e='Enter Correct Mobile Number'
                return render(request, 'seller/404.html', {'e':e})
            if image == "":
                r=Room.objects.get(pk=pk)
                r.room_type=r_t
                r.street=street
                r.room_address=r_a
                r.eircode=eir
                r.number=mobile
                r.image=r.image
                r.rent=rent
                r.desc=desc
                r.save()
            else:
                r=Room.objects.get(pk=pk)
                r.room_type=r_t
                r.street=street
                r.room_address=r_a
                r.eircode=eir
                r.number=mobile
                r.image=image
                r.rent=rent
                r.desc=desc
                r.save()
            # myuser= authenticate(username=u_name, password=password)
            # if myuser is not None:
            #     mylogin(request, myuser)
            #     # return render(request, 'seller/index.html')
            #     return redirect('seller_panel')
            # else:
            return redirect('seller_panel')
        
        else:
            return redirect('contact')
        # a=Activation.objects.get(user_id=request.user.pk)
        # return render(request, "seller/post_ad.html")    
    else:
        return redirect('home')


def handle_add_booking(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            # b = Book.objects.filter(user_id=request.user.pk)
            rpk=request.POST.get('rpk')
            fname=request.POST.get('fname')
            lname=request.POST.get('lname')
            email=request.POST.get('email')
            number=request.POST.get('number')
            country=request.POST.get('country')
            pob=request.POST.get('pob')
            noa=request.POST.get('noa')
            noc=request.POST.get('noc')
            sr=request.POST.get('sr')
            if len(number)>10:
                e='Enter Correct Mobile Number'
                return render(request, 'seller/404.html', {'e':e})
            u=Room.objects.get(pk=rpk)
            print(u.user_id)
            b=Book(booking_username=request.user.username, user_id=u.user_id, room_id=rpk, fname=fname, lname=lname, email=email, number=number, country=country, pob=pob, noa=noa, noc=noc, sr=sr)
            b.save()
            e='Order has been placed'
            return render(request, 'seller/404.html', {'e':e})     
        else:
            return redirect('home')
    else: 
        e='Please Login Before Ordering'
        return render(request, 'seller/404.html', {'e':e})        

def delete_booking(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            pk=request.POST.get('pk')
            b = Book.objects.get(pk=pk)
            b.delete()
            return redirect('seller_panel')    
    else:
        return redirect('home')      


def user_login(request):
    return render(request, 'user/login.html')


def user_panel(request):
    if request.user.is_authenticated:
        try:

            r=Book.objects.filter(booking_username=request.user.username)
            return render(request, "user/index.html", {'r':r})
        except:         
            return render(request, "user/index.html")
    else:
        return redirect('home')




def handle_user_login(request):
    if request.method=='POST':
        u_name = request.POST.get('username')
        password = request.POST.get('pass')
        
        myuser= authenticate(username=u_name, password=password)
        if myuser is not None:
            mylogin(request, myuser)
            # return render(request, 'seller/index.html')
            return redirect('user_panel')
        else:
            e='Enter Valid Creditentials'
            return render(request, 'user/404.html', {'e':e}) 
    
    else:
        return redirect('contact')


def delete_booking_user(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            pk=request.POST.get('pk')
            b = Book.objects.get(pk=pk)
            b.delete()
            return redirect('user_panel')    
    else:
        return redirect('home')        


def edit_booking_user(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            pk=request.POST.get('pk')
            b = Book.objects.get(pk=pk)
            return render(request, "user/edit_booking.html", {'b':b})    
    else:
        return redirect('home')


def handle_edit_booking(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            bpk=request.POST.get('pk')
            fname=request.POST.get('f_name')
            lname=request.POST.get('l_name')
            email=request.POST.get('email')
            number=request.POST.get('mobile')
            country=request.POST.get('country')
            pob=request.POST.get('pob')
            noa=request.POST.get('noa')
            noc=request.POST.get('noc')
            sr=request.POST.get('sr')
            # u=Book.objects.get(pk=bpk)
            # print(u.user_id)
            if len(number)>10:
                e='Enter Correct Mobile Number'
                return render(request, 'seller/404.html', {'e':e})
            
            r=Book.objects.get(pk=bpk)
            r.fname=fname
            r.lname=lname
            r.email=email
            r.number=number
            r.country=country
            r.pob=pob
            r.noa=noa
            r.noc=noc
            r.sr=sr
            r.save()
            
            # myuser= authenticate(username=u_name, password=password)
            # if myuser is not None:
            #     mylogin(request, myuser)
            #     # return render(request, 'seller/index.html')
            #     return redirect('seller_panel')
            # else:
            return redirect('user_panel')
        
        else:
            return redirect('contact')
        # a=Activation.objects.get(user_id=request.user.pk)
        # return render(request, "seller/post_ad.html")    
    else:
        return redirect('home')

def user_change_pass(request):
    return render(request, 'user/change_pass.html')        

def handle_change_pass(request):
    if request.method=='POST':
        u=User.objects.get(pk=request.user.pk)
        pass1=request.POST.get('pass')
        u.set_password(pass1)
        u.save()
        return redirect('home')
