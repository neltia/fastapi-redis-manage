import uvicorn


# test app run
if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=8001, reload=True)