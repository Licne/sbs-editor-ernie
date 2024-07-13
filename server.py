from app import app
import argparse
from dotenv import load_dotenv
import os
# 引入环境设置变量
import config
# 设置命令行参数解析
parser = argparse.ArgumentParser(description="环境设置")
parser.add_argument('--env', type=str, help='dev or prod default = dev')
args = parser.parse_args()

# 根据命令行参数加载不同的 .env 文件
env_file = args.env if args.env else 'prod'

if env_file == 'prod':
    load_dotenv('.env.production')
elif env_file == 'dev':
    load_dotenv('.env.development')
else:
    load_dotenv(env_file)

# config 设置
config.HOST = os.getenv('HOST', '0.0.0.0')
config.PORT = os.getenv('PORT', '8080')
config.EB_AGENT_ACCESS_TOKEN = os.getenv('EB_AGENT_ACCESS_TOKEN', None)
config.SBS_OCR_API_URL = os.getenv('SBS_OCR_API_URL', None)
# 环境设置
HOST = os.getenv('HOST', '0.0.0.0')
PORT = os.getenv('PORT', 1145)
EB_AGENT_ACCESS_TOKEN = os.getenv('EB_AGENT_ACCESS_TOKEN', None)
os.environ["EB_AGENT_ACCESS_TOKEN"] = str(EB_AGENT_ACCESS_TOKEN)

if __name__ == '__main__':
    print('当前模式为:', env_file, 'HOST:', HOST, 'PORT:', PORT)
    app.run(host=HOST, port=PORT)
