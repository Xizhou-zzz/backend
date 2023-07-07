from controller import DBcontroller

db = DBcontroller.Database()
df = db.select('bikemessage', condition='bikeid = 288841')   # 调用查询方法获取数据（返回一个DataFrame）
print(df)
new_df = df.loc[:, ['start_location_x', 'start_location_y']]
print(new_df)
data = new_df.to_dict(orient='records')
print(data)