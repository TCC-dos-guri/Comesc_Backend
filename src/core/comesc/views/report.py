from weasyprint import HTML
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views import View
from core.comesc.models.batch import Batch
from core.comesc.models.roll import Roll
from core.comesc.serializer.roll import RollSerializer
from core.comesc.serializer.batch import BatchSerializer
from config.gemini_config import generate_report
import json 

class ReportView(View):
    def get(self, request, id):
        batch = Batch.objects.get(id=id)
        batch_rolls = Roll.objects.filter(batch=batch)
        batch_data = BatchSerializer(batch).data
        rolls_data = RollSerializer(batch_rolls, many=True).data

        final_data = {
            'batch': batch_data,
            'rolls': rolls_data
        }

        dados_como_string = json.dumps(final_data)

        print("\nIniciando a geração do relatório a partir do arquivo principal...")

        relatorio_html = generate_report(dados_como_string)

        pdf_file = HTML(string=relatorio_html).write_pdf()

        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'

        return response
    