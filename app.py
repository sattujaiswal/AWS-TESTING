from fastapi import FastAPI
import uvicorn
import time

app = FastAPI()

@app.get("/")
def print_numbers():
    numbers = [str(i) for i in range(1, 11)]
    return " ".join(numbers)


@app.get("/compute/")
def compute():
    # Simulate CPU-intensive task
    start_time = time.time()
    while time.time() - start_time < 10:  # Run for 10 seconds
        pass
    return {"message": "Completed CPU-intensive task"}
    

@app.get("/{name}/")  # Corrected route path
def print_numbers(name):
    return f"Hi {name}"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
