from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from datetime import datetime

from ratings.models import Reviews, Routes

def index(request):
    latest_reviews_list = Reviews.objects.order_by('-id')[:5]
    context = {'latest_reviews_list': latest_reviews_list}
    return render(request, 'ratings/index.html', context)

#def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/detail.html', {'question': question})

def base(request):
    return render(request, 'ratings/base.html')

def about_us(request):
    return render(request, 'ratings/about-us.html')

def rate_form(request):
    routes_list = Routes.objects.order_by('id')
    blah = {'routes_list': routes_list}    
    return render(request, 'ratings/rate_matatu_form.html', blah)

def rate(request):
	b = Reviews(route_shot_name=request.POST['route_shot_name'], id_user='2', plate_number=request.POST['plate_number'], rating=request.POST['Rating'], comments=request.POST['comments'], date=datetime.now(), comment_number='2', comment_title=request.POST['comment_title'], username='sloan.holzman')
	b.save()
	return HttpResponseRedirect(reverse('ratings:index'))