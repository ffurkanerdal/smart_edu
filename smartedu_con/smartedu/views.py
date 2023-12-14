from django.views.generic import TemplateView
from pageDesign.models import *
from typing import Any


class BaseView(TemplateView):

    template_name   =   None

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =   super().get_context_data(**kwargs)
        contact =   SiteDetails.objects.filter
        

        context["navbars"]  =   PageNavbar.objects.all()
        context["footers"]  =   Footer.objects.all()
        context["logo"]     =   Logo.objects.first()
        context["socialMedia"]  =   SocialMedia.objects.all()
        context["phone"]    =   contact(name="phone").first()
        context["email"]    =   contact(name="gmail").first()
        context["adress"]   =   contact(name="adress").first()
        context["webSite"]  =   contact(name="web site").first()
        context["aboutUs"]  =   contact(name="About US").first()

        return context
