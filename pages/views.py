from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy

class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

class PageCreate(CreateView):
    model = Page
    fields=[
        'title',
        'content',
        'order'
    ]
    success_url = reverse_lazy('pages:pages')
    # def get_success_url(self):
    #     return reverse('pages:pages')
# Create your views here.
# def pages(request):
#     pages = get_list_or_404(Page)
#     return render(request, 'pages/pages.html', {'pages':pages})

# def page(request, page_id, page_slug):
#     page = get_object_or_404(Page, id=page_id)
#     return render(request, 'pages/page.html', {'page':page})