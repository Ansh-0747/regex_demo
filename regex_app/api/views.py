from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
import pandas as pd
import re
import io

class FileUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        file_obj = request.FILES['file']
        file_type = file_obj.name.split('.')[-1]
        pattern = request.data.get('pattern')
        replacement = request.data.get('replacement')
        column = request.data.get('column')

        if file_type in ['csv']:
            df = pd.read_csv(file_obj)
        elif file_type in ['xlsx', 'xls']:
            df = pd.read_excel(file_obj)
        else:
            return Response({'error': 'Unsupported file type'}, status=400)

        # Apply regex
        df[column] = df[column].astype(str).apply(lambda x: re.sub(pattern, replacement, x))

        output = io.StringIO()
        df.to_csv(output, index=False)
        return Response({'data': output.getvalue()})
