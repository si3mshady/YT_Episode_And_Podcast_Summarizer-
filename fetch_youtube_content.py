from googleapiclient.discovery import build
from pytube import YouTube
import ssl


ssl._create_default_https_context = ssl._create_unverified_context


# Set your API key
API_KEY = ''

# Set the YouTube channel ID
CHANNEL_NAME = "@MeidasTouch"

# Create a service object for interacting with the YouTube Data API
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Request channel information based on the channel title
request = youtube.search().list(
    part='snippet',
    q=CHANNEL_NAME,
    order="date",
    type='channel',
    maxResults=1  # You can adjust this number as needed
)


video_list_sorted_by_date_decending = []

response = request.execute()

CHANNEL_ID = [id['id']['channelId'] for id in response['items']][0]
# Extract video information from the response

request = youtube.search().list(
    part='snippet',
    channelId=CHANNEL_ID,
    order='date',
    type='video',
    maxResults=10  # You can adjust this number as needed
)

response = request.execute()



# Extract video information from the response
for item in response['items']:
    video_title = item['snippet']['title']
    video_id = item['id']['videoId']


    video_url  = f"https://www.youtube.com/watch?v={video_id}"

    obj = {
        "title": video_title,
        "url": video_url
        }
    
    video_list_sorted_by_date_decending.append(obj)

       
print(f"The most current video is {video_list_sorted_by_date_decending[0]}")


# URL of the YouTube video you want to download
video_url = f"{video_list_sorted_by_date_decending[0]['url']}"

# Create a YouTube object
yt = YouTube(video_url)

# Get the highest resolution stream
stream = yt.streams.get_highest_resolution()

# Download the video to the current directory
stream.download()


