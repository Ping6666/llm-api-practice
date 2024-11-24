"""
ref
1. https://platform.openai.com/docs/guides/structured-outputs
"""

from typing import List
from pydantic import BaseModel, Field
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

client = OpenAI(base_url="https://models.inference.ai.azure.com",
                api_key=GITHUB_TOKEN)


class Person(BaseModel):
    name: str = Field(description="姓名")


class Event(BaseModel):
    name: str = Field(description="活動名稱")
    time: str = Field(description="時間")
    place: str = Field(description="地點")
    people: List[Person] = Field(description="參加者")
    summary: str = Field(description="活動介紹摘要")


PROMPT = "You are a helpful AI assistant. 使用臺灣繁體中文回答。"
QUERY = """
活動名稱：創意短片挑戰賽

時間：2024年12月20日（星期五） 下午 1:00 - 4:00
地點：市文化中心 多功能廳

活動人物：
張宇
李華
王娜
陳俊
林怡

活動介紹：
本次創意短片挑戰賽邀請五位參加者，挑戰在三小時內拍攝並剪輯一部短片。
每位參加者需根據指定主題，運用各種創意元素，創作一部富有故事性的短片。
參賽者將自行分組，並利用現場提供的設備進行拍攝。
活動結束後，所有短片將進行播放並評選出最佳影片，獲得獎品及證書。
此活動旨在提升參加者的創意思維、合作精神及影像製作能力，並鼓勵大家分享自己的創作成果。
"""

completion = client.beta.chat.completions.parse(
    messages=[
        {
            "role": "system",
            "content": PROMPT
        },
        {
            "role": "user",
            "content": QUERY
        },
    ],
    # model="gpt-4o",
    model="gpt-4o-mini",
    # model="gpt-4o-mini-2024-07-18",
    response_format=Event,
)

print(f"{completion = }")
print()

print(f"{completion.choices[0].message.parsed = }")
print()
