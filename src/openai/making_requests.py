import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

client = OpenAI(base_url="https://models.inference.ai.azure.com",
                api_key=GITHUB_TOKEN)

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

以上是活動說明，請問有哪些人參加？
"""

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
#                 '參加本次創意短片挑戰賽的有五位參加者，分別是：\n\n1. 張宇\n2. 李華\n3. 王娜\n4. 陳俊\n5. 林怡',
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
#         completion_tokens=49,
#         prompt_tokens=258,
#         total_tokens=307,
#         completion_tokens_details=None,
#         prompt_tokens_details=None,
#     ),
# )

print(f"{response.choices[0].message.content = }")
print()

# response.choices[0].message.content =
# '參加本次創意短片挑戰賽的有五位參加者，分別是：\n\n1. 張宇\n2. 李華\n3. 王娜\n4. 陳俊\n5. 林怡'