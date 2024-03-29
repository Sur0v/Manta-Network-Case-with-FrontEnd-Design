import requests
import json
import pandas as pd
from datetime import datetime
import os
from openpyxl import load_workbook
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from mplcursors import cursor
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
import plotly.express as px

sns.set()
# %matplotlib inline

initiation = 0  #
xyz = []
date = []  # List of time variables
timing = str(datetime.now())
date.append(timing[5:19])  #List slicing on string element

username = "mantanetwork"
url = 'https://api.twitter.com/2/users/by/username/' + username

#Request
r = requests.get(
  url,
  headers={
    'Authorization':
    'Bearer AAAAAAAAAAAAAAAAAAAAAJSQiQEAAAAAtqy%2BjBN5A5WlYHxN1PIYrf8BqXg%3Dw1cpV7BF119COCISa5QXrLGLvoxkU2ZWA2WiSdtfeCRrekWi5L'
  })

#Response
response = json.loads(r.text)

url = 'https://api.twitter.com/2/users/' + response["data"][
  "id"] + '?user.fields=public_metrics,created_at,pinned_tweet_id&expansions=pinned_tweet_id&tweet.fields=created_at,public_metrics,source,context_annotations,entities'

r = requests.get(
  url,
  headers={
    'Authorization':
    'Bearer AAAAAAAAAAAAAAAAAAAAAJSQiQEAAAAAtqy%2BjBN5A5WlYHxN1PIYrf8BqXg%3Dw1cpV7BF119COCISa5QXrLGLvoxkU2ZWA2WiSdtfeCRrekWi5L'
  })
response = json.loads(r.text)
totalFollower = int(response["data"]["public_metrics"]["followers_count"])


def DataToExcel():


  try:
    initiation = len(pd.read_excel('pandas_to_excel.xlsx'))

  except:
    initiation = 0

  print(initiation)

  if initiation == 0:
    pd.ExcelWriter('pandas_to_excel.xlsx', datetime_format='dd/mm/yy')
    df = pd.DataFrame({'Follower': [totalFollower], 'Date': timing[5:19]})
    df2 = df
    dLast = df
    dLast.to_json('Follower.json')
    df2.to_json('pandas_to_json.json')
    df2.to_excel('pandas_to_excel.xlsx',
                sheet_name='new_sheet_name',
                columns={'Follower', 'Date'})

  else:
    previousData = pd.read_excel("pandas_to_excel.xlsx")
    previousDataJson = pd.read_json('pandas_to_json.json')
    pd.ExcelWriter('pandas_to_excel.xlsx', datetime_format='dd/mm/yy')
    df = pd.DataFrame({'Follower': [totalFollower], 'Date': timing[5:19]})
    df2 = pd.concat(
      [previousData, df])  #adding two dataframes .apply function is depreceated.
    dLast = df
    dLast.to_json('Follower.json')
    jsonData = pd.concat([previousDataJson, df], ignore_index=True)
    jsonData.to_json('pandas_to_json.json')
    df2.to_excel('pandas_to_excel.xlsx',
                 sheet_name='new_sheet_name',
                 columns={'Follower', 'Date'})

  twitter_df = pd.read_excel("pandas_to_excel.xlsx")
  figure = sns.lineplot(data=twitter_df, x="Date", y="Follower", marker=".")
  figure.set_ylim((twitter_df["Follower"].min()) * 0.98,
                  (twitter_df["Follower"].max()) * 1.02)
  figure.set_title("Manta Network")
  plt.xticks(rotation=90)

  cursor(hover=True)

DataToExcel()