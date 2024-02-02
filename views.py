from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import contact,product
from .forms import contactform,productform
from django.views.generic import ListView

# Create your views here.
def home(request):
    products=product.objects.all()
    product_count=products.count()
    context={'product_count':product_count}
    return render(request,'home.html',context)
    # template=loader.get_template('home.html')
    # return HttpResponse(template.render())

def client(request):
    template=loader.get_template('clients.html')
    return HttpResponse(template.render())

def vertical(request):
       
    template=loader.get_template('verticals.html')
    return HttpResponse(template.render(),{'recordcount':recordcount})

def about(request):
    template=loader.get_template('about.html')
    return HttpResponse(template.render())   

def contactus(request):
    if request.method=='POST':
        contactobj=contactform(request.POST)
        contactobj.save()
        return render (request,'home.html')
    else:
        contactobj=contactform()
        return render(request,'contact.html',{'form':contactobj})    

class service(ListView):
    model=product
    template_name='product.html'
    context_object_name='prodobj'
