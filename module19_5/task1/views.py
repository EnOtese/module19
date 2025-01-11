from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game, News


# Create your views here.

def platform(request):
    return render(request, 'fourth_task/platform.html')


def games(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    return render(request, 'fourth_task/cart.html')

users = Buyer.objects.all()

def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if Buyer.objects.filter(name=username).exists():
            info['error'] = 'Пользователь уже существует'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        else:
            Buyer.objects.create(name=username, age=int(age), balance=0)
            info['success'] = f'Приветствуем, {username}!'

    info['form'] = UserRegister()
    return render(request, 'fifth_task/registration_page.html', info)

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if username in users:
            info['error'] = 'Пользователь уже существует'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        else:
            info['success'] = f'Приветствуем, {username}!'

    info['form'] = UserRegister()
    return render(request, 'fifth_task/registration_page.html', info)

def news(request):
    news_list = News.objects.all().order_by('-date')
    paginator = Paginator(news_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'news': page_obj
    }
    return render(request, 'fifth_task/news.html', context)