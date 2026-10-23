
# Active Directory Monitoring - Kali Linux Lab

This tool monitors Windows AD security events.

Events Monitored:
- 4624 - Successful logon
- 4625 - Failed logon  
- 4740 - Account locked out

Detection:
- Brute force attack (3+ failed logons)
- Account lockout alert

Run: python3 monitor.py
Input: sample_events.csv
