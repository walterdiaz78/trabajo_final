from django.views.generic import TemplateView

class IndexPage(TemplateView):
    template_name = 'index.html'

class ShopPage(TemplateView):
    template_name = 'product.html'

class ContactoPage(TemplateView):
    template_name = 'contact.html'

class InfoPage(TemplateView):
    template_name = 'about.html'

class MayoristaPage(TemplateView):
    template_name = 'mayorista.html'