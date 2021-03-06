from azure.cognitiveservices.search.newssearch import NewsSearchAPI
from msrest.authentication import CognitiveServicesCredentials

def bingResult(keywords, curLink):
    subscription_key = "18d92d49457f44869027dcd6145d4b11"
    search_term = ""
    for word in keywords:
        search_term += word + " "
    print("SEARCHTERM:", search_term)

    client = NewsSearchAPI(CognitiveServicesCredentials(subscription_key))

    news_result = client.news.search(query=search_term, market="en-us", count=9)
    count = 7
    i = 1

    newsInfo = {"title": [], "provider": [], "description": [], "URL": []}

    while i < min(count, len(news_result.value)):
        if news_result.value[i].url not in curLink:
            print("index:", i)
            cur_news_result = news_result.value[i]
            newsInfo["title"].append(cur_news_result.name)
            newsInfo["provider"].append(cur_news_result.provider[0].name)
            newsInfo["description"].append(cur_news_result.description)
            newsInfo["URL"].append(cur_news_result.url)
            """
            ("num", i, "news url: {}".format(first_news_result.url)),
            ("num", i, "news description: {}".format(first_news_result.description)),
            ("num", i, "published time: {}".format(first_news_result.date_published)),
            ("num", i, "news provider: {}".format(first_news_result.provider[0].name))})
            """
        else:
            count+=1


        i += 1

    return newsInfo
