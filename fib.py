from fastapi import FastAPI
import uvicorn
import time

app = FastAPI()


def multiply(a, b, x, y):
    return x*(a+b) + a*y, a*x + b*y

def square(a, b):
    a2 = a * a
    b2 = b * b
    ab = a * b
    return a2 + (ab << 1), a2 + b2

def power(a, b, m):
    if m == 0:
        return (0, 1)
    elif m == 1:
        return (a, b)
    else:
        x, y = a, b
        n = 2
        while n <= m:
            # repeated square until n = 2^q > m
            x, y = square(x, y)
            n = n*2
        # add on the remainder
        a, b = power(a, b, m-n//2)
        return multiply(x, y, a, b)

def implicit_fib(n):
    start_time = time.perf_counter()
    a, b = power(1, 0, n)
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(total_time)
    return a


@app.get("/fib/{input}")
async def root(input:int):	
	output = implicit_fib(input);
	return {"input": input, "output": output}


if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=8000)





