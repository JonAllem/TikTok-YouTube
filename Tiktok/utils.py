import time


verifyFp = "verify_km3ym1ss_fHkhOpaC_5AaA_4OHU_8Fdo_CrQykN0yqAmt"


def simple_dict(tiktok_dict):
    to_return = dict()
    to_return['user_name'] = tiktok_dict['author']['uniqueId']
    to_return['user_id'] = tiktok_dict['author']['id']
    to_return['video_id'] = tiktok_dict['id']
    to_return['video_description'] = tiktok_dict['desc']
    to_return['video_create_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(tiktok_dict['createTime']))
    to_return['video_length'] = tiktok_dict['video']['duration']
    to_return['video_link'] = 'https://www.tiktok.com/@{}/video/{}?lang=en'.format(to_return['user_name'],
                                                                                   to_return['video_id'])
    to_return['n_likes'] = tiktok_dict['stats']['diggCount']
    to_return['n_shares'] = tiktok_dict['stats']['shareCount']
    to_return['n_comments'] = tiktok_dict['stats']['commentCount']
    to_return['n_plays'] = tiktok_dict['stats']['playCount']
    return to_return
