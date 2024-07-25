import assemblyai as aai
# from constants import assemblyai_api_key
#Set API key
aai.settings.api_key = "d346c2df5e4f4d81a3ce52d91c59bda1"

# FILE_URL = "https://github.com/AssemblyAI-Community/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"
audio_file="https://storage.googleapis.com/aai-web-samples/news.mp4"

#Transcribe an audio file
transcriber = aai.Transcriber()
transcript = transcriber.transcribe(audio_file)

result=transcript.lemur.task(
    "I'm sending you a transcript of a video, please summarize it and I'll you questions of it",
    final_model=aai.LemurModel.claude3_5_sonnet
)
print(result.response)

# print("Hey, there I'm processing your file")