from .models import Page 

# Procesador de contexto
def ctx_dict(request):
    pages = Page.objects.all()
    ctx = {'pages': pages}
    return ctx
