import requests

url = "https://vincentc.work/api/auth/local/register"

payload = "username=vincent123&email=cwc210018111%2B2%40gmail.com&gender=Male&password=123456&role=Public&phone_number=94440589"
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": "Bearer 6527905795ccfdbdeb8ec2a15a08766b623903dea50a72a5f8a7977bf1c0cf9afebdfc3d95995be4a65b024fb8b639c0e5c854a0ab361d1e902019e9ea08f6243e3bd2739dd596bafd2a2689c5e5ff1714a3e1d86f4a61c5a61ab1d1d1f92ad42ea7bf7ac82f21eb33d1101c8ddd405132096a10b22f2c21e86b138df01cc96c",
    "Cookie": "__cf_bm=vcPlcsvOUVM8Azng51m0Qrh4Kwc0BKm1CbQO5HE7cRc-1700293407-0-ASULdpQEDelbyIaF5rbLiaNrYIJ7vnjCWsmi9qtUcHhFEyiq6kS+mi+vi58N/vsmOTjtm3cTm++MUPHZaLRyRlg=",
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
