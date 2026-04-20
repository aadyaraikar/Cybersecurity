## File Integrity Monitor (FIM)
### 0x01 Overview
A Python-based utility that uses Cryptographic Hashing to detect unauthorized modifications to sensitive files. This simulates the core functionality of Host-based Intrusion Detection Systems (HIDS).

A typical FIM process has these processes:

Establishing a baseline: FIM creates a known baseline using factors such as settings and permissions, file contents, credentials, etc.

Change auditing: FIM verifies and validates files by comparing the latest version to this known baseline.

Alerting on suspicious changes: If FIM detects that files have been altered, updated, or compromised, it can generate alerts to ensure further investigation, and if necessary, remediation takes place.


### 0x02 Technical Deep Dive
Algorithm: Uses SHA-256 (Secure Hash Algorithm 256-bit) to create a unique digital fingerprint of the file data.

Mechanism: The script performs a binary read of the file to ensure data integrity is checked at the bit level.

Security Context: In a SOC (Security Operations Center) environment, FIM tools are used to monitor system configuration files (/etc/passwd, config.sys) for signs of tampering or malware persistence


### 0x03 Setup & Usage
Place the file you want to monitor in the directory.

Run the script: python fim.py

If the file is modified by even a single character, the generated hash will change entirely (The Avalanche Effect), triggering a security alert.

### 0x04 Key Learning Outcomes
Hashing vs. Encryption: Understand that hashes are one-way functions used for verification, not for hiding data.

Data Integrity: Hands-on experience with one of the three pillars of the CIA Triad (Confidentiality, Integrity, Availability).

### ⚠️ Disclaimer
This tool is for educational and ethical testing purposes only. Unauthorized scanning of networks you do not own or have explicit permission to test is illegal and unethical.
