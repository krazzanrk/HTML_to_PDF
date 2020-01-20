from django.urls import path
from .views import *

app_name = "weasyprint_html_to_pdf"

urlpatterns = [

    path('', weasyprint_pdf_view, name='weasyprint')
    ,
]
