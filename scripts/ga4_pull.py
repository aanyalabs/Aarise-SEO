from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest, Dimension, Metric, DateRange, OrderBy
)
from google.oauth2 import service_account

KEY_FILE = r"C:\Users\priya\Downloads\level-district-353301-ce6e3430c94e (1).json"
PROPERTY_ID = "535124183"  # Aarise Health from URL: p535124183

creds = service_account.Credentials.from_service_account_file(
    KEY_FILE,
    scopes=["https://www.googleapis.com/auth/analytics.readonly"]
)
client = BetaAnalyticsDataClient(credentials=creds)

print("=" * 60)
print(f"GA4 PROPERTY: {PROPERTY_ID} (Aarise Health)")
print("=" * 60)

# 1. Traffic by channel — last 28 days
print("\n--- TRAFFIC BY CHANNEL (last 28 days) ---")
req = RunReportRequest(
    property=f"properties/{PROPERTY_ID}",
    dimensions=[Dimension(name="sessionDefaultChannelGroup")],
    metrics=[
        Metric(name="sessions"),
        Metric(name="totalUsers"),
        Metric(name="engagementRate"),
    ],
    date_ranges=[DateRange(start_date="28daysAgo", end_date="today")],
    order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True)]
)
resp = client.run_report(req)
print(f"  {'Channel':<35} {'Sessions':>9} {'Users':>9} {'Eng.Rate':>10}")
print(f"  {'-'*35} {'-'*9} {'-'*9} {'-'*10}")
for row in resp.rows:
    ch = row.dimension_values[0].value
    s = row.metric_values[0].value
    u = row.metric_values[1].value
    er = f"{float(row.metric_values[2].value)*100:.1f}%"
    print(f"  {ch:<35} {s:>9} {u:>9} {er:>10}")

# 2. Top pages by sessions
print("\n--- TOP PAGES BY SESSIONS (last 28 days) ---")
req2 = RunReportRequest(
    property=f"properties/{PROPERTY_ID}",
    dimensions=[Dimension(name="pagePath")],
    metrics=[
        Metric(name="sessions"),
        Metric(name="averageSessionDuration"),
        Metric(name="bounceRate"),
    ],
    date_ranges=[DateRange(start_date="28daysAgo", end_date="today")],
    order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True)],
    limit=15
)
resp2 = client.run_report(req2)
print(f"  {'Page':<55} {'Sessions':>9} {'Avg Time':>9} {'Bounce':>8}")
print(f"  {'-'*55} {'-'*9} {'-'*9} {'-'*8}")
for row in resp2.rows:
    page = row.dimension_values[0].value[:55]
    s = row.metric_values[0].value
    t = int(float(row.metric_values[1].value))
    mins, secs = divmod(t, 60)
    br = f"{float(row.metric_values[2].value)*100:.1f}%"
    print(f"  {page:<55} {s:>9} {mins}m{secs:02d}s {br:>8}")

# 3. Last 7 days vs previous 7 days
print("\n--- THIS WEEK vs LAST WEEK ---")
req3 = RunReportRequest(
    property=f"properties/{PROPERTY_ID}",
    dimensions=[Dimension(name="date")],
    metrics=[Metric(name="sessions"), Metric(name="totalUsers")],
    date_ranges=[
        DateRange(start_date="7daysAgo", end_date="today"),
        DateRange(start_date="14daysAgo", end_date="8daysAgo"),
    ],
)
resp3 = client.run_report(req3)
this_week_s = sum(int(r.metric_values[0].value) for r in resp3.rows if r.dimension_values[0].value >= "20260716")
last_week_s = sum(int(r.metric_values[2].value) for r in resp3.rows)
print(f"  This week sessions: {this_week_s}")
print(f"  Last week sessions: {last_week_s}")

# 4. Traffic source / medium breakdown
print("\n--- TOP SOURCES (last 28 days) ---")
req4 = RunReportRequest(
    property=f"properties/{PROPERTY_ID}",
    dimensions=[Dimension(name="sessionSource"), Dimension(name="sessionMedium")],
    metrics=[Metric(name="sessions"), Metric(name="totalUsers")],
    date_ranges=[DateRange(start_date="28daysAgo", end_date="today")],
    order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True)],
    limit=15
)
resp4 = client.run_report(req4)
print(f"  {'Source':<30} {'Medium':<15} {'Sessions':>9} {'Users':>9}")
print(f"  {'-'*30} {'-'*15} {'-'*9} {'-'*9}")
for row in resp4.rows:
    src = row.dimension_values[0].value[:30]
    med = row.dimension_values[1].value[:15]
    s = row.metric_values[0].value
    u = row.metric_values[1].value
    print(f"  {src:<30} {med:<15} {s:>9} {u:>9}")
