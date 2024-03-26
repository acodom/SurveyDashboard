from django.test import TestCase

# Create your tests here.
# Import necessary modules for testing
from django.urls import reverse
from .utils import get_data_points, process_data

class ReportViewTests(TestCase):
    def test_report_view_data(self):
        data_points_df = get_data_points()
        print(data_points_df.info())  # Print DataFrame structure

    def test_report_view_status_code(self):
        # Get the URL for the report view
        url = reverse('report')

        # Make a GET request to the report view
        response = self.client.get(url)

        # Check if the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_report_view_template(self):
        # Get the URL for the report view
        url = reverse('report')

        # Make a GET request to the report view
        response = self.client.get(url)

        # Check if the correct template is used
        self.assertTemplateUsed(response, 'report/report.html')

    def test_report_view_data(self):
        # Retrieve data points using utility function
        data_points_df = get_data_points()
    
        # Process the data points
        processed_data_df = process_data(data_points_df)

        # Get the URL for the report view
        url = reverse('report')

        # Make a GET request to the report view
        response = self.client.get(url)

        # Check if the processed data is passed to the template
        self.assertEqual(response.context['data'].to_dict(), processed_data_df.to_dict())
