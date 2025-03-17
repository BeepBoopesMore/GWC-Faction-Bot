import requests

cookies = {
    'GuestData': 'UserID=-1244009054',
    '_ga_SFYEMVLMML': 'GS1.1.1689714021.27.1.1689714034.0.0.0',
    'rbx-ip2': '',
    'RBXSessionTracker': 'sessionid=fffaec41-675a-4c9c-979f-7f24cf7e423e',
    'ak_bmsc': '234AC1861F573C3398243461582BD952~000000000000000000000000000000~YAAQVWd7XL0QZmeJAQAAtbp1dBRC6bjkwz1SsGQZFuxpNCX3ivdKeCiDuTQrO+XjsXXu9lU57QGYKIEDJ6oUQbuI5Dx+4Z4V+yiGAhz5jeoISPMxjgWWgRgTh+hUzA1/MdgpX0bHpM7RCOUoKZHUPtiIle2LxgY6jXhENU9kTCpIyFZ1NnYW250yWM4Uru2f2AWnNoUxqD49PSPvmi0583BvpcyI6gwlnQxX06YClJ8ICyoujzHumlV5smuv1GhfSSVRQh6gQdOW7e1dLnfPteMyITFibXszgiEfYLNSXlOQen6XvuGSlqgQ7CRdkA0WVx3cQBScjCjtc794OMU8nn3cG1kRv3d3mTTrHjDGQA2bTPJMxdmmWJYTQyibmg2ttq5Dp7PyYU/HIYBOMPhEzuvWXrItdr6FC5yoyHoDMrN7ZTg=',
    'bm_mi': '35A5EC227BAADC0A7F3E2F9E7498E5E9~YAAQVWd7XAARZmeJAQAAKr11dBSEeQPqfmgxcd2r+AfTxZYwiRQI9GdhdexAvZTsnZTeV3lfdITkd++ZLSp9jFPoJfJbeBB0gGuXBPBwgq1iriW/Bh2g7xPtW6KwFGOmRUC2aVsRMYL09WZvNXiUnle1TlHKJffDHtE6OdzZE9c4xGFqP3PDslJFH1buqVId3JIqIO0XvRWI0i0ndQKXJBI9RUmxH6Ii9e2Tm7B/8fnWU97GZmqnjIIaQxsW5hZhp5cdlGLnv6m7iN/FxKAToXJ+4jtvgWNpaOEsCJrBdH8kp5uEEBLdqgOa/cQh4BfRxJhFwg0jonVYxXFG0tjvYtjPPqFTmMxyY0RaXLzMwMTJvCv8LiZ+B9aUAoE=~1',
    'bm_sv': '54E923B00E1BAEA0A1E0822D36949C7C~YAAQVWd7XNISZmeJAQAA9tF1dBT/3W5UYc1Axs1JJQuY7DSkAC8ekLKptXIibPgvdSAFneR/IiHbcNI9oSBOvCRXIahdil8kKk9vJoiFTnZ85zq7pdR1psYPa5L8pk9OiUeEy3FsSh5U0yl03EbjbrDwMIxW0mV7uOMPljOgUk2HdSu97goGnR0JODIX/Yg/+O6xQUEoBj6WMDJE/BLsQY/bBl/ySmZChr+AUkQvteH21cz5wU6fRk39BhCnF3dM~1',
    '_ga_BK4ZY0C59K': 'GS1.1.1689876021.2.1.1689876040.0.0.0',
}

headers = {
    'authority': 'groups.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json;charset=UTF-8',

    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82',
    'x-csrf-token': 'ALBWb6zt2KMD',
}

json_data = {
    'roleId': int(input("Robloxroleid:")),
}

response = requests.patch(
    'https://groups.roblox.com/v1/groups/32747381/users/' + input("Robloxid:"),
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"roleId":99615873}'
#response = requests.patch(
#    'https://groups.roblox.com/v1/groups/32747381/users/4833763176',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)


res = response.text
print(res)