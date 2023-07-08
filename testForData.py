from controller import DBcontroller

db = DBcontroller.Database()
df = db.select('usermessage')   # 调用查询方法获取数据（返回一个DataFrame）
print(df)

column_name1 = 'user_name'
column_name2 = 'user_password'
search_value = 'admin'

mask = df['user_name'].isin([search_value])

if mask.any():
    # 获取目标行的密码
    password = df.loc[mask, 'user_password'].values[0]
    print(f"找到用户名为'{search_value}'，对应的密码为'{password}'")
else:
    print("未找到用户名")

# new_df = df.loc[:, ['start_location_x', 'start_location_y']]
# tmp_df = df.loc[:, ['orderid']]
# print(new_df)
# data = df.to_dict(orient='records')
# print(data)