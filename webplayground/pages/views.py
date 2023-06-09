from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Page
from .forms import PageForm

class StaffRequiredMixin(object):
    """
    Este mixin requerira que el usuario se miembro de staff
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
# List view auto-queries passed model to template
class PageListView(ListView):

    model = Page

# Detail view queries model from pk on url
class PageDetailView(DetailView):

    model = Page

# Class view para agregar 
class PageCreate(StaffRequiredMixin, CreateView):

    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

# Class view para actualizar
class PageUpdate(StaffRequiredMixin, UpdateView):

    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('pages:pages')

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

class PageDelete(StaffRequiredMixin, DeleteView):

    model = Page
    success_url = reverse_lazy('pages:pages')
