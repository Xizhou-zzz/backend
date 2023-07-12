from controller import DBcontroller
from LSTM import lstm

data_date = '2015/7/1'

db = DBcontroller.Database()
df = db.select('predict', condition=f'date = { data_date }')

data_to_draw = lstm.get_predictions(df)

print(data_to_draw)
# return jsonify(data_to_draw)




























# db = DBcontroller.Database()
# df = db.select('bikemessage', condition='userid < 10000 and userid > 9900')   # 调用查询方法获取数据（返回一个DataFrame）
# # new_df = new_df.rename(columns={'orderid': 'name', 'userid': 'value'})
# df['start_time'] = pd.to_datetime(df['start_time'])
# df['hour'] = df['start_time'].dt.hour
# # 创建时间段的标签
# time_labels = ['0:00-0:59', '1:00-1:59', '2:00-2:59', '3:00-3:59', '4:00-4:59', '5:00-5:59', '6:00-6:59', '7:00-7:59',
#                '8:00-8:59', '9:00-9:59', '10:00-10:59', '11:00-11:59', '12:00-12:59', '13:00-13:59', '14:00-14:59',
#                '15:00-15:59', '16:00-16:59', '17:00-17:59', '18:00-18:59', '19:00-19:59', '20:00-20:59', '21:00-21:59',
#                '22:00-22:59', '23:00-23:59']
#
# # 使用cut()函数对时间进行分段，并计算每个时段的数量
# time_count = pd.cut(df['hour'], bins=range(0, 25), labels=time_labels, include_lowest=True).value_counts().sort_index().reset_index()
# time_count.columns = ['time_range', 'count']
# # 将结果保存为DataFrame数据流
# time_count_stream = time_count.to_json(orient='records')
#
# # 打印结果
# print(time_count)
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