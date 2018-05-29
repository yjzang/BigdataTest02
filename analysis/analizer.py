
import json
import re
# json 파일명,추출할 데이터의 json key값을 주면 문자열을 리턴한다.
from typing import Counter

from konlpy.tag import Twitter


def json_to_str(filename,key):
    jsonfile = open(filename,'r',encoding="utf-8")
    json_string = jsonfile.read()
    jsondata = json.loads(json_string)

    #print(type(json_string))
    #print(json_string)

    #print(type(jsondata))
    #print(jsondata)

    data=''
    for item in jsondata:
        value = item.get(key)
        data += re.sub(r'[^\w]',' ',value) # 한글만 계속 붙여나간다.

    print(type(data))
    return data

#명사를 추출해서 빈도수를 알려줌
def count_wordfreq(data):
    twitter = Twitter()
    nouns = twitter.nouns(data)
    print(type(nouns))

    print('명사분리: %s ' % nouns)
    count = Counter(nouns)
    #print(count)
    print(type(count))
    count = dict(count)
    count_list=count.copy().keys()
    for item in count_list:
        print(item)
        if len(item) == 1:
            count.pop(item)

    count = Counter(count)
    count = dict(count.most_common(20))
    return count



if __name__ == '__main__':
    dataString = json_to_str("D:\javaStudy/facebook/jtbcnews.json","message")
    #print(dataString)
    count_wordfreq(dataString)
