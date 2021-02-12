import uuid
import datetime

if __name__ == '__main__':
    t = str(datetime.datetime.now())[:-7]
    print(t)  # 2020-04-18T04:25:03.038Z
    print(uuid.uuid4())
