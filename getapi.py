# getapi.py
# API를 불러오는 코드
import os
import dotenv
import requests

dotenv.load_dotenv()
api_key = os.getenv('NEIS_APIKEY')


class Parser:
    def __init__(self, officeCode, schoolCode, ymd):
        self.officeCode = officeCode
        self.schoolCode = schoolCode
        self.ymd = ymd
        self.url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
        self.params = {
            'KEY': api_key,
            'Type': 'json',
            'ATPT_OFCDC_SC_CODE': self.officeCode,
            'SD_SCHUL_CODE': self.schoolCode,
            'MLSV_YMD': self.ymd,
            'pSize': 1,
            'pIndex': 1
        }

    def get_data(self):
        response = requests.get(self.url, params=self.params)
        return response.json()
