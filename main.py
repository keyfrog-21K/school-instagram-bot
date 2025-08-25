# main.py
from getapi import Parser
from image_generator import drawTextOnBackground
from datetime import datetime


def main():
    officeCode = 'R10' # 경상북도교육청
    schoolCode = '8801139' # 구미중학교
    background_path = './src/background.png'
    font_path = './src/WantedSans-SemiBold.ttf'

    today = datetime.today()

    parser = Parser(officeCode, schoolCode, today.strftime("%Y%m%d"))
    json = parser.get_data()

    row = json["mealServiceDietInfo"][1]["row"][0]
    dish_raw = row["DDISH_NM"]
    meals = [dish.strip() for dish in dish_raw.split("<br/>") if dish.strip()]

    draw = drawTextOnBackground(background_path, font_path, today.strftime("%Y년 %m월 %d일"), meals)
    draw.render()

if __name__ == '__main__':
    main()