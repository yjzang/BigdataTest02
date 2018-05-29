import requests
from datetime import datetime,timedelta

BASE_URL_FB_API = "https://graph.facebook.com/v3.0"
ACCESS_TOKEN = "EAACEdEose0cBAHCnlZBdZBV7yZCdChDmR1sP7OQ5USlUjJlQlZC5ChZCpfz3fqNgOwhguo1SUs8X1yrDyAmXTH1znzDzuZARdIZB4hXBD1WOBvn1zZCG6dkzdSSTEcXKsg9hTJVxh3ZBB8F5JrqUouHjrDJPF4BE8I7JmbuBMiBoY0yZAxlA0Tu9lqTZBAZA8wmYqYMJ4bIRuXAIlAZDZD"
LIMIT_REQUEST = 20
pagename = "chosun"
from_date = "2018-05-12"
to_date="2018-05-23"

def get_json_result(url):
    try:
        response = requests.get(url)

        if response.status_code==200:
            json_result = response.json()

        return json_result

    except Exception as e :
        return '%s : Error for requests [%s]' % (datetime.now(),url)

def fb_name_to_id(pagename):
    base = BASE_URL_FB_API
    node = "/"+pagename
    params = "/?access_token=%s" % ACCESS_TOKEN
    url = base+ node+ params
    print(url)
    # url = "https://graph.facebook.com/v3.0/jtbcnews/?access_token=%s" %ACCESS_TOKEN
    json_result = get_json_result(url)
    return json_result["id"]


#result = fb_name_to_id("jtbcnews")
#print(result)


def preprocess_post(post):
    # 작성일 +9시간 처리
    created_time = post["created_time"]
    created_time = datetime.strptime(created_time, '%Y-%m-%dT%H:%M:%S+0000') # date 포맷 변환
    created_time = created_time + timedelta(hours=+9)
    created_time = created_time.strftime('%Y-%m-%d %H:%M:%S')

    # 공유 수
    if "shares" not in post :
        shares_count = 0
    else :
        shares_count = post["shares"]["count"]
    # 리액션 수
    if "reactions" not in post :
        reactions_count = 0
    else :
        reactions_count = post["reactions"]["summary"]["total_count"]
    # 댓글 수
    if "comments" not in post :
        comments_count = 0
    else :
        comments_count = post["comments"]["summary"]["total_count"]
    # 메세지
    if "message" not in post :
        message_str = ""
    else :
        message_str = post["message"]

    postVO = {
            "created_time": created_time,
            "shares_count": shares_count,
            "reactions_count": reactions_count,
            "comments_count":comments_count,
            "message":message_str
     }

    return postVO

# JTBC 뉴스 포스트 data 가져오기
def fb_get_post_list(pagename,from_date,to_date):
    page_id = fb_name_to_id(pagename)
    base = BASE_URL_FB_API
    node = "/%s/posts" %page_id
    fields="/?fields=id,message,link,name,type,shares," \
        "created_time,comments.limit(0).summary(true)," \
        "reactions.limit(0).summary(true)"
    duration="&since=%s&until=%s" %(from_date,to_date)
    parameters="&limit=%s&access_token=%s" %(LIMIT_REQUEST,ACCESS_TOKEN)

    url = base + node + fields + duration + parameters
    jsonPosts = get_json_result(url) #포스트 정보를 dict 형태로 리턴한다.(data,paging)

    postList=[]
    isNext = True
    while isNext:
        tmpPostList = get_json_result(url)
        print(tmpPostList)
        count=0;
        for post in tmpPostList["data"]:
            postVO = preprocess_post(post)
            postList.append(postVO)
            count=count+1
            print("(%d) %s \n" % (count,post.get("message")))

        paging = tmpPostList.get("paging").get("next")
        #paging = tmpPostList["paging"]["next"]
        if paging!=None:
            url = paging
        else:
            isNext = False

    return postList




result = fb_get_post_list(pagename,from_date,to_date)


print(result)
