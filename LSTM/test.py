
import numpy as np
import pandas as pd
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import ModelCheckpoint

#def denormalize_data(predictions, min_val, max_val):

t1_max = 34.0
t2_max = 34.0
hum_max = 100.0
wind_speed_max = 56.50
hour_max = 24
t1_min = -1.50
t2_min = -6.0
hum_min = 20.5
wind_speed_min = 0.0
hour_min = 0.0
max_val = 7860
min_val = 0

test = pd.read_csv('test.csv')


print(test)
# # 假设您要将第2列乘以2，第4列乘以3
# columns_to_multiply = ['t1', 't2', 'hum', 'wind_speed', 'hour']
# multipliers = [t1_max-t1_min, t2_max-t2_min, hum_max-hum_min, wind_speed_max-wind_speed_min, hour_max-hour_min]
# multipliers1 = [t1_min, t2_min, hum_min, wind_speed_min, hour_min]
#
# for col, multiplier, multiplier1 in zip(columns_to_multiply, multipliers, multipliers1):
#     test[col] = (test[col] - multiplier1 )/multiplier
#
# #创建一个新的模型对象
# model = Sequential([
#     LSTM(units=256, input_shape=(1, 9), return_sequences=True),
#     Dropout(0.4),
#     LSTM(units=256, return_sequences=True),
#     Dropout(0.3),
#     LSTM(units=128, return_sequences=True),
#     LSTM(units=32),
#     Dense(1)
# ])
# model.compile(optimizer='adam', loss='mse')
#
# 加载训练过程中保存的最佳模型权重
# model.load_weights('best_model.hdf5')
#
#
# features = []
#
# for i in range(0, len(test) , 1):
#     data = test.iloc[i:i+1]
#     features.append(data)
#
# test = np.array(features)
#
# test_preds = model.predict(test,verbose =1)
#
# test_preds = test_preds*(max_val-min_val)*0.8
#
# print(test_preds)
