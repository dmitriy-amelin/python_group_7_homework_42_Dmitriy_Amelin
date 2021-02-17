from django.shortcuts import render


def index_view(request):

    if request.method == 'GET':
        return render(request, 'article_create.html')
    elif request.method == 'POST':
        context = {
            'fist_number': request.POST.get('fist_number'),
            'second_number': request.POST.get('second_number'),
            'button': request.POST.get('button'),
        }

        if context['button'] == 'add':
            context['result'] = int(context['fist_number']) + int(context['second_number'])
            context['symbol'] = '+'
        elif context['button'] == 'subtract':
            context['result'] = int(context['fist_number']) - int(context['second_number'])
            context['symbol'] = '-'
        elif context['button'] == 'multiply':
            context['result'] = int(context['fist_number']) * int(context['second_number'])
            context['symbol'] = '*'
        elif context['button'] == 'divide':
            context['result'] = int(context['fist_number']) / int(context['second_number'])
            context['symbol'] = '/'

        return render(request, 'index.html', context)