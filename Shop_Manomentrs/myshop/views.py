from django.http import request
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import TemplateView
from .models import Category, Product
from django.views.generic import View, ListView

class Shop(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class CategoryProducts(ListView):
    model = Product

    template_name = 'category_products.html'
    context_object_name = 'products'

    def get_queryset(self,category_slug=None):
        category_slug = self.kwargs['slug']
        category = get_object_or_404(Category, slug=category_slug)
        return Product.objects.filter(category=category)

