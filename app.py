from flask import jsonify, request, Flask
import nest_asyncio
from flask_cors import CORS

from models import articlePolish

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

