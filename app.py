from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    
    return fib_series

@app.get("/")
def read_root():
    return {"message": "Welcome to Fibonacci FastAPI"}

@app.get("/fibonacci/{n}")
def get_fibonacci(n: int):
    if n < 1:
        raise HTTPException(status_code=400, detail="The number of terms must be a positive integer")
    fib_series = fibonacci(n)
    return {"fibonacci_series": fib_series}

if __name__ == "__main__":
    print("Starting FastAPI application...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
    print("FastAPI application has started.")

# from fastapi import FastAPI
# import requests

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": f"Hello from FastAPI on EC2 Instance server 1!"}

# if __name__ == "__main__":
#     import uvicorn
#     print("Starting FastAPI application...")
#     uvicorn.run(app, host="0.0.0.0", port=8000)
#     print("FastAPI application has started.")
