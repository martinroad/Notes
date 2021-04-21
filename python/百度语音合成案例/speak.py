'''
 接入百度语音Python SDK：https://ai.baidu.com/ai-doc/SPEECH/zk4nlz99s
'''

from aip import AipSpeech

# ai.baidu 后台的 APPID，API_KEY，SECRET_KEY
APP_ID = '24034416'
API_KEY = 'Fy0EFqdRjHNGc6M1ztoqbwRA'
SECRET_KEY = 'R86ULh4Y8GEY75YIgufEI7ZS6iLRvfrn'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
client.setConnectionTimeoutInMillis(5000) #建立连接的超时时间（单位：毫秒）
client.setSocketTimeoutInMillis(1000*30)  #通过打开的连接传输数据的超时时间（单位：毫秒）

result  = client.synthesis('你好百度', 'zh', 1, {
    'spd': 5, #语速，取值0-9，默认为5中语速
    'pit': 5, #音调，取值0-9，默认为5中语调
    'vol': 5, #音量，取值0-15，默认为5中音量
    'per':0,  # 发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)
