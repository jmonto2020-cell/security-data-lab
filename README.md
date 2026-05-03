# Security Data & Log Analysis Lab
This project simulates a Security Operations Center (SOC) workflow by analyzing authentication log data to detect suspicious activity and potential brute-force attacks.

## Overview
The dataset contains login events with timestamps, users, IP addresses, and authentication status.
The project processes raw logs, cleans the data, and applies detection logic to identify abnormal patterns.

## Objectives
* Parse and analyze authentication logs
* Detect repeated failed login attempts
* Identify suspicious IP behavior
* Simulate SOC-style monitoring and alerting
* Build a basic ETL pipeline for log processing

## Workflow
1. **ETL Pipeline**
   * Cleaned and normalized log data (timestamps, status fields)
   * Removed invalid or missing entries

2. **Detection Logic**
   * Filtered failed login attempts
   * Grouped events by IP address
   * Applied threshold-based detection

3. **Alert Generation**
   * Flagged IPs exceeding failed login thresholds
   * Generated alerts for potential brute-force activity

## Example Detection
The analysis identified the following suspicious behavior:
* IP `10.0.0.5` generated **3 consecutive failed login attempts**
* This exceeds the defined threshold and is flagged as a potential brute-force attempt

## Key Concepts
* SOC monitoring and alerting
* Log parsing and anomaly detection
* Basic threat detection (brute-force attacks)
* ETL pipelines for security data

## Skills Demonstrated
* Python for security automation
* Pandas for log analysis
* Detection logic design
* Security event analysis

## Author
Engineering student focusing on cybersecurity, with interest in:
* Security Operations Center (SOC)
* Incident Response (IR)
* Security data analysis

##  Note
This project uses simulated data and is intended for educational purposes only.
