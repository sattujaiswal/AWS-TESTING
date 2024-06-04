from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def print_numbers():
    numbers = [str(i) for i in range(1, 11)]
    return "\n".join(numbers)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
