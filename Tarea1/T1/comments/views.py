from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.template import loader
from .forms import CommentsForm
from .models import CreateComment

# Create your views here.
def home(request):
    comments_list = CreateComment.objects.order_by('-date')
    template = loader.get_template('comments/home.html')

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['Your_Comment']
            date = timezone.now()
            form = new(data,date)
    else:
        form = CommentsForm()

    context = {
        'comments_list': comments_list,
        'form': form
    }
    return HttpResponse(template.render(context, request))


def new(content, date):
    comment = CreateComment(content=content, date=date)
    comment.save()
    return CommentsForm()
