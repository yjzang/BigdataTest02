import matplotlib.pyplot as plt
from matplotlib import font_manager
import pytagcloud
import webbrowser

# matplotlib 그래프
from numpy.ma import size


def show_graph_bar(dictWords, pagename):
    #한글처리
    font_filename = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_filename).get_name()
    print(font_name)
    plt.rc('font', family=font_name)

    # 라벨처리
    plt.xlabel("주요단어")
    plt.ylabel("빈도수")
    plt.grid(True)

    # 데이터 대입
    dict_keys = dictWords.keys()
    dict_values = dictWords.values()

    plt.bar(range(len(dictWords)), dict_values, align='center')
    plt.xticks(range(len(dictWords)), list(dict_keys), rotation=70)

    save_filename = "D:\javaStudy/facebook/%s_bar_graph.png" % pagename
    plt.savefig(save_filename, dpi=400, bbox_inches='tight')

    plt.show()


# 워드 클라우드
def wordcloud(dictWords, pagename):
    print(dictWords)
    taglist = pytagcloud.make_tags(dictWords.items(),maxsize=80)
    save_filename = "D:\javaStudy/facebook/%s_wordcloud.png" %pagename

    pytagcloud.create_tag_image(

        taglist,
        save_filename,
        size=(800,600),
        fontname = 'korea',
        rectangular = False
    )
    webbrowser.open(save_filename)



