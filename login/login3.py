import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'HSID=ArSuqcuZHW2nrwFXO; SSID=AAVapetRk0sNb6YAn; APISID=I6A0pigblbvswlTx/Ad4dQbVOgTnL98TOf; SAPISID=bPH3bnhHTpC1avNe/AA6uT-98KxcZ6gLBI; __Secure-1PAPISID=bPH3bnhHTpC1avNe/AA6uT-98KxcZ6gLBI; __Secure-3PAPISID=bPH3bnhHTpC1avNe/AA6uT-98KxcZ6gLBI; LOGIN_INFO=AFmmF2swRQIgauRLsl3d8OVelNUi8MDTkE3mT4P2cs-GTqt2LbPqZzkCIQCCX_OwCzAelKjGX1PgVP9vv6HtSqAhasfoZp96aMkeUw:QUQ3MjNmeEFjRGFfYnlCVTR6Q1FTNUNYeHFxSGx2WXdSYXVwSFFsUFB5RG9TOVkzcG05d2E4XzVIbkRYZk15eFMwYlEtMTJMMWtuSVAtUExuWDJkdXEwbnBsNnRyRUo5anA2QWcxbHJPZ0IzU1hMcXBrN19haDNuRE1ZcEZRUGhyNUY2ZXZORVBSZk5ieHpKM0IzZ2I1UUZ6ZDQxU25TQ1ln; PREF=f7=4100&tz=Asia.Tokyo; VISITOR_INFO1_LIVE=D-vt12YPrIU; VISITOR_PRIVACY_METADATA=CgJKUBIEGgAgVQ%3D%3D; YSC=C7f8S0dGyOo; __Secure-ROLLOUT_TOKEN=CLGSiLzD9fCe_gEQtYmarN_5iwMY_PT06MbNjAM%3D; SID=g.a000vwhsY2BZyeEhON9oirVxYBLEsJl4hdmVVX4tbHQxwYDSJJ-wQRpXu-fQAkETx1oIIdVO0wACgYKAZISARISFQHGX2Miq2H_0Nd2sylrKkRKFcJ1pBoVAUF8yKqx8Tivak88CPFDo7w6B93V0076; __Secure-1PSID=g.a000vwhsY2BZyeEhON9oirVxYBLEsJl4hdmVVX4tbHQxwYDSJJ-wuAjFLNUrJ_BrqMvuX4m0LAACgYKAaMSARISFQHGX2Mix39-QWP7BV9o7dHtAaQSHhoVAUF8yKqDoev3ML1moIFnGhmZJo8g0076; __Secure-3PSID=g.a000vwhsY2BZyeEhON9oirVxYBLEsJl4hdmVVX4tbHQxwYDSJJ-wm4TFJ1BCtXFAGdpDP2b4bQACgYKAbASARISFQHGX2MiJR3NCa7oLuotkZAOymERYhoVAUF8yKq2KymADizAgFOpmARimo0w0076; __Secure-1PSIDTS=sidts-CjIB7pHptR217_-1q9m2y1PyzwcO0MQWmgu_PuV6n5tJdFV6btHo_ki29SwccC7Sg8HoKxAA; __Secure-3PSIDTS=sidts-CjIB7pHptR217_-1q9m2y1PyzwcO0MQWmgu_PuV6n5tJdFV6btHo_ki29SwccC7Sg8HoKxAA; SIDCC=AKEyXzVszIlHt2C2YhpwXCEqLjhZcZjBEycyfu1EKygFKJCj382DSCC6lSqCI5IlX3-Cmz-AFHk; __Secure-1PSIDCC=AKEyXzWrGOT0z8IVcE-aXPVHutP35njmzNPNLJkD7IUz7BTY6Q-6XTXUDsu76wZTlItD4r5r_pU; __Secure-3PSIDCC=AKEyXzWL8geSjJRrevUfKNviZZLBNf6oPADw5y2xfYkY6wXbOgPNngzgC8ut1sxpomaVsxlmgts',
    'Host': 'https://www.youtube.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}
session  = requests.Session()
source = session.get('https://www.youtube.com/', headers=headers, verify=False).content.decode()
x = session.get('https://www.youtube.com/feed/history', headers=headers, verify=False).content.decode()
print(x)
