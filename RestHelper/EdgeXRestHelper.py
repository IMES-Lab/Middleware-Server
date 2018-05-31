import requests
import json


class VideoFovDataRestHelper:

    def __init__(self):
        pass

    def __del__(self):
        pass


class VideoInfoRestHelper:

    def __init__(self, API_HOST):
        self.API_HOST = API_HOST
        self.API_HEADERS = {'Content-Type': 'application/json'}

    def __del__(self):
        pass

    def post_addressable(self, addressable_object):
        url = self.API_HOST + 'addressable'
        addressable_data = addressable_object.getData()
        resp = requests.post(url=url, headers=self.API_HEADERS, json=addressable_data)
        print(addressable_data)
        print(resp.text)
        return resp

    def post_deviceService(self, deviceService_object):
        url = self.API_HOST + 'deviceservice'
        deviceService_data = deviceService_object.getData()
        resp = requests.post(url=url, headers=self.API_HEADERS, json=deviceService_data)
        print(deviceService_data)
        print(resp.text)
        return resp

    def post_deviceProfile(self, deviceProfile_object):
        url = self.API_HOST + 'deviceprofile'
        deviceProfile_data = deviceProfile_object.getData()
        resp = requests.post(url=url, headers=self.API_HEADERS, json=deviceProfile_data)
        print(deviceProfile_data)
        print(resp.text)
        return resp

    def post_deviceInfo(self, deviceInfo_object):
        url = self.API_HOST + 'device'
        deviceInfo_data = deviceInfo_object.getData()
        resp = requests.post(url=url, headers=self.API_HEADERS, json=deviceInfo_data)
        print(deviceInfo_data)
        print(resp.text)
        return resp
