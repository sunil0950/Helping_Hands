from django.shortcuts import render, redirect
from .models import Details as blood

# Create your views here.
def home1(req):
    return render(req, 'home.html')
def register1(req):
    if req.method=='POST':
        uid=req.POST.get('uid')
        name=req.POST.get('name')
        password=req.POST.get('password')
        cnfpassword=req.POST.get('cnfpassword')
        phoneno=(req.POST.get('phoneno'))
        gender=req.POST.get('gender')
        lang=req.POST.get('lang')
        state=req.POST.get('state')
        city=req.POST.get('city')
        group=req.POST.get('group')
        c=0
        l=0
        u=0
        d=0
        s=0
        for i in password:
            c+=1
            if i.isupper():
                u+=1
            elif i.islower():
                l+=1
            elif i.isdigit():
                d+=1
            else:
                s+=1
        if c>=8 or c<=16 and l>=1 and u>=1 and d>=1 and s>=1:
            r='valid'
        else:
            r='Invalid Password'
            return render(req,'register.html',{'r':r})
        if password != cnfpassword:
            return render(req,'register.html',{'res':'password and cnf password should be match'})
        if not phoneno.isdigit() or len(phoneno) != 10:
            return render(req,'register.html',{'res':'phone number should be 10 digits'})
        info=blood(uid=uid,name=name,password=password,cnfpassword=cnfpassword,phoneno=phoneno,gender=gender,lang=lang,state=state,city=city,group=group)
        info.save()
        return render(req,'register.html',{'res':'Registration Done'})
    return render(req,'register.html')
def login1(req):
    if req.method == 'POST':
        a = req.POST.get('name')
        b = req.POST.get('password')
        c = req.POST.get('select')

        try:
            user = blood.objects.get(name=a)
        except blood.DoesNotExist:
            return render(req, 'login.html', {'masg': 'User Not Found'})

        if user.password == b and c == 'user' and user.name == a:
            # Store UID in session
            req.session['uid'] = user.uid  # Store UID in session
            return render(req, 'User.html', {'name': user.name, 'uid': user.uid})
        elif user.password == b and c == 'admin' and a == 'sunil':
            return render(req, 'admin.html',{'name':user.name})
        else:
            return render(req, 'login.html', {'masg': 'User name and Password is incorrect'})
    return render(req, 'login.html')
def search(req):
    if req.method=='POST':
        a=req.POST.get('group')
        res=blood.objects.filter(group=a)
        if res.exists():
            return render(req,'search.html',{'s':res})
        else:
            return render(req,'search.html',{'res':'Blood group is not Avaliable'})
    return render(req,'search.html')
def editing(req):
    res=blood.objects.all()
    return render(req,'editing.html',{'user':res})
def Update(req, uid):
    user = blood.objects.get(uid=uid)
    if req.method == 'POST':
        user.name = req.POST.get('name')
        user.phoneno = req.POST.get('phoneno')
        user.state = req.POST.get('state')
        user.city = req.POST.get('city')
        user.group = req.POST.get('group')
        user.save()
        return redirect('editing')
    return render(req, 'update.html', {'user': user})
def logout(req):
    return render(req,'logout.html')
def details1(req):
    res=blood.objects.all()
    return render(req,'details.html',{'user':res})
def u_editing(req, uid):
    try:
        res = blood.objects.get(uid=uid)
    except blood.DoesNotExist:
        res = None
    return render(req, 'u_editing.html', {'i': res})
def User1(req):
    return render(req,'User.html')
