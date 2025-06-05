from django.shortcuts import render

# creating views here importing the HttpReponse from django.http and the render was imported from default


# a list of dictionary which represnets dummy data for populating the html
posts=[
    {
        'author':"aashutosh dahal",
        'title':"blog post",
        'content':"this is the first content published",
        'date_posted':"May 4, 2025"
    },
    {
        'author':"aashutosh dahal",
        'title':"blog post",
        'content':"this is the first content published",
        'date_posted':"May 4, 2025"
    },
    {
        'author':"aashutosh dahal",
        'title':"blog post",
        'content':"this is the first content published",
        'date_posted':"May 4, 2025"
    },
]

def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})