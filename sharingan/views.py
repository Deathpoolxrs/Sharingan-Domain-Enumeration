from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def result(request):
    if request.method == "POST":
        url = request.POST.get("domain")
        param ={'domainname':url}
        subdomain(url)
        return render(request,'result.html',param)
    else:
        return render(request,'index.html')
    
    
    
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def errorpage(request):
    return render(request,'Error.html')


def subdomain(url):
    return print(url)
    