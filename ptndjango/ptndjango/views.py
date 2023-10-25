from django.shortcuts import redirect

def Home(request):
    return redirect('posts_home_url')