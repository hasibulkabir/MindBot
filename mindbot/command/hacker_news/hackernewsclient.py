from requests import get

from ..commandbase import CommandBase

class HackerNewsClient():

    def get_latest_items(self,type):
        url = 'https://hacker-news.firebaseio.com/v0/{}'.format(type)
        response = get(url)
        return response.json()

    def get_item(self, item_id):
        item = {'title': None,
                'url': None,
                'score': None}
        url = 'https://hacker-news.firebaseio.com/v0/item/{}.json'.format(item_id)
        response = get(url).json()
        if 'url' in response:
            item['url'] = response['url']
        if 'title' in response:
            item['title'] = response['title']
        if 'score' in response:
            item['score'] = response['score']
        return item


    def is_number(self, quantity):
        try:
            int(quantity)
            return True
        except ValueError:
            return False
