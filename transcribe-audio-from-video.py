import openai 
from google.oauth2 import service_account 
from google.cloud import speech
from google.cloud import storage
from pydub import AudioSegment


# export GOOGLE_APPLICATION_CREDENTIALS=/Users/si3mshady/peter_yang_podcast_summarizer/speechToTextGoogleKey.json
MP4_VIDEO = "Supreme Court HITS Marjorie Taylor Greene with BAD NEWS.mp4"
CredentialFileName = 'speechToTextGoogleKey.json'
AUDIO_FILE_EXPORT = 'audio.wav'
GOOGLE_BUCKET = 'elliott-sandbox'
TRANSCRIBE_OUTPUT_FILE = 'transcribe_output.json'

# Load the video file and extract audio
video = AudioSegment.from_file(MP4_VIDEO, format="mp4")
audio = video.set_channels(1).set_frame_rate(16000).set_sample_width(2)
audio.export(AUDIO_FILE_EXPORT, format="wav")

bucket_client = storage.Client()
bucket_ref = bucket_client.get_bucket(GOOGLE_BUCKET)
blob = bucket_ref.blob(AUDIO_FILE_EXPORT)
blob.upload_from_filename(AUDIO_FILE_EXPORT)

print(f"File {AUDIO_FILE_EXPORT} uploaded to {GOOGLE_BUCKET} bucket.")




uri = f'gs://{GOOGLE_BUCKET}/{AUDIO_FILE_EXPORT}'

print(uri) #should see gs://elliott-sandbox/audio.mp3

creds = service_account.Credentials.from_service_account_file(CredentialFileName)
client = speech.SpeechClient(credentials=creds)

audio = speech.RecognitionAudio(uri=uri)

config = speech.RecognitionConfig(
        # encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        # sample_rate_hertz=16000,
        language_code="en-US")

# response = client.recognize(config=config, audio=audio)

response = client.long_running_recognize(config=config, audio=audio)

# 
print('Waiting for operation to complete...')

while not response.done():
    # Check operation status periodically
    if response.running():
        print('Transcription in progress...')
    else:
        print('Operation status: Unknown')

res = response.result(timeout=90)

with open(TRANSCRIBE_OUTPUT_FILE, 'w') as file:
        for result in res.results:
            transcript = result.alternatives[0].transcript
            file.write(transcript + '\n')
