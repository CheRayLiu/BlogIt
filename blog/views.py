from django.shortcuts import render

posts = [
    {
      'author': 'Ray',
      'title':  'First Post!',
      'content': 'First one',
      'date_posted': 'August 27,2018'
    },
    {
      'author': 'Ray',
      'title':  'Second Post!',
      'content': 'Second one',
      'date_posted': 'August 28,2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request,"blog/home.html",context)

def about(request):
    return render(request,"blog/about.html",{'title': 'About'})