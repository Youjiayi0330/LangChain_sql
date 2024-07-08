from operations import DatabaseOperations


def main():
    db_ops = DatabaseOperations()
    db_ops.query_devices()
    while(1==1):
        text_query = input("请输入查询语句：")
        result = db_ops.run_query(text_query)
        print(f"回答：{result}")


if __name__ == '__main__':
    main()


