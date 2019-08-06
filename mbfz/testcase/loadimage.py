import  requests
from requests_toolbelt import MultipartEncoder
import unittest
import os
import json


class loadingTest(unittest.TestCase):
    def setUp(self):
        self.bash_url = 'http://yjjktest.yunjiacloud.com/yj-mbfz-ws/services/file/220015'
        # self.bash_url = 'http://192.168.34.28:8080/yj-mbfz-ws/services/file/220015'

    def test_load(self):
        # postData = {}
        # postData['funcode'] = "220015"
        # arg = {}
        # arg['revisitId'] = "198"
        # arg['pictureType'] = "avater"
        # # fileSize = os.chdir('/Users/apple/Downloads/1.jpg')
        # file_payload = {'file': open('/Users/apple/Downloads/1.jpg', 'rb')}
        # m = MultipartEncoder(file_payload)
        # arg['targetFile'] = m
        # postData['args'] = arg
        m = MultipartEncoder(
            fields={'pictureType': 'avater', 'psnId': '198',
                    'targetFile': ('filename', open('/Users/apple/Downloads/1.jpg', 'rb'), 'text/plain')}
        )
        headers = {"Content-Type": m.content_type}
        response = requests.post(self.bash_url, data=m, headers=headers)
        print(response)


