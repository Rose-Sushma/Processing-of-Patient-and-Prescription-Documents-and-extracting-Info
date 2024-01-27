from fastapi import FastAPI,Form, UploadFile,File
import uvicorn
import uuid
app = FastAPI()
from extractor import extract
@app.post("/extract_from_doc")
async def extract_from_doc(

        file_format:str=Form(...),
        file:UploadFile=File()
    ):
    contents = file.file.read()
    file_path=r'{provide a path where you want your internediate file to be created}' + str(uuid.uuid4()) + '.pdf'
    with open(file_path,"wb") as f:
        f.write(contents)
    try:
        data = extract(file_path, file_format)
    except Exception as e:
                data = {
            'error': str(e)
        }
    return data
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
