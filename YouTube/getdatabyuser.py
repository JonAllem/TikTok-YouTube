import pandas as pd
import time
from youtube_api import YoutubeDataApi

from utils import API_KEY
from utils import video_playlist_dict2
from utils import tags
from utils import channelIds

youtube = YoutubeDataApi(key=API_KEY)
for channelId, tag in zip(channelIds, tags):
    print(tag)
    meta = youtube.get_channel_metadata(channelId)
    meta['account_creation_date'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(meta['account_creation_date']))
    meta_df = pd.DataFrame([meta])
    meta_df.to_csv('data/{}/metadata.csv'.format(tag), index=False)
    playlist_id_uploads = meta['playlist_id_uploads']
    try:
        videos = youtube.get_videos_from_playlist_id(playlist_id_uploads)
        videos = [video_playlist_dict2(video) for video in videos]
        # playlists = youtube.get_playlists(channelId)
        # # print(len(playlists))
        # playlists = [playlist_dict(playlist) for playlist in playlists]
        # all_videos = []
        # for playlist in playlists:
        #     videos = youtube.get_videos_from_playlist_id(playlist['playlist_id'])
        #     # playlists_df = pd.DataFrame(playlists)
        #     # playlists_df.to_csv('{}_channel_playlists.csv'.format(channelId), index=False)
        #     videos = [video_playlist_dict(video, playlist['playlist_id']) for video in videos]
        #     # print(len(videos))
        #     all_videos += videos
        # # print(len(all_videos))
        video_df = pd.DataFrame(videos)
        video_df.to_csv('data/{}/videos.csv'.format(tag), index=False)
    except Exception:
        print('No videos uploaded for tag {}'.format(tag))
