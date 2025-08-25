# main.py
from getapi import Parser
from datetime import datetime


def main():
    officeCode = 'R10' # 경상북도교육청
    schoolCode = '8801139' # 구미중학교
    today = datetime.today().strftime("%Y%m%d")

    parser = Parser(officeCode, schoolCode, today)
    json = parser.get_data()

    row = json["mealServiceDietInfo"][1]["row"][0]
    dish_raw = row["DDISH_NM"]
    meals = [dish.strip() for dish in dish_raw.split("<br/>") if dish.strip()]
