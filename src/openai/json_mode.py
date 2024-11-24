from typing import List
from pydantic import BaseModel, Field
import json
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


PROMPT = f"""
You are a helpful AI assistant.
The JSON object must use the schema: {json.dumps(Event.model_json_schema(), indent=2)}
使用臺灣繁體中文回答。
"""
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

print(f"{json.dumps(Event.model_json_schema(), indent=2)}")
print()

# {
#     "$defs": {
#         "Person": {
#             "properties": {
#                 "name": {
#                     "description": "\u59d3\u540d",
#                     "title": "Name",
#                     "type": "string"
#                 }
#             },
#             "required": ["name"],
#             "title": "Person",
#             "type": "object"
#         }
#     },
#     "properties": {
#         "name": {
#             "description": "\u6d3b\u52d5\u540d\u7a31",
#             "title": "Name",
#             "type": "string"
#         },
#         "time": {
#             "description": "\u6642\u9593",
#             "title": "Time",
#             "type": "string"
#         },
#         "place": {
#             "description": "\u5730\u9ede",
#             "title": "Place",
#             "type": "string"
#         },
#         "people": {
#             "description": "\u53c3\u52a0\u8005",
#             "items": {
#                 "$ref": "#/$defs/Person"
#             },
#             "title": "People",
#             "type": "array"
#         },
#         "summary": {
#             "description": "\u6d3b\u52d5\u4ecb\u7d39\u6458\u8981",
#             "title": "Summary",
#             "type": "string"
#         }
#     },
#     "required": ["name", "time", "place", "people", "summary"],
#     "title": "Event",
#     "type": "object"
# }

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": PROMPT,
        },
        {
            "role": "user",
            "content": QUERY,
        },
    ],
    #
    model="gpt-4o-mini",
    #
    response_format={"type": "json_object"},
    temperature=1,
    max_tokens=1024,
    top_p=1,
)

print(f"{response = }")
print()

# response = ChatCompletion(
#     id='chatcmpl-...',
#     choices=[
#         Choice(
#             finish_reason='stop',
#             index=0,
#             logprobs=None,
#             message=ChatCompletionMessage(
#                 content=
#                 '{\n  "name": "創意短片挑戰賽",\n  "time": "2024年12月20日（星期五） 下午 1:00 - 4:00",\n  "place": "市文化中心 多功能廳",\n  "people": [\n    {\n      "name": "張宇"\n    },\n    {\n      "name": "李華"\n    },\n    {\n      "name": "王娜"\n    },\n    {\n      "name": "陳俊"\n    },\n    {\n      "name": "林怡"\n    }\n  ],\n  "summary": "本次創意短片挑戰賽邀請五位參加者，挑戰在三小時內拍攝並剪輯一部短片。每位參加者需根據指定主題，運用各種創意元素，創作一部富有故事性的短片。參賽者將自行分組，並利用現場提供的設備進行拍攝。活動結束後，所有短片將進行播放並評選出最佳影片，獲得獎品及證書。此活動旨在提升參加者的創意思維、合作精神及影像製作能力，並鼓勵大家分享自己的創作成果。"\n}',
#                 refusal=None,
#                 role='assistant',
#                 audio=None,
#                 function_call=None,
#                 tool_calls=None,
#             ),
#         )
#     ],
#     created=0,
#     model='gpt-4o-mini',
#     object='chat.completion',
#     service_tier=None,
#     system_fingerprint='fp_...',
#     usage=CompletionUsage(
#         completion_tokens=279,
#         prompt_tokens=598,
#         total_tokens=877,
#         completion_tokens_details=None,
#         prompt_tokens_details=None,
#     ),
# )

content = response.choices[0].message.content

print(f"{content = }")
print()

# content = '{\n  "name": "創意短片挑戰賽",\n  "time": "2024年12月20日（星期五） 下午 1:00 - 4:00",\n  "place": "市文化中心 多功能廳",\n  "people": [\n    {\n      "name": "張宇"\n    },\n    {\n      "name": "李華"\n    },\n    {\n      "name": "王娜"\n    },\n    {\n      "name": "陳俊"\n    },\n    {\n      "name": "林怡"\n    }\n  ],\n  "summary": "本次創意短片挑戰賽邀請五位參加者，挑戰在三小時內拍攝並剪輯一部短片。每位參加者需根據指定主題，運用各種創意元素，創作一部富有故事性的短片。參賽者將自行分組，並利用現場提供的設備進行拍攝。活動結束後，所有短片將進行播放並評選出最佳影片，獲得獎品及證書。此活動旨在提升參加者的創意思維、合作精神及影像製作能力，並鼓勵大家分享自己的創作成果。"\n}'

content_json = Event.model_validate_json(content)

print(f"{content_json = }")
print()

# content_json = Event(
#     name='創意短片挑戰賽',
#     time='2024年12月20日（星期五） 下午 1:00 - 4:00',
#     place='市文化中心 多功能廳',
#     people=[
#         Person(name='張宇'),
#         Person(name='李華'),
#         Person(name='王娜'),
#         Person(name='陳俊'),
#         Person(name='林怡')
#     ],
#     summary=
#     '本次創意短片挑戰賽邀請五位參加者，挑戰在三小時內拍攝並剪輯一部短片。每位參加者需根據指定主題，運用各種創意元素，創作一部富有故事性的短片。參賽者將自行分組，並利用現場提供的設備進行拍攝。活動結束後，所有短片將進行播放並評選出最佳影片，獲得獎品及證書。此活動旨在提升參加者的創意思維、合作精神及影像製作能力，並鼓勵大家分享自己的創作成果。'
# )
