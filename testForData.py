from controller import DBcontroller
import pandas as pd

db = DBcontroller.Database()
df = db.select('bikemessage', condition='userid < 10000 and userid > 9900')   # 调用查询方法获取数据（返回一个DataFrame）
# new_df = new_df.rename(columns={'orderid': 'name', 'userid': 'value'})
df['start_time'] = pd.to_datetime(df['start_time'])
df['weekday'] = df['start_time'].dt.weekday
# 按星期几分组并计算每个组的数量
weekday_count = df.groupby('weekday').size().reset_index(name='count')
# 将结果保存为DataFrame数据流
weekday_count_stream = weekday_count.to_json(orient='records')
weekday_mapping = {
    0: 'Mon',
    1: 'Tue',
    2: 'Wed',
    3: 'Thu',
    4: 'Fri',
    5: 'Sat',
    6: 'Sun'
}
# 将 'weekday' 列的值替换为星期的缩写
weekday_count['weekday'] = weekday_count['weekday'].replace(weekday_mapping)
# 打印结果
print(weekday_count)
print(weekday_count_stream)
# print(data)












#
# db = DBcontroller.Database()
# df = db.select('usermessage')   # 调用查询方法获取数据（返回一个DataFrame）
# print(df)
#
# column_name1 = 'user_name'
# column_name2 = 'user_password'
# search_value = 'admin'
#
# mask = df['user_name'].isin([search_value])
#
# if mask.any():
#     # 获取目标行的密码
#     password = df.loc[mask, 'user_password'].values[0]
#     print(f"找到用户名为'{search_value}'，对应的密码为'{password}'")
# else:
#     print("未找到用户名")

# new_df = df.loc[:, ['start_location_x', 'start_location_y']]
# tmp_df = df.loc[:, ['orderid']]
# print(new_df)
# data = df.to_dict(orient='records')
# print(data)