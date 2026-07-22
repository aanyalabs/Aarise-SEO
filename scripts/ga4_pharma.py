from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, Dimension, Metric, DateRange, OrderBy
from google.oauth2 import service_account

KEY_FILE = r"C:\Users\priya\Downloads\level-district-353301-ce6e3430c94e (1).json"
PROPERTY_ID = "450152213"  # Aarise Pharma

creds = service_account.Credentials.from_service_account_file(
    KEY_FILE, scopes=["https://www.googleapis.com/auth/analytics.readonly"]
)
client = BetaAnalyticsDataClient(credentials=creds)

print("=" * 60)
print("GA4 — aarisepharma.com (last 28 days)")
print("=" * 60)

# 1. Traffic by channel
print("\n--- TRAFFIC BY CHANNEL ---")
req = RunReportRequest(
    property=f"properties/{PROPERTY_ID}",
    dimensions=[Dimension(name="sessionDefaultChannelGroup")],
    metrics=[Metric(name="sessions"), Metric(name="totalUsers"), Metric(name="engagementRate")],
    date_ranges=[DateRange(start_date="28daysAgo", end_date="today")],
    order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True)]
)
resp = client.run_report(req)
print(f"  {'Channel':<35} {'Sessions':>9} {'Users':>9} {'Eng%':>8}")
print(f"  {'-'*35} {'-'*9} {'-'*9} {'-'*8}")
for row in resp.rows:
    ch = row.dimension_values[0].value
    s = row.metric_values[0].value
    u = row.metric_values[1].value
    er = f"{float(row.metric_values[2].value)*100:.1f}%"
    print(f"  {ch:<35} {s:>9} {u:>9} {er:>8}")

# 2. Top pages
print("\n--- TOP PAGES BY SESSIONS ---")
req2 = RunReportRequest(
    property=f"properties/{PROPERTY_ID}",
    dimensions=[Dimension(name="pagePath")],
    metrics=[Metric(name="sessions"), Metric(name="averageSessionDuration"), Metric(name="bounceRate")],
    date_ranges=[DateRange(start_date="28daysAgo", end_date="today")],
    order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True)],
    limit=15
)
resp2 = client.run_report(req2)
print(f"  {'Page':<50} {'Sessions':>9} {'AvgTime':>9} {'Bounce':>8}")
print(f"  {'-'*50} {'-'*9} {'-'*9} {'-'*8}")
for row in resp2.rows:
    page = row.dimension_values[0].value[:50]
    s = row.metric_values[0].value
    t = int(float(row.metric_values[1].value))
    mins, secs = divmod(t, 60)
    br = f"{float(row.metric_values[2].value)*100:.1f}%"
    print(f"  {page:<50} {s:>9} {mins}m{secs:02d}s {br:>8}")

# 3. Traffic sources
print("\n--- TOP SOURCES ---")
req3 = RunReportRequest(
    property=f"properties/{PROPERTY_ID}",
    dimensions=[Dimension(name="sessionSource"), Dimension(name="sessionMedium")],
    metrics=[Metric(name="sessions"), Metric(name="totalUsers")],
    date_ranges=[DateRange(start_date="28daysAgo", end_date="today")],
    order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True)],
    limit=15
)
resp3 = client.run_report(req3)
print(f"  {'Source':<30} {'Medium':<15} {'Sessions':>9} {'Users':>9}")
print(f"  {'-'*30} {'-'*15} {'-'*9} {'-'*9}")
for row in resp3.rows:
    src = row.dimension_values[0].value[:30]
    med = row.dimension_values[1].value[:15]
    s = row.metric_values[0].value
    u = row.metric_values[1].value
    print(f"  {src:<30} {med:<15} {s:>9} {u:>9}")

# 4. Country breakdown
print("\n--- TOP COUNTRIES ---")
req4 = RunReportRequest(
    property=f"properties/{PROPERTY_ID}",
    dimensions=[Dimension(name="country")],
    metrics=[Metric(name="sessions"), Metric(name="totalUsers")],
    date_ranges=[DateRange(start_date="28daysAgo", end_date="today")],
    order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True)],
    limit=15
)
resp4 = client.run_report(req4)
print(f"  {'Country':<30} {'Sessions':>9} {'Users':>9}")
print(f"  {'-'*30} {'-'*9} {'-'*9}")
for row in resp4.rows:
    country = row.dimension_values[0].value[:30]
    s = row.metric_values[0].value
    u = row.metric_values[1].value
    print(f"  {country:<30} {s:>9} {u:>9}")
