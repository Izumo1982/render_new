from flask import Flask
import datetime
app = Flask(__name__)

@app.route('/')
def hello_world():
   now = datetime.datetime.now() 
   return now.strftime('今日は%Y年%m月%d日\n今は%H時%M分%S秒') + '\n\nただのHello World'