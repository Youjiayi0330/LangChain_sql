# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import Base

# 初始化数据库连接
engine = create_engine('mysql+pymysql://root:yjy%402001@localhost:3306/military_demo')

# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 创建所有表
Base.metadata.create_all(engine)
