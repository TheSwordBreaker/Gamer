from django.shortcuts import render

# Create your views here.
def review(request):
    context = {
        'data' : rating.objects.all(),
    }
    return render(request,'review.html',context)