
import google.auth
from googleapiclient.discovery import build

# Set up API credentials (replace with your own)
credentials, project = google.auth.default()

# Create a Google Sheets API service client
api_service_name = 'sheets'
api_version = 'v4'
sheets_api = build(api_service_name, api_version, credentials=credentials)

def get_google_sheets_data(spreadsheet_id, range_name):
    # Send request to the Google Sheets API
    request = sheets_api.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name)

    try:
        # Execute the request
        response = request.execute()

        # Process the received data
        data = process_sheets_data(response)
        return data

    except Exception as e:
        print(f"Error executing request: {e}")
        return None

def process_sheets_data(raw_data):
    # Process the received data as needed
    # Example: Extract values from the response
    values = raw_data.get('values', [])
    processed_data = [row for row in values]
    return processed_data

# Example Usage:
spreadsheet_id = 'your_spreadsheet_id'
range_name = 'Sheet1!A1:B10'  # Replace with the actual range in your spreadsheet
google_sheets_data = get_google_sheets_data(spreadsheet_id, range_name)

if google_sheets_data:
    print(google_sheets_data)
else:
    print("Error fetching Google Sheets data.")
