import io
import pandas as pd
from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from reportlab.pdfgen import canvas
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny

# We'll store the last processed data in memory for the PDF 
LAST_ANALYSIS = {}

@method_decorator(csrf_exempt, name='dispatch')
class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)
    permission_classes = [AllowAny]  # Allows React to upload without login issues

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES.get('file')
        
        if not file_obj:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            df = pd.read_csv(file_obj)
            
            summary = {
                "total_rows": len(df),
                "mean_flowrate": float(df['Flowrate'].mean()),
                "mean_pressure": float(df['Pressure'].mean()),
                "mean_temperature": float(df['Temperature'].mean()),
            }
            
            distribution = df['Type'].value_counts().to_dict()
            data_json = df.to_dict(orient='records')

            # Save for PDF export
            global LAST_ANALYSIS
            LAST_ANALYSIS = {"summary": summary, "distribution": distribution}

            return Response({
                "summary": summary,
                "distribution": distribution,
                "data": data_json
            }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class DownloadPDFView(APIView):
    permission_classes = [AllowAny] # Set to IsAuthenticated if you want security back later

    def get(self, request):
        global LAST_ANALYSIS
        if not LAST_ANALYSIS:
            return Response({"error": "No data to export"}, status=400)

        buffer = io.BytesIO()
        p = canvas.Canvas(buffer)
        
        p.setFont("Helvetica-Bold", 16)
        p.drawString(100, 800, "Chemical Equipment Summary Report")
        
        p.setFont("Helvetica", 12)
        p.drawString(100, 770, f"Total Equipment Count: {LAST_ANALYSIS['summary']['total_rows']}")
        p.drawString(100, 750, f"Average Flowrate: {LAST_ANALYSIS['summary']['mean_flowrate']:.2f}")
        p.drawString(100, 730, f"Average Pressure: {LAST_ANALYSIS['summary']['mean_pressure']:.2f}")
        
        p.drawString(100, 700, "Equipment Distribution:")
        y = 680
        for eq_type, count in LAST_ANALYSIS['distribution'].items():
            p.drawString(120, y, f"- {eq_type}: {count}")
            y -= 20

        p.showPage()
        p.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='Equipment_Report.pdf')