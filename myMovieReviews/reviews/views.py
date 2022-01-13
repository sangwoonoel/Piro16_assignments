from http.client import REQUEST_URI_TOO_LONG
from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm


def review_list(request):
    reviews = Review.objects.all()
    ctx = {'reviews' : reviews}

    return render(request, template_name = 'list.html', context = ctx)

def review_detail(request, pk):
    review = Review.objects.get(id=pk)
    ctx = {'review' : review}

    return render(request, template_name='detail.html', context= ctx)


def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()  # 이 부분 약간 헷갈려
            return redirect('reviews:list')
  
    else :
        form = ReviewForm()
        ctx = {'form' : form}

        return render(request, template_name='review_form.html', context=ctx)

def review_update(request, pk):
    review = get_object_or_404(Review, id=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance = review)
        if form.is_valid():
            review = form.save()  # 이 부분 약간 헷갈려
            return redirect('reviews:detail', pk)
  
    else :
        form = ReviewForm(instance=review)
        ctx = {'form' : form}

        return render(request, template_name='review_form.html', context=ctx)

def review_delete(request, pk):
    review = get_object_or_404(Review, id=pk)
    review.delete()
    return redirect('reviews:list')




        