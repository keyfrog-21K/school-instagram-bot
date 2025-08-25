# image_generator.py
from PIL import Image, ImageDraw, ImageFont

class drawTextOnBackground:
    def __init__(self, background_path, font_path, title, body_lines):
        self.img = Image.open(background_path).convert("RGBA")
        self.W, self.H = self.img.size
        self.draw = ImageDraw.Draw(self.img)

        # 제목 / 본문 폰트
        self.title_font = ImageFont.truetype(font_path, 80)
        self.body_font = ImageFont.truetype(font_path, 50)  # 본문 글자 조금 더 크게

        self.title = title
        self.body_lines = body_lines
        self.fill_color = "black"  # 글자 색상 통일
        self.line_spacing = 60     # 본문 줄간격
        self.title_body_spacing = 50  # 제목과 본문 사이 간격

    def draw_centered_text(self, text, y, font):
        """가로 중앙 정렬 텍스트 그리기"""
        bbox = self.draw.textbbox((0, 0), text, font=font)
        width = bbox[2] - bbox[0]
        self.draw.text(((self.W - width) / 2, y), text, font=font, fill=self.fill_color)

    def render(self, output_path="output.jpeg"):
        # 제목 높이 계산
        title_bbox = self.draw.textbbox((0, 0), self.title, font=self.title_font)
        title_height = title_bbox[3] - title_bbox[1]

        # 본문 전체 높이 계산
        body_heights = sum([self.draw.textbbox((0, 0), line, font=self.body_font)[3] -
                            self.draw.textbbox((0, 0), line, font=self.body_font)[1]
                            for line in self.body_lines])
        total_body_height = body_heights + (len(self.body_lines)-1) * self.line_spacing

        # 전체 텍스트 높이
        total_text_height = title_height + self.title_body_spacing + total_body_height

        # 상하 중앙 기준 y 시작 위치
        start_y = (self.H - total_text_height) / 2

        # 제목 그리기
        self.draw_centered_text(self.title, start_y, self.title_font)

        # 본문 그리기
        current_y = start_y + title_height + self.title_body_spacing
        for line in self.body_lines:
            self.draw_centered_text(line, current_y, self.body_font)
            line_bbox = self.draw.textbbox((0,0), line, font=self.body_font)
            line_height = line_bbox[3] - line_bbox[1]
            current_y += line_height + self.line_spacing

        # 이미지 저장
        rgb_img = self.img.convert("RGB")
        rgb_img.save(output_path, "JPEG")
