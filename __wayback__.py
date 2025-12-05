"""
Annotated Deleted Directory - Wayback API Calls for Directory Search
--------------------------------
This script serves as the data processing script for Wayback Calls. Its primary task is
1. Call URLs of relevent directories from the Wayback Machine API
2. Build exisiting list of URLs for the annotated directory

Author: Alexander O. Smith (2025–present)
Maintainer: Alexander O. Smith <aos35@cornell.edu>
"""

from wayback import WaybackMachineCDXServerAPI

# Initialize the API
cdx = WaybackMachineCDXServerAPI()

# Search for captures of a specific URL
for capture in cdx.search("example.com"):
    print(f"Date: {capture.timestamp} - URL: {capture.original}")

# Search with filters
for capture in cdx.search(
    "example.com",
    from_date="20200101",
    to_date="20201231",
    match_type="prefix",  # Also try "exact", "host", "domain"
):
    print(f"{capture.timestamp} - {capture.original}")
