from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def print_numbers():
    numbers = [str(i) for i in range(1, 11)]
    return "\n".join(numbers)
