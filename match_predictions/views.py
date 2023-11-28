from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from matches.models import Match
from predictions.models import Prediction

def index(request):
    matches = Match.objects.all()[:15]
    prediction = Prediction.objects.all()[:15]
    data={
        'matches':matches,
        'predictions':prediction
    }
    return render(request,"index.html",data)


def viewMatches(request):
    matches = Match.objects.all()
    paginator = Paginator(matches, 20)
    page_number = request.GET.get('page')
    matches_final = paginator.get_page(page_number)
    totalPageNumber = matches_final.paginator.num_pages
    
 
    current_page = matches_final.number
    start_page = max(1, current_page - 2)
    end_page = min(totalPageNumber, current_page + 2) + 1  
    page_range = range(start_page, end_page)
    
    data = {
        'matches': matches_final,
        'lastpage': totalPageNumber,
        'totalPage': page_range,
    }
    return render(request, "matches.html", data)
