# Threat Detection and Response

## Overview
This project involves investigating a suspicious domain name using Chronicle. The scenario involves identifying whether employees have received phishing emails containing the domain and whether they have visited the domain. The investigation includes performing a domain search, evaluating search results, and investigating threat intelligence data, affected assets, and resolved IP addresses.

## Scenario
You are a security analyst at a financial services company. You receive an alert that an employee received a phishing email in their inbox. You review the alert and identify a suspicious domain name contained in the email's body: signin.office365x24.com. You need to determine whether any other employees have received phishing emails containing this domain and whether they have visited the domain.

## Project Steps

### 1. Perform a Domain Search
- **VT CONTEXT**: VirusTotal information available for the domain.
- **WHOIS**: Information about the domain using WHOIS.
- **Prevalence**: Historical prevalence of the domain.
- **Resolved IPs**: IP addresses that map to the domain.
- **Sibling Domains**: Domains sharing a common top or parent domain.
- **Timeline**: Events and interactions made with the domain.
- **Assets**: List of assets that have accessed the domain.

### 2. Evaluate the Search Results
- **VT CONTEXT**: 12/94 security vendors flagged this domain as malicious. Refer to VT_CONTEXT.png.
- **WHOIS**: Information about the domain owner. Refer to WHOIS.txt.
- **Prevalence**: Last accessed by 6 assets on July 9, 2023. Refer to Prevalence.png.
- **Resolved IPs**: 104.215.148.63, 40.100.174.34. Refer to Resolved_IPs.txt.
- **Sibling Domains**: login.office365x24.com.
- **Timeline**: 8 assets accessed the domain across 3 days. Refer to Timeline.csv.
- **Assets**: 6 total assets. Refer to Assets.csv.

### 3. Investigate the Affected Assets and Events
- **POST Requests**: 6 POST requests to /login.php.
	- 1/31/23 14:40:45 ashton-davidson-pc
	- 1/31/23 14:42:45 emil-palmer-pc
	- 7/8/23 5:02:47 ashton-davidson-pc
	- 7/8/23 5:04:47 emil-palmer-pc
	- 7/9/23 5:02:44 ashton-davidson-pc
	- 7/9/23 5:04:44 emil-palmer-pc
- **Assets**: All 6 assets were affected.

### 4. Investigate the Resolved IP Address
- **Resolved IP Address**: 40.100.174.34.
- **Timeline**: New POST /login.php.
	- 1/31/23 14:51:45 warren-morris-pc
- **Assets**: New affected asset.
	- warren-morris-pc
- **Domains**: signin.accounts-google.com, signin.office365x24.com.

### 5. Domain Investigation
- **Assets Accessed**: 6 assets. Refer to Assets.csv.
- **Resolved IP Address**: signin.office365x24.com resolves to the IP address 40.100.174.34.
- **POST Requests to IP address 40.100.174.34**: 3 POST requests were made to 40.100.174.34 . This indicates that sensitive information was submitted to the login page such as login credentials.
- **Target URL**: The POST requests were sent to signin.office365x24.com/login.php.
- **Resolved Domains**: 40.100.174.34 resolves to both signin.accounts-gooqle.com and signin.office365x24.com.

## Conclusion
After investigating, I found that the suspicious domain was involved in phishing campaigns, affecting several assets as login information was sent via POST requests. By examining the IP address, I also uncovered two more related domains. This investigation shows how crucial it is to thoroughly analyze domains to identify and stop phishing threats. Using tools like Chronicle, I gained valuable insights into malicious activities, protected our assets, and improved our overall cybersecurity.
