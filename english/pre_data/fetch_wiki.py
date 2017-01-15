# Author: Tenghu Wu
# Date:   2017-Jan-15

import wikipedia
from clean_str import clean_str

if __name__ == '__main__':
    
    # get page documents from the wikipedia
    lines = open('100_US_cities.txt','r').readlines()
    w = open('ciities_corpus','w+')
    count = 0
    for item in lines:
        temp = item.strip()
        count += 1
        print(count,temp)
        try:
            tit = wikipedia.page(temp,"html.parser")
            cut_content = clean_str(tit.content)
            w.write(cut_content+' ')
        except:
            pass

    w.close()

        # print(item)
    # cut_content_temp = tit.content.split('\n')
    # cut_content = []
    # for item in cut_content_temp:
    #     item = clean_str(item)
    #     # print(item,type(item))
    #     if item == u'':
    #         pass
    #     else:
    #         cut_content.append(item)

    # print(' '.join(item for item in cut_content))
