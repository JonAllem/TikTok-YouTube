from youtube_api import YoutubeDataApi
import pandas as pd
from utils import API_KEY
from utils import video_metadata_dict
from utils import tags

youtube = YoutubeDataApi(key=API_KEY)
for tag in tags:
    try:
        videos_df = pd.read_csv('data/{}/videos.csv'.format(tag))
    except Exception:
        print('Video file doesn\'t exist for tag {}'.format(tag))
        continue
    videos = videos_df.values.tolist()
    metas = []
    for video in videos:
        metadata = youtube.get_video_metadata(video[0])
        metadata = video_metadata_dict(metadata, video)
        metas.append(metadata)

    video_df = pd.DataFrame(metas)
    video_df.to_csv('data/{}/videos.csv'.format(tag), index=False)
