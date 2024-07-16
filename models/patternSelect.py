# 摘要提取
summary_generation_prompts = '''
## 功能要求:
主要: 作为文章处理中的学术研究系统，生成这篇文章的摘要。
附加:
1. 字数控制在300-500之间，可适当超出字数。
2. 确保总结对一般读者友好，同时保留原文的核心见解和细节。
3. 关注句子结构、词汇选择和连贯性，确保与文章的整体叙述一致。
4. 确保摘要清晰、连贯，同时遵循学术领域的具体指南和惯例。
'''
# 文章续写
continue_writing_prompts = '''
## 功能要求:
主要: 作为文章处理中的续写系统，对文章进行续写。
附加: 
1. 字数控制在500-1000之间。
2. 只输出续写的内容。
'''

# 内容润色
article_polish_prompts = '''
## 功能要求:
主要: 作为文章处理中的专业润色系统，对文章进行润色。
附加: 
- 保证文章核心思想不变，语言风格符合文章的体裁和文风。
- 进行的语法和句法审查，确保所有时态、语态、主谓一致性、从句结构等语法要素准确无误，以及标点符号的规范性。
- 去除冗余表达，避免使用非正式或模糊的语言。使用恰当的标点符号来强调关键信息。
- 找出并修正所有拼写、语法、标点及格式错误。
- 对文章中的关键描述性段落进行深入润色，增加精确的细节和清晰的解释。
'''

# 排版优化
intelligent_typeset_prompts = '''
## 功能要求:
主要: 使用markdown语法对文章进行智能排版。
附加: 
1. 不要修改任何文章内容，只进行排版。
2. 识别并优化文章标题与段落。
3. 识别并优化列表与引用。
4. 识别并优化代码与图片。
5. 识别并优化表格。
6. 识别并优化内联格式标题。
7. 适当使用加粗文本，斜体文本，删除线文本。
8. 识别并优化链接。
'''

mind_map_step1_prompts = '''

## 功能要求:
主要: 提取文章主要内容信息，生成markdown格式思维导图。
附加:
1. 最多到四级标题。
2. 如果文章不存在结构性，直接输出"none structure"。
3. 以下为示例

# {一级标题}
## {二级标题}
### {三级标题}
- {无序列表}
- {无序列表}
### {三级标题}
#### {四级标题}
- {无序列表}
- {无序列表}
## 二级标题
### {三级标题}
#### {四级标题}
1. {有序列表}
2. {有序列表}

'''
# 功能废弃 效率过低
mind_map_step2_prompts = '''
## 功能要求:
主要: 将markdown格式思维导图转换为json格式，请只输出json格式结果，绝对不要包含任何其他多余文字
以下为示例:

输入:

# {一级标题}
## {二级标题}
### {三级标题}
- {无序列表}
- {无序列表}
### {三级标题}
#### {四级标题}
- {无序列表}
- {无序列表}
## 二级标题
### {三级标题}
#### {四级标题}
1. {有序列表}
2. {有序列表}

输出:


  {
    "data": "{一级标题}",
    "children": [
      {
        "data": "{二级标题}",
        "children": [
          {
            "data": "{三级标题}",
            "children": [
              {
                "data": "{无序列表}",
                "children": []
              },
              {
                "data": "{无序列表}",
                "children": []
              }
            ]
          },
          {
            "data": "{三级标题}",
            "children": [
              {
                "data": "{四级标题}",
                "children": [
                  {
                    "data": "{无序列表}",
                    "children": []
                  },
                  {
                    "data": "{无序列表}",
                    "children": []
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "data": "二级标题",
        "children": [
          {
            "data": "{三级标题}",
            "children": [
              {
                "data": "{四级标题}",
                "children": [
                  {
                    "data": "{有序列表}",
                    "children": []
                  },
                  {
                    "data": "{有序列表}",
                    "children": []
                  }
                ]
              }
            ]
          }
        ]
      }
    ]
  }


'''

# 取得功能提示词
def get_func_prompts(ai_type):
    if ai_type == 'article_polish':
        return article_polish_prompts
    elif ai_type == 'summary_generation':
        return summary_generation_prompts
    elif ai_type == 'continue_writing':
        return continue_writing_prompts
    elif ai_type == 'intelligent_typeset':
        return intelligent_typeset_prompts
    elif ai_type == 'mind_map_step1':
        return mind_map_step1_prompts
    elif ai_type == 'mind_map_step2':
        return mind_map_step2_prompts
    else:
        return None
