import pandas as pd
df = pd.read_excel('fat.xlsx')

# https://qiita.com/inoory/items/12028af62018bf367722

import plotly.graph_objects as go
fig = go.Figure(data=[
    go.Scatter(x=df['date'],
               y=df['weight'],
               name='体重'
              ),
    go.Scatter(
               x=df['date'],
               y=df['fat'],
               name='体脂肪率'
              ),
])
fig.show()
