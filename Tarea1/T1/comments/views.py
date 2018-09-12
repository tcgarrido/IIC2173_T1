from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.template import loader
from .forms import CommentsForm
from .models import CreateComment

# Create your views here.
def home(request):
    comments_list = CreateComment.objects.order_by('-date')

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['Your_Comment']
            date = timezone.now()
            form = new(data,date, request.META.get('REMOTE_ADDR'))
    else:
        form = CommentsForm()

    template = loader.get_template('comments/home.html')
    context = {
        'comments_list': comments_list,
        'form': form
    }
    return redirect(template.render(context, request))


def new(content, date, ip):
    comment = CreateComment(content=content, date=date, server_IP=ip)
    comment.save()
    return CommentsForm()
