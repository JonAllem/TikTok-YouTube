from youtube_api import YoutubeDataApi
import pandas as pd
from utils import search_dict
from utils import API_KEY


query = 'Juul'
youtube = YoutubeDataApi(key=API_KEY)
searches = youtube.search(q=query)
print(len(searches))
searches = [search_dict(search) for search in searches]
searches_df = pd.DataFrame(searches)
searches_df.to_csv('{}_searches.csv'.format(query), index=False)
