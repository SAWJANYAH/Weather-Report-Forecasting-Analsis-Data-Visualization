import pandas as pd
import numpy as np
from statsmodels.tsa.vector_ar.var_model import VAR

## 7.Please add the data in the dataset for 2034 and 2035 as well as forecast predictions for these years
df = pd.read_csv('Processed Weater Data.csv', index_col=0, parse_dates=True)
train = df.iloc[:-730, :]
test = df.iloc[-730:, :]

model = VAR(train)
model_fit = model.fit()

lag_order = model_fit.k_ar
predictions = model_fit.forecast(test.values, steps=730)

date_range = pd.date_range(start=test.index[0], periods=730, freq='D')
predictions_df = pd.DataFrame(data=predictions, index=date_range, columns=df.columns)

df_forecast = pd.concat([df, predictions_df])

df_forecast.to_csv('weather_data_forecast.csv')



