# 🛡️ Ransomware Defense and Recovery System for SMEs

## Overview

The **Ransomware Defense and Recovery System** is a lightweight cybersecurity solution developed to improve ransomware resilience for **Small and Medium Enterprises (SMEs)**. The system continuously monitors file system activities, detects suspicious file behavior associated with ransomware attacks, automatically creates backup copies of important files, records system events, and provides a real-time monitoring dashboard.

This project was developed as part of an undergraduate research project titled:

> **Resilient, Low-Cost Ransomware Defense and Recovery Systems for Small and Medium Enterprises (SMEs)**

---

## Features

- Real-time file system monitoring
- Threshold-based ransomware detection
- Automatic file backup
- Event logging
- Alert generation
- Web-based monitoring dashboard
- Modular architecture for easy maintenance and future expansion

---

## System Architecture

The system consists of the following modules:

- **Monitoring Agent**
  - Watches file system activities using Watchdog.

- **Detection Server**
  - Receives file events and coordinates system operations.

- **Detection Engine**
  - Analyses file activity and identifies suspicious behaviour.

- **Backup Manager**
  - Creates automatic backup copies of monitored files.

- **Logging Module**
  - Records file events and security alerts.

- **Monitoring Dashboard**
  - Displays system activity in real time using Streamlit.

---

## Project Structure

```
Ransomware-Defense-System/
│
├── agent.py
├── server.py
├── dashboard.py
├── requirements.txt
│
├── config/
│   └── settings.py
│
├── modules/
│   ├── backup_manager.py
│   ├── detector.py
│   └── logger.py
│
├── logs/
│
├── backup/
│
├── auto_backup/
│
└── test_files/
```

---

## Technologies Used

- Python 3
- Flask
- Streamlit
- Watchdog
- Pandas
- Requests
- OS
- Shutil

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Chrismontin/Ransomware-Defense-System2.git
```

Move into the project folder:

```bash
cd Ransomware-Defense-System2
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Start the Detection Server

```bash
python server.py
```

---

### Start the Monitoring Agent

```bash
python agent.py
```

---

### Launch the Dashboard

```bash
python -m streamlit run dashboard.py
```

The dashboard will open automatically in your browser.

---

## Testing

To test the prototype:

1. Start the server.
2. Start the monitoring agent.
3. Launch the Streamlit dashboard.
4. Create, modify, rename, or delete files inside the monitored directory.
5. Observe:
   - File events
   - Backup generation
   - Event logging
   - Dashboard updates
   - Detection alerts (when the configured threshold is exceeded)

---

## Results

The implemented prototype successfully demonstrates:

- Continuous file monitoring
- Automatic backup generation
- Behaviour-based ransomware detection
- Real-time dashboard updates
- Event logging
- Alert generation

The project confirms that affordable open-source technologies can be used to improve ransomware resilience for Small and Medium Enterprises.

---

## Current Limitations

The current prototype:

- Uses threshold-based behavioural detection
- Was evaluated in a controlled environment
- Stores backups locally
- Supports a single monitored endpoint

These limitations provide opportunities for future improvement.

---

## Future Improvements

Possible enhancements include:

- Machine learning-based ransomware detection
- Cloud backup integration
- Email and SMS notifications
- Multi-device monitoring
- User authentication
- Encrypted backups
- SIEM integration
- Role-based access control

---

## Author

**Chris Montin**

Bachelor of Science in Cyber Security

Final Year Research Project

---

## License

This project is intended for academic and educational purposes.

```

---

# Optional improvements

I also recommend adding these files to your repository:

- `LICENSE` (for example, the MIT License if you want others to use your code)
- `CONTRIBUTING.md` (if you ever want collaborators)
- `CHANGELOG.md` (to track future versions)

Finally, I'd suggest enhancing the README with **screenshots** once you've captured them. A "Screenshots" section showing the dashboard, server, and monitoring agent would make the repository much more engaging and immediately demonstrate that the project is functional.
