from flask import jsonify, request
import os
import json
import asyncio
import erniebot
from erniebot_agent.chat_models import ERNIEBot
from erniebot_agent.memory import HumanMessage, AIMessage, SystemMessage, FunctionMessage

# 数据处理
async def handle_data(json_data):
    print(json_data)
    ai_res_data = {
        'content': json_data['content']
    }

    ai_req_data = await ai_polish(ai_res_data)

    return ai_req_data

# ai润色功能模块
async def ai_polish(res_data):
    # 选择模型
    model = ERNIEBot(model="ernie-3.5")
    # 系统预设
    system_message = SystemMessage('''
        将提供的文档进行润色处理，
        要求:
        1.保证文章核心内容不变，
        2.使语句更加流畅通顺,
        3.使用markdown格式并进行格式优化,
        4.如果用户提供的内容少于20字则拒绝优化并回复"内容过短，请重新输入" 
        ''')

    # 用户文档输入
    document_input = res_data['content']
    # Message模块
    messages = [
        HumanMessage(document_input),
    ]
    ai_message = await model.chat(messages=messages, system=system_message.content)
    print(ai_message)

    req_data = {
        'content':ai_message.content
    }

    return req_data