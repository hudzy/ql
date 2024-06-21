"""
cron: 0 17 * * *
new Env('validateCookie');
"""

#!/usr/bin/env python3
# coding: utf-8
# Notify on invalid JD_COOKIE
# https://github.com/hudzy/ql/raw/master/validateCookie.py

import os
import requests
from notify import send
from datetime import datetime

class getJDCookie(object):

    # Retrieve cookies from environment variables
    def getCookie(self):
        global cookies
        cookies = []
        try:
            # Check if the "JD_COOKIE" environment variable exists
            if "JD_COOKIE" in os.environ:
                # Ensure the length of the cookie string is greater than 10
                if len(os.environ["JD_COOKIE"]) > 10:
                    # Split the cookie string by '&' to handle multiple cookies
                    cookies = os.environ["JD_COOKIE"].split('&')
                    print(f"\n[{self.getCurrentTime()}] Retrieved cookies from environment variables\n")
                    return
        except Exception as e:
            print(f"【getCookie Error】{e}")

    # Fetch user information using the provided cookie
    def getUserInfo(self, ck, pinName, userNum):
        url = 'https://me-api.jd.com/user_new/info/GetJDUserInfoUnion?orgFlag=JD_PinGou_New&callSource=mainorder&channel=4&isHomewhite=0&sceneval=2&sceneval=2&callback='
        headers = {
            'Cookie': ck,
            'Accept': '*/*',
            'Connection': 'close',
            'Referer': 'https://home.m.jd.com/myJd/home.action',
            'Accept-Encoding': 'gzip, deflate, br',
            'Host': 'me-api.jd.com',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Mobile/15E148 Safari/604.1',
            'Accept-Language': 'zh-cn'
        }
        try:
            # Send a GET request to the API endpoint with headers
            resp = requests.get(url=url, headers=headers, timeout=60).json()
            if resp['retcode'] == "0":
                # Retrieve the nickname from the response data
                nickname = resp['data']['userInfo']['baseInfo']['nickname']
                if not nickname:
                    # Use the current pin if nickname is not available
                    nickname = resp['data']['userInfo']['baseInfo']['curPin']
                return ck, nickname
            else:
                context = f"Account {userNum}【{pinName}】Cookie has expired! Please re-acquire.\n"
                print(f"[{self.getCurrentTime()}] {context}")
                return ck, False
        except Exception:
            context = f"Account {userNum}【{pinName}】Cookie has expired! Please re-acquire.\n"
            print(f"[{self.getCurrentTime()}] {context}")
            return ck, False
    
    # Get the current time as a string
    def getCurrentTime(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    jd_cookie = getJDCookie()
    jd_cookie.getCookie()
    
    if not cookies:
        # Notify if no cookies are found
        send("Cookie Status", "No cookies found in environment variables.")
        return

    expired_cookies_report = ""
    # Iterate through the list of cookies and validate each one
    for idx, cookie in enumerate(cookies):
        pinName = f"user{idx+1}"
        ck, status = jd_cookie.getUserInfo(cookie, pinName, idx+1)
        if status:
            # Print valid cookie information
            print(f"[{jd_cookie.getCurrentTime()}] Account {idx+1}【{status}】Cookie is valid.\n")
        else:
            # Print and append invalid cookie information to the expired cookies report
            print(f"[{jd_cookie.getCurrentTime()}] Account {idx+1}【{status}】Cookie has expired!\n")
            expired_cookies_report += f"Account {idx+1}【{pinName}】Cookie has expired! Please re-acquire.\n"
    
    # Send the expired cookies report using the notify module if there are expired cookies
    if expired_cookies_report:
        send("Cookie Status Report", expired_cookies_report)

if __name__ == "__main__":
    main()
