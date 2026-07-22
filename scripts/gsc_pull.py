import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta

KEY_FILE = r"C:\Users\priya\Downloads\level-district-353301-ce6e3430c94e (1).json"
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]

creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
service = build("searchconsole", "v1", credentials=creds)

# List all verified properties first
sites = service.sites().list().execute()
print("=== VERIFIED PROPERTIES ===")
for s in sites.get("siteEntry", []):
    print(f"  {s['siteUrl']}  ({s['permissionLevel']})")

SITES = [
    "https://aarisepharma.com/",
    "https://aarisehealthcare.com/",
    "sc-domain:aarisepharma.com",
    "sc-domain:aarisehealthcare.com",
]

end = datetime.today().strftime("%Y-%m-%d")
start = (datetime.today() - timedelta(days=28)).strftime("%Y-%m-%d")

for site_url in sites.get("siteEntry", []):
    url = site_url["siteUrl"]
    print(f"\n{'='*60}")
    print(f"SITE: {url}")
    print(f"Period: {start} to {end}")
    try:
        body = {
            "startDate": start,
            "endDate": end,
            "dimensions": ["query"],
            "rowLimit": 20,
            "orderBy": [{"fieldName": "impressions", "sortOrder": "DESCENDING"}]
        }
        res = service.searchanalytics().query(siteUrl=url, body=body).execute()
        rows = res.get("rows", [])
        if not rows:
            print("  No data returned.")
        else:
            print(f"  {'Keyword':<50} {'Clicks':>7} {'Impressions':>12} {'CTR':>7} {'Pos':>6}")
            print(f"  {'-'*50} {'-'*7} {'-'*12} {'-'*7} {'-'*6}")
            for r in rows:
                kw = r["keys"][0][:50]
                clicks = int(r["clicks"])
                impr = int(r["impressions"])
                ctr = f"{r['ctr']*100:.1f}%"
                pos = f"{r['position']:.1f}"
                print(f"  {kw:<50} {clicks:>7} {impr:>12} {ctr:>7} {pos:>6}")
    except Exception as e:
        print(f"  ERROR: {e}")
