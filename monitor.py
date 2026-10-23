
import csv
from collections import defaultdict

print("=== Active Directory Monitor - Kali ===\n")

failed = defaultdict(int)
alerts = []

with open('sample_events.csv','r') as f:
    # clean blank lines
    lines = [l for l in f if l.strip()]
    
with open('sample_events.csv','w') as f:
    f.writelines(lines)

with open('sample_events.csv','r') as f:
    reader = csv.DictReader(f)
    # show what header it found
    print(f"Headers found: {reader.fieldnames}\n")
    
    for row in reader:
        # auto-clean keys (remove spaces, lower case)
        clean_row = {k.strip().lower(): v for k,v in row.items()}
        ts = clean_row.get('timestamp')
        eid = clean_row.get('event_id')
        user = clean_row.get('username')
        ip = clean_row.get('source_ip') if clean_row.get('source_ip') else "N/A"
        msg = clean_row.get('message')

        print(f"{ts} | {eid} | {user} | {ip} | {msg}")
        
        if eid == '4625':
            failed[user] += 1
        if eid == '4740':
            alerts.append(f"[CRITICAL] {user} LOCKED at {ts}")
        if eid == '4625' and failed[user] >= 3:
            alerts.append(f"[BRUTE FORCE] {user} {failed[user]} fails from {ip}")

print("\n--- FINAL REPORT ---")
for a in set(alerts):
    print(a)
print(f"\nFailed counts: {dict(failed)}")
