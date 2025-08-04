import requests
import certifi

url = "https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg"

try:
    response = requests.get(url, timeout=5, verify=certifi.where())
    print("✅ Status code:", response.status_code)
except requests.exceptions.SSLError as e:
    print("❌ SSL Error:", e)
except Exception as ex:
    print("⚠️ Other error:", ex)
