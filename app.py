from fastapi import FastAPI
import uvicorn
import time
import multiprocessing

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
    

def cpu_load():
    while True:
        pass

@app.get("/test-cpu-utilization/")
def test_cpu_utilization():
    num_processes = multiprocessing.cpu_count()
    target_utilization = 0.25  # Target CPU utilization (25%)
    processes = []

    for _ in range(num_processes):
        process = multiprocessing.Process(target=cpu_load)
        processes.append(process)
        process.start()

    # Monitor CPU utilization until target is reached
    while True:
        total_utilization = sum(p.cpu_percent() / 100 for p in processes)
        if total_utilization >= target_utilization * num_processes:
            break
        time.sleep(1)

    return {"message": "CPU utilization test completed"}    

@app.get("/{name}/")  # Corrected route path
def print_numbers(name):
    return f"Hi {name}"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
