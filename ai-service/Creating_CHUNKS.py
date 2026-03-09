import whisper
import json
import os

model = whisper.load_model("small")

audios = os.listdir(r"C:\Users\Adiraj\Desktop\ALL\marathon-v2\audios")

for audio in audios:
    name = audio.split(".")[0]
    print(name)
    result = model.transcribe(audio = f"audios/{audio}",
                            language = "hi",
                            task="translate",
                            word_timestamps = False)

    # print(result)

    chunks = []
    for segement in result["segments"]:
        chunks.append({"name":name, "start":segement["start"], "end":segement["end"], "id":segement["id"], "text":segement["text"]})

    chunks_with_metadat = {"chunks":chunks, "text":result["text"]}

    with open(f"jsons/{name}.json", "w") as f:
        json.dump(chunks_with_metadat,f)