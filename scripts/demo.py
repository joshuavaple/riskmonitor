# import riskmonitor as rm 
from riskmonitor.configs.apicredentials import API_KEY
import eventregistry as evreg


print(API_KEY)
MAX_RESULTS = 5
query_keywords = ["Port", "Shipping", "Disruption"]


er = evreg.EventRegistry(apiKey = YOUR_API_KEY)

q = QueryArticlesIter(keywords = QueryItems.OR(query_keywords))
for art in q.execQuery(er, maxItems = MAX_RESULTS):
    print(art)