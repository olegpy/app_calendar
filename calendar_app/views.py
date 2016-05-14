from django.shortcuts import render
from django.db.models import F, Count, Max, Q, Min


from agreements.models import Period


def index(request):
    return render(request, 'index.html')


def comments(request):
    # get request
    period = search(request.GET)
    # main dictionary
    dic_main = {years.year: [0] *
                12 for years in period.dates('end_date', 'year')}
    # set unique id objects
    list_id = set(period.values_list('choice__id', flat=True))

    set_objects = [period.filter(
        choice__id=i).order_by("-end_date")[0] for i in list_id]

    for i in set_objects:
        dic_main[i.end_date.year][i.end_date.month - 1] += 1

    return render(request, 'comments.html',
                  {'dic': dic_main})


def search(req):
    dic_s = {}
    company = req.get('company', '')
    country = req.get('country', '')
    negotiator = req.get('negotiator', '')
    l = lambda x: str(x).split(',')

    if company or country or negotiator:
        if company:
            dic_s['choice__company__in'] = l(company)

        if country:
            dic_s['choice__company__country__in'] = l(country)

        if negotiator:
            dic_s['choice__negotiator__in'] = l(negotiator)

        period = Period.objects.filter(**dic_s)
    else:
        period = Period.objects.all()

    return period
