"""
===========================================
HTTP REQUESTS USING PYTHON (requests module)
===========================================

This file demonstrates:
1. GET requests
2. POST requests
3. Query parameters
4. Headers & status codes
5. Downloading binary content (images)
6. JSON responses
7. Authentication
8. Timeouts & delays
9. Common HTTP status codes (reference)

Author intent:
- Learning HTTP practically
- Debugging-friendly
- Revisitable after a long break
"""

import requests as rq


# -------------------------------------------------
# 1. BASIC GET REQUEST
# -------------------------------------------------
r = rq.get("https://httpbin.org/get")

# r.text      -> response body as STRING (decoded text)
# r.content   -> response body as BYTES (raw)
# r.json()    -> parses JSON response into Python dict
# r.headers   -> response headers
# r.status_code -> HTTP status code (int)

# print(r.text)
# print(r.json())
# print(r.headers)
# print(r.status_code)
# print(r.ok)   # True if status_code < 400


# -------------------------------------------------
# 2. DOWNLOADING BINARY DATA (IMAGE)
# -------------------------------------------------
# IMPORTANT:
# - Images, PDFs, videos → binary data
# - Always use r.content and 'wb' mode

r_img = rq.get("https://imgs.xkcd.com/comics/python.png")

with open("python_comic.png", "wb") as img:
    img.write(r_img.content)


# -------------------------------------------------
# 3. QUERY PARAMETERS (GET with params)
# -------------------------------------------------
# params → added to URL as ?key=value

params = {
    "page": 2,
    "count": 25
}

r = rq.get(
    "https://httpbin.org/get",
    params=params,
    timeout=(1, 1)   # (connect_timeout, read_timeout)
)

# Shows final URL with encoded query params
print("Final URL:", r.url)


# -------------------------------------------------
# 4. POST REQUEST (sending data)
# -------------------------------------------------
# data=  → form-encoded (application/x-www-form-urlencoded)
# json=  → JSON body (application/json) [more common in APIs]

payload = {
    "username": "corey",
    "password": "testing"
}

r = rq.post(
    "https://httpbin.org/post",
    data=payload
)

# httpbin echoes back what it received
print("POST response JSON:", r.json())


# -------------------------------------------------
# 5. AUTHENTICATION (Basic Auth)
# -------------------------------------------------
auth_response = rq.get(
    "https://httpbin.org/basic-auth/corey/test",
    auth=("corey", "test")
)

print("Auth status:", auth_response.status_code)
print("Auth response:", auth_response.text)


# -------------------------------------------------
# 6. TIMEOUTS & DELAYS
# -------------------------------------------------
"""
timeout meaning:
- NOT total execution time
- Limits how long client waits for:
  1. connection
  2. server response (read)

delay endpoint is provided by httpbin.org
to simulate slow servers.
"""

try:
    delay_response = rq.get(
        "https://httpbin.org/delay/6",
        timeout=2   # seconds
    )
    print(delay_response)
except rq.exceptions.Timeout:
    print("Request timed out (as expected)")
except rq.exceptions.RequestException as e:
    print("Request failed:", e)


# -------------------------------------------------
# 7. COMMON HTTP STATUS CODES (REFERENCE)
# -------------------------------------------------
"""
Code | Meaning
-------------------------------
200  | OK – Request successful
201  | Created – Resource created
301  | Moved Permanently
302  | Found (Temporary redirect)
400  | Bad Request – Client error
401  | Unauthorized – Login required
403  | Forbidden – No permission
404  | Not Found
429  | Too Many Requests (rate limit)
500  | Internal Server Error
502  | Bad Gateway
503  | Service Unavailable
504  | Gateway Timeout
"""
