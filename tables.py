# models.py
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义Device对象
class Device(Base):
    # 表名
    __tablename__ = 'device'

    # 表的结构
    id = Column(String(50), primary_key=True)
    name = Column(String(50))
    max_flight_weight = Column(Float)
    manufacturer = Column(String(50))


# 指定模块的公共接口
__all__ = ['Device', 'Base']
