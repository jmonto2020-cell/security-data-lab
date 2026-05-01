Security Data & Log Analysis Lab

This project simulates a Security Operations Center (SOC) workflow by processing and analyzing authentication log data to detect suspicious activity and security anomalies.

Objectives
- Parse and analyze authentication and system log data
- Detect suspicious login patterns such as repeated failed login attempts
- Identify potential IP-based anomalies and brute-force behavior
- Build a simple ETL pipeline for cleaning and transforming raw log data
- Practice SOC-style incident detection and security monitoring logic

Structure
- sample_logs.csv → raw authentication log dataset
- scripts/etl_pipeline.py → data cleaning and transformation pipeline
- scripts/anomaly_detector.py → detection of failed login patterns and suspicious activity

Key Concepts
- SOC monitoring and security event analysis
- Log parsing and anomaly detection
- ETL (Extract, Transform, Load) pipelines
- Basic threat detection logic (failed logins, suspicious IP behavior)

Skills Demonstrated
- Python for security automation
- Pandas-based log processing and transformation
- Security event analysis and pattern detection
- Basic incident detection and SOC workflow simulation

Author
Engineering student specializing in systems, automation, and applied cybersecurity (SOC, incident response, and security data analysis)

Note: This project is a simulated SOC environment for learning purposes and does not process real sensitive data.
