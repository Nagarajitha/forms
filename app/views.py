from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *
from django.db.models.functions import Length



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
    QLTO = Topic.objects.all()
    d = {'QLTO':QLTO}

    if request.method =='POST':
        tn = request.POST['tn']
        na = request.POST['na']
        url = request.POST['url']
        email = request.POST['email']
        #returned topic object
        TO = Topic.objects.get(topic_name = tn)
        WO = Webpage.objects.get_or_create(topic_name =TO ,name =na, url=url , email=email)[0]
        WO.save()

        
        return HttpResponse('Webpage created successfully!!!')
    return render(request,'insert_webpage.html',d)

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

    QLWO = Webpage.objects.all()
    d = {'QLWO':QLWO}

    if request.method == 'POST':
        na = request.POST['na']
        date = request.POST['date']
        author = request.POST['author']
        #here id na holds id of the Access Record as it is PK for the Webpage
        RWO = Webpage.objects.get(id =na)
        AO = AccessRecord.objects.get_or_create(name =RWO , date=date, author=author)[0]
        AO.save()
        return HttpResponse('Access Record crearted successfully')
    return render(request,'insert_access.html',d)
   


   # retrieving , updating , deleting


def display_webpage(request):

    
    QLWO = Webpage.objects.all().order_by('topic_name')#orders topic_name colun accroding to ASCII values in ascending order
    QLWO = Webpage.objects.filter(topic_name='Cricket').order_by('topic_name') #filters all Cricket topics accroding to ASCII values in ascending order
    QLWO = Webpage.objects.filter(topic_name='Hockey').order_by('topic_name') # filters all hockey topics 
    QLWO = Webpage.objects.filter(topic_name ='Football').order_by('id')
    QLWO = Webpage.objects.order_by(Length('name'))#orders in asc order based on length  of name column
    QLWO = Webpage.objects.order_by(Length('url'))#orders in asc order based on length  of url column
    QLWO = Webpage.objects.order_by(Length('name').desc())#orders in desc order based on length  of name column
    
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(topic_name = 'Chess').order_by('name')
    d = {'QLWO':QLWO}

    return render(request,'display_webpage.html',d)


def display_access(request):

    QLAO=AccessRecord.objects.all()
    QLAO = AccessRecord.objects.all().order_by('date')#orders date column in ascending order
    QLAO = AccessRecord.objects.all().order_by('-author') # order in desc order based on author 
    QLAO=AccessRecord.objects.all()[::-1] #in reverse order using slicing on list
    QLAO=AccessRecord.objects.all()[3:5:] # get only 4,5
    QLAO=AccessRecord.objects.order_by(Length('name').desc())
    QLAO=AccessRecord.objects.filter(author='msd').order_by('id')
    #QLAO=AccessRecord.objects.filter(name='dhoni').order_by('name')
    QLAO = AccessRecord.objects.exclude(author='msd')


#LOOKups

    #for pattern searching we go for startswith,endswith,contains --> its not case sensitive

    #QLAO = AccessRecord.objects.filter(name__startswith = 'a')-->it is foreign key column we can't use lookupd coz its object
     # its like a pattern searching LIKE operator in sql
    QLAO = AccessRecord.objects.filter(author__startswith = 'r')
    QLAO = AccessRecord.objects.filter(author__endswith ='d')
    QLAO = AccessRecord.objects.filter(author__contains ='d')
    QLAO = AccessRecord.objects.all()
    #__year lookup
    QLAO = AccessRecord.objects.filter(date__year ='1999')

    #__month lookup
    QLAO = AccessRecord.objects.filter(date__month =9)
    #__day lookup
    QLAO = AccessRecord.objects.filter(date__day =17)

    #IN lookup
    QLAO = AccessRecord.objects.filter(author__in =('msd','virat'))

    #__gt lookup(greater than > )
    QLAO = AccessRecord.objects.filter(date__year__gt=1990)

    #__lt lookup(lessthan <)
    QLAO = AccessRecord.objects.filter(date__year__lt=1990)
    #__gte lookup(greater thanequalsto >= )
    QLAO = AccessRecord.objects.filter(date__year__gte=1990)
    #__lte lookup(lessthan equal to <=)
    QLAO = AccessRecord.objects.filter(date__year__lte=1990)

    #Foreign Key columns
    #QLAO = AccessRecord.objects.filter(name__startswith ='v')

    d={'QLAO':QLAO}
    return render(request,'display_access.html',d)


   


def update_webpage(request):
    Webpage.objects.filter(name='Virat').update(name='Virat Kohili')
    Webpage.objects.filter(name='Virat').update(name='msd')
    WPDO=Webpage.objects.all()
    d={'WPDO':WPDO}
    return render(request,'display_webpage.html',d)

def delete_access(request):
    
    ARDO=AccessRecord.objects.all()
    AccessRecord.objects.filter(author='virat').delete()
    d={'ARDO':ARDO}
    return render(request,'display_access.html',d)

  