from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
import pandas as pd
from .serializers import FileUploadSerializer

class ProcessCSVView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileUploadSerializer(data=request.data)
        
        if file_serializer.is_valid():
            file_instance = file_serializer.save()
            
            try:
                # Read CSV
                df = pd.read_csv(file_instance.file.path)
                
                # --- REQUIREMENT: Data Summary ---
                summary = {
                    "total_rows": int(len(df)),
                    "mean_flowrate": float(df['Flowrate'].mean()) if 'Flowrate' in df else 0,
                    "mean_pressure": float(df['Pressure'].mean()) if 'Pressure' in df else 0,
                    "mean_temp": float(df['Temperature'].mean()) if 'Temperature' in df else 0,
                }
                
                # --- REQUIREMENT: Equipment Type Distribution ---
                # Example: {"Pump": 10, "Valve": 5}
                type_dist = df['Type'].value_counts().to_dict() if 'Type' in df else {}

                return Response({
                    "message": "File processed successfully",
                    "summary": summary,
                    "distribution": type_dist,
                    "data": df.head(50).to_dict(orient='records') # Return first 50 rows for display
                }, status=status.HTTP_201_CREATED)
                
            except Exception as e:
                return Response({"error": f"Error processing CSV: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)