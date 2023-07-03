from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from colors.models import ColorBox


# Create your views here.
class ColorView(ListView):
    template_name = "base.html"
    queryset = ColorBox.objects.order_by("user_id", "id")

    def get_queryset(self):
        qs = super().get_queryset()
        object_list = {}
        for cb in qs:
            if cb.user_id in object_list:
                object_list[cb.user_id].append(cb)
            else:
                object_list[cb.user_id] = [cb, ]

        return object_list


