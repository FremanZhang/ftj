import key
import requests


def run_query(search_term):
    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
    headers = {"Ocp-Apim-Subscription-Key" : key.BING_API_KEY}
    params  = {"q": search_term, "textDecorations":True, "textFormat":"HTML"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    filtered_results = []

    for result in search_results['value']:
        filtered_results.append({
            'title': result['name'],
            'content_link': result['contentUrl'],
            'origin_page': result['hostPageDisplayUrl']
        })

    return filtered_results


# if __name__ == '__main__':
#     print run_query('abigaile')

    