from django.shortcuts import redirect, render

def firstlogin(request):
    return render(request,"login.html")

def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")
# def loginpost(request):
#     u = request.POST['uname']
#     p = request.POST['pass']
#     obj =login.objects.filter(username =u,password = p)
 
def register(request):
    return render(request,"registerindex.html")

def  catalogue_seeing(request):
    return render(request, "CATALOGUE SEEING.HTML")

def address(request):
    return render(request,"contact.html")

def harmonyindex(request):
    return render(request,"harmonyindex.html")

def login_copy(request):
    return render(request,"logincopy.html")

def register_index_copy(request):
    return render(request,"registerindex copy.html")

def catalogue_seeing_copy(request):
    return render(request,"CATALOGUESEEINGcopy.HTML")

def catalogue_add(request):
    return render(request,"CATALOGUE.HTML")
