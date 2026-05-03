Incident Report – Authentication Log Analysis

1. Summary

This report documents the analysis of authentication logs to identify potential brute-force activity and suspicious login behavior. The dataset contains login events with timestamps, usernames, IP addresses, and authentication status (success/fail).
The analysis identified repeated failed login attempts originating from specific IP addresses, indicating possible automated attack behavior.

2. Detection Method

A Python-based log analysis pipeline was used to:
•	Parse authentication logs from CSV format 
•	Normalize timestamp and status fields
•	Filter failed login attempts
•	Group events by IP address
•	Count failed login occurrences per IP
•	Apply a threshold-based detection rule

Detection rule:
•	Any IP with ≥ 3 failed login attempts is flagged as suspicious

3. Findings / Evidence

The following suspicious activity was detected:
•	IP Address: 10.0.0.5
  o	Failed login attempts: 3
  o	Timeframe: 2025-01-01 10:02 – 10:04
  o	Pattern: Consecutive failed login attempts within a short time window
•	IP Address: 192.168.1.10
  o	Failed login attempts: 1
  o	Status: Not flagged (below threshold)

4. Analysis

The IP 10.0.0.5 shows characteristics consistent with a brute-force login attempt, including:
•	Multiple failed authentication attempts in rapid succession 
•	No successful login following failures 
•	Repetitive login behavior from a single source IP 
This pattern suggests either:
•	Automated attack tool activity, or 
•	Misconfigured client repeatedly attempting authentication 

5. Conclusion & Recommendations

Conclusion
The system detected one IP exhibiting behavior consistent with a potential brute-force attack.
Recommendations
•	Implement IP-based rate limiting 
•	Introduce account lockout after repeated failed attempts 
•	Monitor repeated authentication failures in real time 
•	Integrate alerts into a SIEM system for automated detection 

6. Notes

This analysis is based on simulated log data and is intended for educational purposes only. No real user or production data was used.
