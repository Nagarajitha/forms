from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *


#inserting data with FE  thorugh Forms
def insert_topic(request):

    # if POST method is activated with data -->do 
    if request.method == 'POST':

        tn = request.POST['tn'] #get value of key with key name from dictionary  -->request.POST in form of dictionary
        TO= Topic.objects.get_or_create(topic_name = tn)[0] #as get_or_create returns tuple we want only object at 0 th index postion we perform indexing

        TO.save()
        return HttpResponse('Topic is inserted successfully!!!')

    return render(request,'insert_topic.html')

def insert_webpage(request):
    if request.method =='POST':
        tn = request.POST['tn']
        na = request.POST.get('na')
        url = request.POST['url']
        email = request.POST['email']
        #returned topic object
        RTO = Topic.objects.get(topic_name = tn)
        WO = Webpage.objects.get_or_create(topic_name =RTO ,name =na, url=url , email=email)[0]
        WO.save()
        return HttpResponse('Webpage created successfully!!!')
    return render(request,'insert_webpage.html')

def insert_access(request):
    # na = RE
    # # Check if the Webpage exists
    # WO = Webpage.objects.filter(name=name)
    
    # if WO:
    #     # If Webpage exists, use the first one found
    #     wp = WO[0]
        
    #     date = input('Enter date: ')
    #     author = input('Enter  author: ')
        
    #     # Create AccessRecord using get_or_create
    #     ARO = AccessRecord.objects.get_or_create(name = wp, date=date, author=author)[0]
    #     ARO.save()
    #     d={'QLAO':AccessRecord.objects.all()}
    if request.method == 'POST':
        na = request.POST['na']
        date = request.POST['date']
        author = request.POST['author']
        
        RWO = Webpage.objects.get(name =na)
        AO = AccessRecord.objects.get_or_create(name =RWO , date=date, author=author)[0]
        AO.save()
        return HttpResponse('Access Record crearted successfully')
    return render(request,'insert_access.html')
   