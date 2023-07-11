from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense
from tensorflow.keras.utils import plot_model

# 创建一个新的模型对象
model = Sequential([
    LSTM(units=256, input_shape=(10, 8), return_sequences=True),
    Dropout(0.4),
    LSTM(units=256, return_sequences=True),
    Dropout(0.3),
    LSTM(units=128, return_sequences=True),
    LSTM(units=32),
    Dense(1)
])

plot_model(model, to_file='model.png', show_shapes=True)
