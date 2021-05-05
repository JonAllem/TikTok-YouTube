from youtube_api import YoutubeDataApi
import pandas as pd
from utils import API_KEY
from utils import video_comments_dict
from utils import tags

youtube = YoutubeDataApi(key=API_KEY)
for tag in tags:
    print(tag)
    try:
        videos_df = pd.read_csv('data/{}/videos.csv'.format(tag))
    except Exception:
        print('Video file doesn\'t exist for tag {}'.format(tag))
        continue
    videos = videos_df.values.tolist()
    for video in videos:
        try:
            comments = youtube.get_video_comments(video[0])
            if len(comments) > 0:
                comments = [video_comments_dict(comment) for comment in comments]
                comment_df = pd.DataFrame(comments)
                comment_df.to_csv('data/{}/comments/{}.csv'.format(tag, video[0]), index=False)
        except Exception as e:
            print(e)
