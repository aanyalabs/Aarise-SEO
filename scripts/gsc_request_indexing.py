"""
Request Google indexing for updated pages via Google Indexing API.

PREREQUISITE — service account must be a verified owner in GSC:
1. Go to https://search.google.com/search-console/users
2. Add search-console@level-district-353301.iam.gserviceaccount.com as OWNER (not user)
3. Do this for both aarisepharma.com and aarisehealthcare.com properties

Also enable the Indexing API in Google Cloud Console:
  https://console.cloud.google.com/apis/library/indexing.googleapis.com?project=level-district-353301
"""

from google.oauth2 import service_account
from googleapiclient.discovery import build
import json

KEY_FILE = r"C:\Users\priya\Downloads\level-district-353301-ce6e3430c94e (1).json"

# Indexing API needs this scope — different from readonly webmasters scope
SCOPES = ["https://www.googleapis.com/auth/indexing"]

URLS = [
    # 5 upgraded pages on aarisepharma.com
    "https://aarisepharma.com/who-gmp-certification-pharma-requirements-process/",
    "https://aarisepharma.com/coa-and-msds-for-pharmaceutical-apis/",
    "https://aarisepharma.com/third-party-pharmaceutical-manufacturing-india-complete-guide/",
    "https://aarisepharma.com/steroid-api-supplier-mumbai-india/",
    "https://aarisepharma.com/pharma-api-supplier-hyderabad-india/",
]

try:
    creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
    service = build("indexing", "v3", credentials=creds)

    print("=== Google Indexing API — Request Re-indexing ===\n")

    for url in URLS:
        try:
            body = {"url": url, "type": "URL_UPDATED"}
            response = service.urlNotifications().publish(body=body).execute()
            print(f"  ✓ {url}")
            print(f"    notifyTime: {response.get('urlNotificationMetadata', {}).get('latestUpdate', {}).get('notifyTime', 'n/a')}")
        except Exception as e:
            print(f"  ✗ {url}")
            print(f"    Error: {e}")

    print("\nDone. Google will re-crawl these URLs within 24-48 hours.")

except Exception as e:
    print(f"Auth error: {e}")
    print("\nIf you see a 403/permission error:")
    print("  1. Enable Indexing API: https://console.cloud.google.com/apis/library/indexing.googleapis.com?project=level-district-353301")
    print("  2. Add service account as OWNER in GSC: https://search.google.com/search-console/users")
    print("     Email: search-console@level-district-353301.iam.gserviceaccount.com")
