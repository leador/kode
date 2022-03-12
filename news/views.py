from django.shortcuts import render
from django.views.generic import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from .models import News, Category


def news_list(request):
    news = News.objects.filter(published=True).select_related('category').order_by('-id')[1:]
    last_new = News.objects.filter(published=True).order_by('-id')[0]
    paginator = Paginator(news, 6)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse('')
        news = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,
                      'news/list_ajax.html',
                      {'section': 'home',
                       'news': news})
    return render(request,
                  'news/news_list.html',
                  {'section': 'home',
                   'last_new': last_new,
                   'news': news})


def news_by_category(request, category_slug):
    news = News.objects.filter(category__slug=category_slug,
                               published=True).select_related('category').order_by('-id')[1:]
    last_new = News.objects.filter(category__slug=category_slug, published=True).order_by('-id')[0]
    paginator = Paginator(news, 6)
    page = request.GET.get('page')
    title = Category.objects.get(slug=category_slug)
    count = News.objects.filter(category__slug=category_slug, published=True).count()
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse('')
        news = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,
                      'news/list_ajax.html',
                      {'section': 'category',
                       'news': news, 'title': title,
                       'count': count})
    return render(request,
                  'news/news_category.html',
                  {'section': 'category',
                   'last_new': last_new,
                   'news': news, 'title': title,
                   'count': count})


class ViewNews(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news_item'
    slug_url_kwarg = 'news_slug'
    extra_context = {
        'section': 'view_news',
    }
