# 🛡️ Active Directory Monitoring Lab

<p align="center">
  <strong>Cybersecurity | Windows Security Logs | Python | Kali Linux</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Kali%20Linux-557C94?logo=kalilinux&logoColor=white" alt="Kali Linux">
  <img src="https://img.shields.io/badge/Focus-Security%20Monitoring-red" alt="Security Monitoring">
  <img src="https://img.shields.io/badge/Project-Educational-green" alt="Educational Project">
</p>

## 📌 Project Overview

The **Active Directory Monitoring Lab** is a beginner-friendly cybersecurity project designed to analyze Windows Security event logs and identify potentially suspicious authentication activity.

The project uses Python on Kali Linux to process exported Windows event data, detect repeated failed login attempts, identify account lockouts, and generate a security report.

This project provides hands-on experience with security event analysis, log processing, and basic threat detection.

## 🎯 Objectives

- Monitor Windows authentication events using exported Security logs.
- Identify successful and failed logon events.
- Detect repeated failed login attempts.
- Identify account-lockout events.
- Summarize activity by username and source IP address.
- Generate a readable security monitoring report.
- Practice defensive cybersecurity analysis using Kali Linux and Python.

## 🧰 Technologies Used

| Technology | Purpose |
|---|---|
| Kali Linux | Security analysis environment |
| Python 3 | Log processing and alert generation |
| Windows Security Logs | Authentication event source |
| PowerShell | Export Windows event records |
| CSV | Store and transfer event data |
| Git and GitHub | Version control and project hosting |

## 📂 Project Structure

```text
Active-Directory-Monitoring/
│
├── monitor.py
├── sample_events.csv
├── security_report.txt
├── requirements.txt
└── README.md
```

### File Descriptions

- `monitor.py` — analyzes event records and generates alerts.
- `sample_events.csv` — contains sample Windows security events for testing.
- `security_report.txt` — contains the generated analysis report.
- `requirements.txt` — lists Python dependencies; the current version uses only the standard library.
- `README.md` — project documentation.

## ⚙️ Installation and Setup

### Step 1: Update Kali Linux

```bash
sudo apt update
sudo apt install -y python3 python3-venv git
```

### Step 2: Create the Project Directory

```bash
mkdir -p ~/cybersecurity-projects/active-directory-monitor
cd ~/cybersecurity-projects/active-directory-monitor
```

### Step 3: Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 4: Add the Project Files

Create the required files:

```bash
touch monitor.py sample_events.csv requirements.txt README.md
```

Copy the Python monitoring code into `monitor.py` and the sample event records into `sample_events.csv`.

## ▶️ How to Run the Project

Run the analyzer:

```bash
python3 monitor.py
```

The program analyzes the supplied CSV file and displays:

- Successful logon count
- Failed logon count
- Account-lockout count
- Failed logons grouped by username
- Failed logons grouped by source IP
- Security alerts

The generated report is saved as:

```text
security_report.txt
```

## 🔍 Windows Security Event IDs

| Event ID | Description |
|---|---|
| `4624` | Successful logon |
| `4625` | Failed logon |
| `4740` | User account locked out |
| `4720` | User account created |
| `4722` | User account enabled |
| `4725` | User account disabled |

Event availability depends on the configured Windows audit policies and the machine producing the event.

## 🖥️ Collecting Windows Security Events

Active Directory runs on Windows Server. Kali Linux is used here to analyze the exported data.

To analyze real Windows events:

1. Use a Windows test machine or authorized lab environment.
2. Export the relevant Security events using PowerShell.
3. Save the exported records as `ad_events.csv`.
4. Transfer the CSV file to the Kali Linux project directory.
5. Rename it to `sample_events.csv`, or update the input filename in `monitor.py`.
6. Run the Python analyzer again.

For domain authentication investigations, collect appropriate events from the domain controller as well as relevant endpoints.

## 🚨 Detection Features

### Repeated Failed Logins

The current version generates an alert when the same username has at least three failed-login events in the supplied CSV file.

### Account Lockouts

The program identifies event ID `4740` and records an account-lockout alert.

### IP-Based Analysis

The program groups failed-login events by source IP address to help identify repeated activity.

**Note:** The current version counts events across the entire input file. It does not yet implement time-window correlation, continuous monitoring, or automated incident response.

## 🔮 Future Enhancements

Planned improvements include:

- [ ] Time-based failed-login detection
- [ ] Real-time Windows event collection
- [ ] Automated email notifications
- [ ] Dashboard using Flask
- [ ] Graphs and authentication trend analysis
- [ ] Export reports to CSV and JSON
- [ ] Integration with Wazuh or Splunk
- [ ] Improved event filtering and investigation notes

## 📚 Learning Outcomes

Through this project, I practiced:

- Python file handling and CSV processing
- Security event identification
- Basic authentication monitoring
- Event aggregation using Python
- Alert generation and report writing
- Kali Linux command-line workflows
- Git and GitHub project management

## 🔐 Security and Responsible Use

This project is intended for educational and defensive cybersecurity purposes.

- Analyze only systems and logs you own or are authorized to access.
- Use synthetic sample records for initial testing.
- Protect exported logs because they may contain usernames, hostnames, and IP addresses.
- Do not publish sensitive organizational logs or personal information to GitHub.
- Treat generated alerts as indicators requiring investigation, not definitive proof of malicious activity.

## 👨‍💻 Author

**Ramesh**

GitHub: [prathakotaramesh2000-gif](https://github.com/prathakotaramesh2000-gif)

LinkedIn: [Connect with me](https://www.linkedin.com/in/prathakota-ramesh)

## ⭐ Conclusion

The Active Directory Monitoring Lab demonstrates a foundational approach to Windows authentication log analysis using Python and Kali Linux. It serves as a starting point for learning security monitoring, SIEM concepts, and defensive incident investigation.
