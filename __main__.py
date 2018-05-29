from collect import crawler
from analysis import analizer
from visualize import visualizer

pagename = "chosun"
from_date = "2018-02-09"
to_date = "2018-02-30"

if __name__ =="__main__":
    
    # 수집
    result = crawler.fb_get_post_list(pagename,from_date,to_date)
    print(result)

    # 분석
    dataString = analizer.json_to_str("D:\javaStudy/facebook/chosun.json", "message")
    # print(dataString)
    dictWords = analizer.count_wordfreq(dataString)
    #count_data = analizer.count_wordfreq(dataString)
    #print(count_data)
    #dictWords = dict(count_data.most_common(20))
    print(type(dictWords))
    print(dictWords)
    # 그래프
    visualizer.show_graph_bar(dictWords, pagename)
    visualizer.wordcloud(dictWords, pagename)
