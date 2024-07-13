import requests
import pathlib
import pprint
import os
import base64
import config

# 数据处理 提取
async def handle_data(json_data):
    ai_res_data = {
        "image": json_data['image']
    }

    ai_req_data = await ai_sbs_ocr(ai_res_data)

    return ai_req_data

# OCR调用远程
async def ai_sbs_ocr(res_data):
    # 请求头设置
    headers = {
        "Authorization": f"token {config.EB_AGENT_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    resp = requests.post(url=config.SBS_OCR_API_URL, json=res_data, headers=headers)

    print(resp.status_code)
    ocr_result = resp.json()["result"]
    # ocr_status_code = resp.status_code
    print(ocr_result["texts"])

    req_data = {
        'image': ocr_result["image"],
        'texts': ocr_result["texts"]
    }
    return req_data

# 测试接口
async def local_picToBase64():
    image_path = "./testFiles/pic/sb_zb.jpg"
    image_bytes = pathlib.Path(image_path).read_bytes()
    image_base64 = base64.b64encode(image_bytes).decode('ascii')

    json_data = {
        "image": image_base64
    }

    result = await handle_data(json_data)

    output_image_path = "./testFiles/opt/output.jpg"
    with open(output_image_path, "wb") as f:
        f.write(base64.b64decode(result['image']))
    print(f"OCR结果图保存在 {output_image_path}")
    print("\n文本信息:")
    pprint.pp(result["texts"])
    # print(result)

