"""
Annotated Deleted Directory - Zotero API Calls for Directory Processing
--------------------------------
This script serves as the data processing script for Zoero Calls. Its primary task is
1. Call HTML screen captures and Zotero metadata
2. Ping URLs in HTML and metadata to create URLs to check

Author: Alexander O. Smith (2025–present)
Maintainer: Alexander O. Smith <aos35@cornell.edu>
"""

# Standard Libraries
import requests
import json
import os

# Third-party Libraries
import dotenv
# from pyzotero import zotero

_ = dotenv.load_dotenv(dotenv.find_dotenv())
API_KEY = os.environ.get("API_KEY")
GROUP_ID = os.environ.get("GROUP_ID")
BASE_URL = f"https://api.zotero.org/groups/{GROUP_ID}/items"


# Fetch all items in the LIGO group library
headers = {"Authorization": f"Bearer {API_KEY}"}
params = {"format": "json", "limit": 100}
response = requests.get(BASE_URL, headers=headers, params=params)
items = response.json()
print(items)
