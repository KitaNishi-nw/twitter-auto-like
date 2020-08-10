import tweepy
from config import CONFIG

CONSUMER_KEY = CONFIG["CONSUMER_KEY"]
CONSUMER_SECRET = CONFIG["CONSUMER_SECRET"]
ACCESS_TOKEN = CONFIG["ACCESS_TOKEN"]
ACCESS_SECRET = CONFIG["ACCESS_SECRET"]
#キーの呼び出しをする記述↑


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)
#インスタンス作成↑

search_results = api.search(q="#いいねした人全員フォロー", count=100)
#ここでツイートの検索↑

for result in search_results:
    tweet_id = result.id
    try:
        api.create_favorite(tweet_id)
    except Exception as e:
        print(e)
#ここでいいねしてる↑

#参考URL https://qiita.com/starcoffee66/items/cd61fd187d26c245e37d