from flask import Flask
app = Flask(__name__)
import pandas as pd
import plotly.graph_objects as go

@app.route('/')
def hello_world():
    df = pd.read_excel('fat.xlsx')

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

   return fig.show()