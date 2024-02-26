## Project README

This project combines three scripts to perform various tasks including downloading the latest video from a specified YouTube channel, transcribing its audio content, and summarizing the transcription using artificial intelligence models.

### YouTube Video Downloader

#### Description

This script utilizes the Google API Client Library and PyTube library to download the most recent video from a specified YouTube channel.

#### Prerequisites

- `google-api-python-client`
- `pytube`

#### Setup

1. Obtain a YouTube Data API key from the Google Developers Console.
2. Set the obtained API key to the `API_KEY` variable in the script.
3. Set the desired YouTube channel name or ID to the `CHANNEL_NAME` variable in the script.

#### Usage

1. Run the script.
2. It fetches the most recent video from the specified YouTube channel.
3. It downloads the video with the highest resolution available.

#### Important Notes

- Use caution with unverified SSL context in the script.
- Ensure the API key has necessary permissions to interact with the YouTube Data API.

---

### Speech to Text Transcription

#### Description

This script uses the Google Cloud Speech-to-Text API to transcribe audio from a video file and save the transcription output to a JSON file.

#### Prerequisites

- Google Cloud SDK
- Google Cloud Storage
- Google Cloud Speech-to-Text API
- `pydub`

#### Configuration

1. Set the path to your service account JSON key file in the `CredentialFileName` variable.
2. Specify the input video file (`MP4_VIDEO`) and the desired audio export file name (`AUDIO_FILE_EXPORT`).
3. Set the name of your Google Cloud Storage bucket (`GOOGLE_BUCKET`).
4. Define the name of the output file for transcription (`TRANSCRIBE_OUTPUT_FILE`).

#### Usage

1. Run the script.
2. It loads the specified video file, extracts the audio, and exports it to a WAV format.
3. It uploads the audio file to the configured Google Cloud Storage bucket.
4. The script transcribes the audio using the Speech-to-Text API.
5. Transcription results are saved to the specified output file in JSON format.

#### Important Notes

- Verify necessary permissions and quotas for using the Google Cloud Speech-to-Text API.
- Ensure the specified Google Cloud Storage bucket exists and has appropriate permissions.

---

### Text Summarization

#### Description

This script utilizes the OpenAI GPT-3.5 model to summarize text extracted from a file.

#### Prerequisites

- OpenAI API Key

#### Configuration

- Set your OpenAI API key in the `OPENAI_API_KEY` environment variable.
- Specify the name of the text file you want to summarize in the `TEXT_TO_SUMMARIZE` variable.

#### Usage

1. Run the script.
2. It loads the content from the specified text file.
3. It constructs a prompt for the OpenAI GPT-3.5 model, requesting it to summarize the text.
4. The script sends the prompt to the OpenAI API and retrieves the summarized text.
5. Finally, it prints the summarized text to the console.

#### Important Note

- Keep your OpenAI API key secure and not shared publicly.
- Monitor your usage of the OpenAI API to avoid exceeding plan limits or incurring unexpected charges.

---

### Disclaimer

These scripts are provided as examples and may require additional customization for production use. Review and validate the outputs generated by these scripts for accuracy and coherence in critical applications.