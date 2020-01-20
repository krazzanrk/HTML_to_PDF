
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML, CSS


def weasyprint_pdf_view(request):
    html_string = render_to_string('invoice.html')
    response = HttpResponse(content_type='application/pdf')
    html = HTML(string=html_string,base_url=request.build_absolute_uri())
    html.write_pdf(response, stylesheets=[CSS(settings.STATIC_ROOT + '/css/pdf.css'),CSS(string='body { font-family: serif !important }'),])
    return response