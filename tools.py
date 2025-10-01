import os
import requests
from dotenv import load_dotenv

load_dotenv()

CRM_API_URL = os.getenv("CRM_API_URL")
CRM_API_KEY = os.getenv("CRM_API_KEY")
INVOICE_API_URL = os.getenv("INVOICE_API_URL")
INVOICE_API_KEY = os.getenv("INVOICE_API_KEY")

def book_meeting(title, start_time, end_time, attendees):
    """
    Mock function to book meeting (replace with Google Calendar or MCP API)
    """
    print(f"Booking meeting '{title}' from {start_time} to {end_time} with {attendees}")
    return {"status": "success", "meeting_id": "mock123"}

def update_crm(customer_name, details):
    """
    Update CRM (mock endpoint)
    """
    payload = {"customer_name": customer_name, "details": details}
    headers = {"Authorization": f"Bearer {CRM_API_KEY}"}
    # Mock request
    print(f"Updating CRM for {customer_name}: {details}")
    return {"status": "success", "crm_id": "crm123"}

def create_invoice(customer_name, amount, description):
    """
    Create invoice (mock)
    """
    payload = {"customer_name": customer_name, "amount": amount, "description": description}
    headers = {"Authorization": f"Bearer {INVOICE_API_KEY}"}
    print(f"Creating invoice for {customer_name}: ${amount} - {description}")
    return {"status": "success", "invoice_id": "inv123"}
