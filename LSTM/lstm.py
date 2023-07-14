import numpy as np
import pandas as pd
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import ModelCheckpoint

# 构建与训练模型的代码

# 创建一个新的模型对象
model = Sequential([
    LSTM(units=256, input_shape=(1, 9), return_sequences=True),
    Dropout(0.4),
    LSTM(units=256, return_sequences=True),
    Dropout(0.3),
    LSTM(units=128, return_sequences=True),
    LSTM(units=32),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')

# 加载训练过程中保存的最佳模型权重
model.load_weights('best_model.hdf5')


def preprocess_data(t1, t2, hum, wind_speed, weather_code, is_holiday, is_weekend, season, hour):
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

    # # 创建一个DataFrame来存储输入数据
    df = pd.DataFrame(columns=['t1', 't2', 'hum', 'wind_speed', 'weather_code', 'is_holiday', 'is_weekend', 'season', 'hour'])

    # 将输入数据转换为归一化形式并添加到DataFrame中
    new_row = {'t1': (float(t1) - t1_min) / (t1_max - t1_min),
               't2': (float(t2) - t2_min) / (t2_max - t2_min),
               'hum': (float(hum) - hum_min) / (hum_max - hum_min),
               'wind_speed': (float(wind_speed) - wind_speed_min) / (wind_speed_max - wind_speed_min),
               'weather_code': weather_code,
               'is_holiday': is_holiday,
               'is_weekend': is_weekend,
               'season': season,
               'hour': (float(hour) - hour_min) / (hour_max - hour_min)}
    df.loc[len(df)] = new_row

    # 返回预处理后的数据
    return df


def denormalize_data(predictions, min_val, max_val):
    return predictions * (max_val - min_val) + min_val


# 创建输入数据
input_data = preprocess_data('3.0', '2.0', '93.0', '6.0', '3.0', '0.0', '1.0', '3.0', '0.0')

# 调整输入数据的形状
input_data = np.reshape(input_data.values, (1, 1, 9))

# 将数据类型转换为float32
input_data = input_data.astype(np.float32)

# 进行预测
predictions = model.predict(input_data, verbose=1)

# 设置最大值和最小值
max_val = 7860
min_val = 0

# 反归一化预测结果
predictions = denormalize_data(predictions, min_val, max_val)

# 输出预测结果
print(predictions)
