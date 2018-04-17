# coding:utf-8
# 程序入口

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_script import Manager

class Config(object):
    """配置参数"""
    DEBUG=True
    # 配置mysql数据库：真实开发不写127,
    SQLALCHEMY_DATABASE_URI="mysql://root:mysql@127.0.0.1:3306/iHome_gz"
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    # 配置redis数据库：真实开发填写redis数据库的真实IP
    REDIS_HOST='127.0.0.1'
    REDIS_PORT=6379

app=Flask(__name__)

# 加载配置参数
app.config.from_object(Config)

# 创建连接到数据库的对象
db=SQLAlchemy(app)

# 创建连接到redis数据库的对象
redis_store=redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)


# 创建脚本管理器对象
manager=Manager(app)
@app.route('/index')
def index():
    redis_store.set('name','zry')
    return "index"


if __name__ == '__main__':
    manager.run()