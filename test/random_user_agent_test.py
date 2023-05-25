#!/usr/bin/env python
if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from http import HTTPStatus
from bs4 import BeautifulSoup
import bcrypt
import pybase64
import requests
import json
import time
import asyncio
import clipboard
import re

from common.utils import global_log_append
from tenacity import retry, wait_fixed, stop_after_attempt

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

import datetime


class RandomUserAgentTest:
    def __init__(self):
        self.get_headers()
        print(self.headers)

    def set_user_agent(self):
        software_names = [SoftwareName.CHROME.value]
        operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
        user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
        self.user_agent = user_agent_rotator.get_random_user_agent()

    def get_headers(self):
        self.set_user_agent()
        self.headers = {
            "User-Agent": self.user_agent,
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6",
            "Referer": "https://m.land.naver.com/",
        }


if __name__ == "__main__":
    tester = RandomUserAgentTest()
