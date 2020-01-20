from django.urls import path
from .views import *

app_name = "pdfkit_html_to_pdf"

urlpatterns = [

    path('', pdfkit_pdf_view, name='pdfkitview'),
]
