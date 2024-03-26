# report/views.py
from django.shortcuts import render
from .utils import get_data_points, process_data

def report_view(request):
    # Retrieve data points using utility function
    data_points_df = get_data_points()
    
    # Process the data points
    processed_data_df = process_data(data_points_df)
    
    # Pass the processed data to the template
    return render(request, 'report/report.html', {'data': processed_data_df})

#views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def chart_view(request):
    return render(request, 'chart.html')

def index(request):
    data_points = [
        { "label": "apple",  "y": 10  },
        { "label": "orange", "y": 15  },
        { "label": "banana", "y": 25  },
        { "label": "mango",  "y": 30  },
        { "label": "grape",  "y": 28  }
    ]
    return render(request, 'index.html', { "data_points" : data_points }) 


from datetime import datetime
from report.models import DataPoint

# Create and save a DataPoint instance with a specific timestamp and value
data_point = DataPoint(timestamp=datetime(2024, 3, 27, 12, 30), value=42.0)
data_point.save()
