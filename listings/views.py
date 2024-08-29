from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import SavedSearch
from django.shortcuts import  redirect
from django.urls import reverse

def home(request):

    return redirect(reverse('saved-search-list'))

class SavedSearchListView(LoginRequiredMixin, ListView):
    model = SavedSearch
    template_name = 'saved_search_list.html'

    def get_queryset(self):
        return SavedSearch.objects.filter(user=self.request.user)

class SavedSearchCreateView(LoginRequiredMixin, CreateView):
    model = SavedSearch
    template_name = 'saved_search_form.html'
    fields = ['name', 'municipality', 'rent_amount', 'is_wheelchair_friendly']
    success_url = reverse_lazy('saved-search-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SavedSearchUpdateView(LoginRequiredMixin, UpdateView):
    model = SavedSearch
    template_name = 'saved_search_form.html'
    fields = ['name', 'municipality', 'rent_amount', 'is_wheelchair_friendly']
    success_url = reverse_lazy('saved-search-list')

    def get_queryset(self):
        return SavedSearch.objects.filter(user=self.request.user)



class SavedSearchDeleteView(LoginRequiredMixin, DeleteView):
    model = SavedSearch
    template_name = 'saved_search_confirm_delete.html'
    success_url = reverse_lazy('saved-search-list')

    def get_queryset(self):
        return SavedSearch.objects.filter(user=self.request.user)

class SavedSearchListView(ListView):
    model = SavedSearch
    template_name = 'listings/savedsearch_list.html'