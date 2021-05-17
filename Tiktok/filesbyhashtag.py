import random
import string

import pandas as pd
from TikTokApi import TikTokApi
from tqdm import tqdm

from utils import simple_dict, verifyFp


def getTiktok():
    hashtags = ['juul', 'swishersweets', 'backwood', 'puffplus']
    did = ''.join(random.choice(string.digits) for num in range(19))

    api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=False, custom_did=did)
    for hashtag in tqdm(hashtags):
        hashtag_object = api.getHashtagObject(hashtag)
        total_cnt = hashtag_object['challengeInfo']['stats']['videoCount']
        print(hashtag + ':' + str(total_cnt))
        user_videos = api.byHashtag(hashtag, count=total_cnt)
        print(len(user_videos))
        processed_videos = [simple_dict(video) for video in user_videos]
        video_df = pd.DataFrame(processed_videos)
        video_df.to_csv('data/{}_hashtag_all_videos.csv'.format(hashtag), index=False)


if __name__ == '__main__':
    getTiktok()
