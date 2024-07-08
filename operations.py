from tables import *
from database import DBSession
# from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
from langchain_experimental.sql import SQLDatabaseChain
from langchain.sql_database import SQLDatabase
from langchain_community.llms import OpenAI


class DatabaseOperations:
    def __init__(self):
        # 创建session
        self.session = DBSession()
        # 连接OpenAI
        self.db_uri = 'mysql+pymysql://root:yjy%402001@localhost:3306/military_demo'
        self.db = SQLDatabase.from_uri(self.db_uri)
        self.llm = OpenAI(temperature=0, verbose=True)
        self.db_chain = SQLDatabaseChain.from_llm(self.llm, self.db, verbose=True)

    def add_device(self, device_id, name, max_flight_weight, manufacturer):
        new_device = Device(id=device_id, name=name, max_flight_weight=max_flight_weight, manufacturer=manufacturer)
        self.session.add(new_device)
        self.session.commit()

    def query_devices(self):
        devices = self.session.query(Device).all()
        for device in devices:
            print(f'ID: {device.id}, Name: {device.name}, Max Flight Weight: {device.max_flight_weight}, Manufacturer: {device.manufacturer}')

    def close_session(self):
        self.session.close()

    def run_query(self, query):
        return self.db_chain.run(query)