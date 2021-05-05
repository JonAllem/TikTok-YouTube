import time
def search_dict(youtube_dict):
    youtube_dict['video_link'] = 'https://www.youtube.com/watch?v={}'.format(youtube_dict['video_id'])
    return youtube_dict


def playlist_dict(youtube_dict):
    youtube_dict['playlist_link'] = 'https://www.youtube.com/playlist?list={}'.format(youtube_dict['playlist_id'])
    return youtube_dict


def video_playlist_dict(youtube_dict, playlist_id):
    youtube_dict['playlist_id'] = playlist_id
    youtube_dict['video_url'] = 'https://www.youtube.com/watch?v={}&list={}'.format(youtube_dict['video_id'],
                                                                                    playlist_id)
    youtube_dict['publish_date'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(youtube_dict['publish_date']))
    return youtube_dict


def video_playlist_dict2(youtube_dict):
    youtube_dict['video_url'] = 'https://www.youtube.com/watch?v={}'.format(youtube_dict['video_id'])
    youtube_dict['publish_date'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(youtube_dict['publish_date']))
    return youtube_dict


def video_metadata_dict(youtube_video_dict, video):
    video_dict = dict()
    video_dict['video_id'] = video[0]
    video_dict['channel_id'] = video[1]
    video_dict['video_url'] = video[4]
    video_dict['publish_date'] = video[2]
    video_dict['collection_date'] = video[3]

    for key, value in youtube_video_dict.items():
        if key == 'channel_title' or key == 'channel_id' or key == 'video_category' or key == 'video_thumbnail':
            continue
        video_dict[key] = value
    video_dict['video_publish_date'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(video_dict['video_publish_date']))
    return video_dict


def video_comments_dict(comments_dict):
    result_dict = dict()
    for key, value in comments_dict.items():
        if key == 'video_id' or key == 'commenter_rating':
            continue
        result_dict[key] = value
    result_dict['comment_publish_date'] = time.strftime('%Y-%m-%d %H:%M:%S',
                                                        time.localtime(result_dict['comment_publish_date']))
    return result_dict


API_KEY = 'AIzaSyDstqO4PNSc8Pv88kJ5njrMPgGVy8RZJTc'
tags = ['juullabs', 'vusenewzealand', 'blucigs', 'njoyvape', 'joyetech', 'vapage', 'halocigs']
channelIds = ['UCpZDjAlOA4XdgV4dYArwbgw', 'UCjl50EcTt7niIsODWyiJRig', 'UCjz4G_c8LiBWuXe9Nlmv_0g',
              'UCJYNTn9Rsfyc0X0p1j8rP5g', 'UCcBv_mvnggN2ltTQaV-fLPQ', 'UCbq6vHFTE8dasOOwMARUu3g',
              'UC67bNJ7dLHoFGz0oiXZIcgg']