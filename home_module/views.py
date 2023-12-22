from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from site_module.models import SiteSetting, FooterLinkBox ,FooterLink, Slider


class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slider : Slider = Sliƒder.objects.filter(is_active=True)
        context['sliders'] = slider
        # context['data'] = 'this is data in home page'
        # context['description'] = 'این صفحه اصلی است'
        return context


def site_header_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': setting
    }
    return render(request, 'shared/site_header_partial.html', context)


def site_footer_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_boxes : FooterLinkBox = FooterLinkBox.objects.all() #.filter(is_active=True) میشه اینم گزاشت
    for item in footer_link_boxes:
        item.footerlink_set
    context = {
        'site_setting': setting,
        'footer_link_boxes': footer_link_boxes
    }
    return render(request, 'shared/site_footer_partial.html', context)


class AboutView(TemplateView):
    template_name = 'home_module/about_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_setting : SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = site_setting
        return context
