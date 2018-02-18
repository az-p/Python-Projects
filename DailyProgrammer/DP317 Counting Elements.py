##########################################################################
#     Project: Counting Elements
#        From: https://redd.it/6eerfk
# Description: Show number of each elements for a given chemical formula
#
##########################################################################

# import asyncio
import requests


def main():
    search_term = "Philosophy"

    articles = ["Edison"]
    cls = []
    queue = []
    found = False
    while found = False:
        qry = build_api_call(articles)
        get_links(qry)

def build_api_call(article_names):
    qry = []
    for article in article_names:
        qry.append(qry, "https://en.wikipedia.org/w/api.php?action=query&prop=categories&cllimit=100&titles=" + article)
    return qry

def get_links(qry):
    requests = async.compile(qry)
    results = requests.Get()
    for result in results:
        if title = search:
            found = True