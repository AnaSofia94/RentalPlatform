from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import SavedSearch


class SavedSearchListView(LoginRequiredMixin, ListView):
    model = SavedSearch
    template_name = 'saved_search_list.html'

    def get_queryset(self):
        return SavedSearch.objects.filter(user=self.request.user)

class SavedSearchCreateView(LoginRequiredMixin, CreateView):
    model = SavedSearch
    template_name = 'saved_search_form.html'
    fields = ['name', 'municipality', 'rent_amount', 'is_wheelchair_friendly']  # Include all the fields you want the user to set
    success_url = reverse_lazy('saved-search-list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Automatically associate the saved search with the logged-in user
        return super().form_valid(form)

class SavedSearchUpdateView(LoginRequiredMixin, UpdateView):
    model = SavedSearch
    template_name = 'saved_search_form.html'
    fields = ['name', 'municipality', 'rent_amount', 'is_wheelchair_friendly']  # Include all the fields you want the user to update
    success_url = reverse_lazy('saved-search-list')

    def get_queryset(self):
        return SavedSearch.objects.filter(user=self.request.user)



class SavedSearchDeleteView(LoginRequiredMixin, DeleteView):
    model = SavedSearch
    template_name = 'saved_search_confirm_delete.html'
    success_url = reverse_lazy('saved-search-list')

    def get_queryset(self):
        return SavedSearch.objects.filter(user=self.request.user)  # Ensure users can only delete their own saved searches