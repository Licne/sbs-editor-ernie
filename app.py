from flask import jsonify, request, Flask
import nest_asyncio
from flask_cors import CORS

from models import articlePolish
from models import sbsOCR

# 解决事件循环
nest_asyncio.apply()
# 创建实例
app = Flask(__name__)
# 跨域问题解决
CORS(app)

##############################

# 首页
@app.route('/')
def home():
    return '瞬爆闪AI编辑器,好耶！'


# ai基础润色
@app.route('/api/article_polish', methods=['POST'])
async def article_polish():
    # 读取数据
    json_data = request.get_json()
    data = await articlePolish.handle_data(json_data)
    print('ai润色请求成功')
    return jsonify(data)

# ocr识别
@app.route('/api/sbs_ocr', methods=['POST'])
async def sbs_ocr():
    json_data = request.get_json()
    data = await sbsOCR.handle_data(json_data)
    print('ocr识别成功')
    return jsonify(data)

# ocr本地测试接口
@app.route('/api/sbs_ocr_local', methods=['POST'])
async def sbs_ocr_local():
    print("in")
    json_data = request.get_json()
    if json_data['password'] == 'adminLicne':
        await sbsOCR.local_picToBase64()
        return 'ok'
    return 'error password'
