from flask import jsonify, request, Flask
import nest_asyncio
from flask_cors import CORS

from models import articleHandle
from models import sbsOCR
from models import mindMap
# 解决事件循环
nest_asyncio.apply()
# 创建实例
app = Flask(__name__)
# 跨域问题解决
CORS(app)


#################################
# 连接性测试接口
#################################

# 首页
@app.route('/')
def home():
    print("连通性测试")
    return '瞬爆闪AI编辑器,好耶！'


##################################
# 功能api
##################################

# 文章润色
@app.route('/api/article_polish', methods=['POST'])
async def article_polish():
    # 读取数据
    print('文章润色请求')
    json_data = request.get_json()
    data = await articleHandle.handle_data(json_data, 'article_polish')
    return jsonify(data)


# 摘要提取
@app.route('/api/summary_generation', methods=['POST'])
async def summary_generation():
    print('摘要提取请求')
    json_data = request.get_json()
    data = await articleHandle.handle_data(json_data, 'summary_generation')
    return jsonify(data)

# 文章续写
@app.route('/api/continue_writing', methods=['POST'])
async def continue_writing():
    print('文章续写请求')
    json_data = request.get_json()
    data = await articleHandle.handle_data(json_data, 'continue_writing')
    return jsonify(data)

@app.route('/api/intelligent_typeset', methods=['POST'])
async def intelligent_typeset():
    print('排版优化请求')
    json_data = request.get_json()
    data = await articleHandle.handle_data(json_data, 'intelligent_typeset')
    return jsonify(data)

# ocr识别
@app.route('/api/sbs_ocr', methods=['POST'])
async def sbs_ocr():
    print('ocr识别请求')
    json_data = request.get_json()
    data = await sbsOCR.handle_data(json_data)
    return jsonify(data)

# 思维导图
@app.route('/api/mind_map', methods=['POST'])
async def mind_map():
    print('思维导图请求')
    json_data = request.get_json()
    data = await mindMap.handle_data(json_data)
    return jsonify(data)

##################################
# 内部测试接口
##################################
# ocr本地测试接口
@app.route('/api/sbs_ocr_local', methods=['POST'])
async def sbs_ocr_local():
    print("内部ocr测试接口调用")
    json_data = request.get_json()
    if json_data['password'] == 'adminLicne':
        await sbsOCR.local_picToBase64()
        return 'ok'
    return 'error password'
