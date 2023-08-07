from fastapi import FastAPI
import uvicorn
import pyppeteer
from gologin import GoLogin
app = FastAPI()


@app.get("/")
async def root():
    gl = GoLogin({
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NGM4ZWJiMmYyNjJkZTllZThmZTQzZmUiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NGNhMTIzNDc3MTIzMzQ2OTUzZjIxMjEifQ.ubWuZVeZ75iioJHSTpImCxds4Tz7XZDig0Q1ikG9alE",
        "profile_id": "64ca105e7712335e093e4278",
    })

    debugger_address = gl.start()
    browser = await pyppeteer.connect(browserURL="http://" + debugger_address)
    page = await browser.newPage()
    await gl.normalizePageView(page)
    await page.goto('https://gologin.com')
    content = await page.content()
    print(content.encode("utf-8"))
    await browser.close()
    gl.stop()
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)