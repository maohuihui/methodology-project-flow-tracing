from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import DevelopmentConfig, ProductionConfig
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=DevelopmentConfig):
    load_dotenv()  # 加载 .env 文件中的环境变量

    app = Flask(__name__)

    # 使用配置文件中的设置
    app.config.from_object(config_class)

    #初始化配置
    # 初始化数据库和迁移工具
    db.init_app(app)
    migrate.init_app(app, db)

    CORS(app)  # 启用跨域支持

    # 导入并注册蓝图
    from .routes import main
    app.register_blueprint(main)

    return app
