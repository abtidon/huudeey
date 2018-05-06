from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
import datetime

# Create your views here.


from .models import Prodsale

def index(request):
    """
      View function for home page of site
    """

    # Generate counts of the main objects

    num_sales=Prodsale.objects.all().count()

    # Render the HTML template index.html with the data in the context variable

    return render(
         request, 'index.html',
         context={'num_sales':num_sales},
    )


from django.views import generic

class ProdsaleListView(generic.ListView):
      model = Prodsale
      def get_queryset(self):
          return  Prodsale.objects.filter(prodname__icontains='BELT')



from django.shortcuts import render
from django.http import HttpResponseRedirect

<<<<<<< HEAD
from .forms import saledateform, searchdateform,searchcostform
=======
from .forms import saledateform, searchdateform
>>>>>>> 216a4bb38ccbaad1f656463f8a37f6a95f916389

def prodsale(request):
    #model = Prodsale
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = saledateform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            content = form.cleaned_data[ 'prodname' ]
          
            # redirect to a new URL:
            return redirect('results', content_all=content)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = saledateform()

    return render(request, 'saledate.html', {'form': form})

def results(request,content_all):
    content = Prodsale.objects.filter(prodname__icontains=content_all)
    return render(request, 'results.html' , {'content':content} )


def searchdatesale(request):
    #model = Prodsale
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = searchdateform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
<<<<<<< HEAD
            sdate = form.cleaned_data[ 'fdate' ]
            endate = form.cleaned_data[ 'edate' ]
=======
            sdate = form.cleaned_data[ 'saledate' ]
>>>>>>> 216a4bb38ccbaad1f656463f8a37f6a95f916389
            print (sdate)
            #print sdate.value() 
            #t_result = Prodsale.objects.filter(saledate__gte=sdate)
            # redirect to a new URL:
<<<<<<< HEAD
            return redirect('searchdresults', b_result=sdate,e_result=endate)
            #return redirect('searchdresults', b_result=sdate, t_result=edate)
=======
            return redirect('searchdresults', b_result=sdate)
>>>>>>> 216a4bb38ccbaad1f656463f8a37f6a95f916389
            #return render(request, 'searchdateform.html', {'form': form, 't_result':t_result})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = searchdateform()

    return render(request, 'searchdateform.html', {'form': form})




<<<<<<< HEAD
def searchdresults(request,b_result,e_result):
    content = Prodsale.objects.filter(saledate__gte=b_result, saledate__lte=e_result).order_by('saledate')
   #content = Prodsale.objects.filter(saledate__lte=b_result)
=======
def searchdresults(request,b_result):
    content = Prodsale.objects.filter(saledate__lte=b_result)
>>>>>>> 216a4bb38ccbaad1f656463f8a37f6a95f916389
    #for i in b_result :
    #    print( i.prodname )
    return render(request, 'results.html' , {'content':content} )




from django.db.models import Q

def searchcost(request):
    #model = Prodsale
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
<<<<<<< HEAD
        form = searchcostform(request.POST)
=======
        form = searchdateform(request.POST)
>>>>>>> 216a4bb38ccbaad1f656463f8a37f6a95f916389
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            scost = form.cleaned_data[ 'unitcost' ]
            print (scost)
            #print sdate.value() 
            #t_result = Prodsale.objects.filter(saledate__gte=sdate)
            # redirect to a new URL:
            return redirect('costresults', b_result=scost)
            #return render(request, 'searchdateform.html', {'form': form, 't_result':t_result})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = searchcostform()

    return render(request, 'searchcostform.html', {'form': form})




def costresults(request,b_result):
<<<<<<< HEAD
    content = Prodsale.objects.filter(unitcost__gte=b_result).order_by('unitcost')
    #content =Q(Prodsale__unitcost_lte=b_result)
=======
    #content = Prodsale.objects.filter(saledate__lte=b_result)
    content =Q(Prodsale__unitcost_lte=40000)
>>>>>>> 216a4bb38ccbaad1f656463f8a37f6a95f916389
    return render(request, 'results.html' , {'content':content} )
