import warnings
from concurrent.futures import ThreadPoolExecutor
from requests import Session
from django.shortcuts import render

warnings.filterwarnings('ignore', message='Unverified HTTPS request')

escapeurl=[] 
statuscode=[]

def index(request):
    return render(request,'index.html')

def result(request):
    del escapeurl[:]
    del statuscode[:]
    if request.method == "POST":
        file = request.FILES['domainfile'].read() # get the uploaded 
        escapechr(file)
        print(escapeurl)
        return render(request,'result.html',{'urls':escapeurl})
    else:
        return render(request,'index.html')
    
    
    
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def errorpage(request):
    return render(request,'Error.html')


def escapechr(file):
    with ThreadPoolExecutor(max_workers=100) as executor:
        splitfile=file.splitlines(True)
        for i in splitfile:
            decode=i.decode('utf-8') #decoding byte data from file example:b'google.com' we remove the the b'' 
            stripedurl = decode.rstrip() #this will strip the spcae
            url ="https://"+stripedurl
          # escapeurl.append(url)  #adding in list
            executor.submit(urlrequest,url)
    return

s = Session()
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
                         'AppleWebKit/537.36 (KHTML, like Gecko) '\
                         'Chrome/75.0.3770.80 Safari/537.36'}
s.headers.update(headers)

def urlrequest(url):
    r = s.head(url, verify=False ,timeout=3)
    code = r.status_code
    escapeurl.append(url)
    statuscode.append(code)
    return 
