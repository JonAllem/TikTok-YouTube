import random
import random
import string

import pandas as pd
from TikTokApi import TikTokApi

from utils import simple_dict, verifyFp

username = 'juullllss'

did = ''.join(random.choice(string.digits) for num in range(19))

api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True, custom_did=did)

user_videos = api.byUsername(username, count=10)

# with open("juul.pkl", 'wb') as file:
#     pkl.dump(user_videos, file)
print(len(user_videos))
# print(json.dumps(user_videos[0]))
# print(simple_dict(user_videos[0]))
processed_videos = [simple_dict(video) for video in user_videos]
videos_df = pd.DataFrame(processed_videos)
videos_df.to_csv('{}_videos.csv'.format(username))
