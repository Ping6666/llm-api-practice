import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
GROQ_TOKEN = os.getenv("GROQ_TOKEN")

client = Groq(api_key=GROQ_TOKEN)

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

completion = client.chat.completions.create(
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
    model="llama3-8b-8192",
    #
    temperature=1,
    max_tokens=1024,
    top_p=1,
    #
    stream=True,
    stop=None,
)

print(f"{completion = }")
print()

# completion = <groq.Stream object at 0x7f3a9057fbe0>

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
print()
print()

# 根據活動介紹，以下五人參加創意短片挑戰賽：

# 1. 張宇
# 2. 李華
# 3. 王娜
# 4. 陳俊
# 5. 林怡
