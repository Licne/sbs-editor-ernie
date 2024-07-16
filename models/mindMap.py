from models.articleHandle import ai_handle
import json

async def handle_data(json_data):
    # print(json_data)
    ai_res_data = {
        'content': json_data['content'],
        'ai_type': 'mind_map_step1'
    }

    data_step1 = await ai_handle(ai_res_data)

    ai_res_data = {
        'content': data_step1['content'],
        'ai_type': 'mind_map_step2'
    }

    print('思维导图请求-step1-finished')

    # if  ai_res_data['content'] == 'none structure':
    #     return {
    #         'content':'none structure'
    #     }
    #
    # data_step2 = await ai_handle(ai_res_data)
    #
    # ai_req_data = {
    #     'content':  data_step2['content'],
    #     'markdown': data_step1['content']
    # }

    json_template = markdown_to_json(data_step1['content'])
    ai_req_data = {
        'content': json_template,
        'markdown':data_step1['markdown'],
    }
    # print(json.dumps(json_template, ensure_ascii=False, indent=2))

    return ai_req_data


def markdown_to_json(markdown):
    lines = markdown.split('\n')
    stack = []
    root = []
    current = root

    for line in lines:
        if line.startswith('# '):
            current = {"data": line[2:], "children": []}
            root.append(current)
            stack = [current]
        elif line.startswith('## '):
            current = {"data": line[3:], "children": []}
            stack[0]["children"].append(current)
            stack = [stack[0], current]
        elif line.startswith('### '):
            current = {"data": line[4:], "children": []}
            stack[1]["children"].append(current)
            stack = [stack[0], stack[1], current]
        elif line.startswith('#### '):
            current = {"data": line[5:], "children": []}
            stack[2]["children"].append(current)
            stack = [stack[0], stack[1], stack[2], current]
        elif line.startswith('- '):
            current = {"data": line[2:], "children": []}
            stack[-1]["children"].append(current)
        elif line.startswith('1. ') or line.startswith('2. '):
            current = {"data": line[3:], "children": []}
            stack[-1]["children"].append(current)

    return root