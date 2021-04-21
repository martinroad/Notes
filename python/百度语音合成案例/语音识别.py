'''
    将map3语音文件识别为文本文件
    接入百度语音Python SDK：https://ai.baidu.com/ai-doc/SPEECH/zk4nlz99s
'''

import os
from aip import AipSpeech


# ai.baidu 后台的 APPID，API_KEY，SECRET_KEY
APP_ID = '24034416'
API_KEY = 'Fy0EFqdRjHNGc6M1ztoqbwRA'
SECRET_KEY = 'R86ULh4Y8GEY75YIgufEI7ZS6iLRvfrn'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# client.setConnectionTimeoutInMillis(5000) #建立连接的超时时间（单位：毫秒）
# client.setSocketTimeoutInMillis(1000*30)  #通过打开的连接传输数据的超时时间（单位：毫秒）


# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别文件
file_url = os.getcwd()+ '\\audio.wav'
print('file_url:', file_url)
speech = get_file_content(file_url)
print(speech)
result = client.asr(speech, 'wav', 8000, {
    'dev_pid': 1537,
})

print(result)