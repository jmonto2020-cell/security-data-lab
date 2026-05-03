# Security Incident Report – Authentication Log Analysis

## 1. Overview

This report documents the analysis of authentication logs to identify suspicious login activity and potential brute-force attempts.

The dataset contains authentication events with timestamps, usernames, IP addresses, event types, and login status (success/fail).

The objective of this analysis is to detect abnormal login behavior and simulate a basic Security Operations Center (SOC) detection workflow.

---

## 2. Scope

The analysis focuses on:

- Authentication failure patterns
- IP-based login anomalies
- Repeated login attempts within short time intervals

No production or real user data is used. All data is simulated for educational purposes.

---

## 3. Detection Methodology

The log data was processed using Python and Pandas. The following steps were performed:

- Loading and parsing CSV log data
- Normalization of timestamp and status fields
- Filtering failed login events
- Grouping events by IP address
- Counting failed login attempts per IP
- Applying a threshold-based detection rule (≥ 3 failed attempts)

---

## 4. Findings

### 4.1 Suspicious IP Activity

| IP Address   | Failed Attempts | Status   |
|--------------|----------------|----------|
| 10.0.0.5     | 3              | Flagged  |

### 4.2 Event Summary

- IP address 10.0.0.5 generated multiple failed login attempts
- Attempts occurred within a short time window (10:02–10:04)
- No successful authentication recorded for this IP during the observed period

---

## 5. Analysis

The observed behavior from IP 10.0.0.5 is consistent with a brute-force login attempt pattern.

Key indicators:

- Multiple consecutive authentication failures
- Short time interval between attempts
- No successful login following repeated failures

This behavior is commonly associated with automated login attacks or credential-guessing activity.

---

## 6. Risk Assessment

| Severity | Description |
|----------|------------|
| Medium   | Repeated failed authentication attempts from a single IP may indicate brute-force activity |

---

## 7. Recommendations

- Implement rate limiting on authentication endpoints
- Introduce account lockout after repeated failed login attempts
- Monitor failed login patterns in real time
- Integrate authentication logs into a SIEM system for automated alerting

---

## 8. Conclusion

The analysis identified one IP address exhibiting behavior consistent with a potential brute-force attack pattern.

While no successful login was observed, the repeated failures indicate suspicious activity that should be monitored or blocked in a production environment.

---

## 9. Tools Used

- Python 3
- Pandas
- CSV log dataset

Notes

This analysis is based on simulated log data and is intended for educational purposes only. No real user or production data was used.
