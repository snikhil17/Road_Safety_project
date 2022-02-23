
from GoogleNews import GoogleNews
import pandas as pd
import nltk
from tqdm import tqdm
from newspaper import Article
nltk.download('punkt')

#tutorial : https://pypi.org/project/GoogleNews/

googlenews = GoogleNews()
#googlenews.search('accidents in india')
googlenews.get_news('accidents in india')
result=googlenews.result()

df=pd.DataFrame(result)
dic={'news_body':[],'keywords':[],'summary':[]}
df['news_body']=''
df['keywords']=''
df['summary']=''

for i in tqdm(range(len(df['link']))):
    try:
            
        url="https://"+df['link'][i]
        article = Article(url)
        article.download()
        article.parse()
        df['news_body'][i]=article.text
        article.nlp()
        df['keywords'][i]=article.keywords
        df['summary'][i]=article.summary
    except:
        df['news_body'][i]='Nan'
        df['keywords'][i]='Nan'
        df['summary'][i]='Nan'
   

df.to_csv('accidents_india.csv')
