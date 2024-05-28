from app import app
import argparse
from dotenv import load_dotenv
import os

# 设置命令行参数解析
parser = argparse.ArgumentParser(description="环境设置")
parser.add_argument('--env', type=str, help='dev or prod default = dev')
args = parser.parse_args()

# 根据命令行参数加载不同的 .env 文件
env_file = args.env if args.env else 'dev'

if env_file == 'prod':
    load_dotenv('.env.production')
elif env_file == 'dev':
    load_dotenv(env_file)
else:
    load_dotenv(env_file)

# 环境设置
HOST = os.getenv('HOST', '0.0.0.0')
PORT = os.getenv('PORT', 1145)
EB_AGENT_ACCESS_TOKEN = os.getenv('EB_AGENT_ACCESS_TOKEN', None)

os.environ["EB_AGENT_ACCESS_TOKEN"] = str(EB_AGENT_ACCESS_TOKEN)

if __name__ == '__main__':
    print('当前模式为:', env_file, 'HOST:', HOST, 'PORT:', PORT)
    app.run(host=HOST, port=PORT)
