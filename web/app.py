import csv
from io import TextIOWrapper, StringIO
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from common import Algorithms, names

app = FastAPI()


@app.post("/pair", response_model=list[list[str]])
async def pair(data: list[str]):
    return Algorithms.detect_duplicates(data)


@app.post("/classify", response_model=list[str])
async def classify(data: str):
    return [names[category] for category in Algorithms.classify_category(data)]


@app.post("/clear_and_classify")
async def clear_and_classify(file: UploadFile = File()):
    wrapper = TextIOWrapper(file.file, encoding="utf-8")
    texts = [text + f"${channel_id}" for text, channel_id in csv.reader(wrapper)[1:]]
    result = [
        [
            text.rsplit("$")[0],
            int(text.rsplit("$")[1]),
            Algorithms.classify_category(text),
        ]
        for text in {
            max(result, key=len) for result in Algorithms.detect_duplicates(texts)
        }
    ]
    io = StringIO()
    writer = csv.writer(io)
    writer.writerows(result)
    response = StreamingResponse(iter(io.getvalue()), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=predictions.csv"
    return response
