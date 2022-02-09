import datetime
import json

def log_to_file(obj):
    open('logs.txt', 'a').write(
        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " | " + json.dumps(obj) + '\n'
    )
obj = {"message":"OK"}
log_to_file(obj)
print (obj)