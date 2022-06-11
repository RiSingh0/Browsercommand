from distutils.log import debug
from flask import Flask, render_template
from flask import Flask, request, jsonify
import start as st
import clean as cl
import activetab as at
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/start', methods=["POST","GET"])
def start():
    # print(request.args["browser"],request.args["url"])
    browserName=""
    url=""
    if "browser" in request.args:
        browserName = request.args["browser"]
    if "url" in request.args:
        url = request.args["url"]

    browObject=st.StratBrowsure(browserName,url)
    flag=browObject.start()

    if flag:
        return "Everything is perfect"
    else:
        return "Somthing went wrong"


@app.route('/stop', methods=["POST","GET"])
def stop():
    browser_name=""
    if "browser" in request.args:
        browser_name = request.args["browser"]

    if browser_name == "chrome":
        os.system("taskkill /F /IM chrome.exe")
        return "CHROME CLOSED"
    elif browser_name == "firefox":
        os.system("taskkill /F /IM firefox.exe")
        return "FIREFOX CLOSED"

    return "This browser is not available"


@app.route('/cleanup', methods=["POST","GET"])
def cleanup():

    browser_name=""
    if "browser" in request.args:
        browser_name = request.args["browser"]

    if browser_name == "chrome":
        flag = cl.clear_history_chrome()
        if flag:
            return "CHROME CLEANED"
        else:
            return "Somthing went wrong"
    elif browser_name == "firefox":
        flag = cl.clear_history_firefox()
        if flag:
            return "FIREFOX CLEANED"
        else:
            return "Somthing went wrong"

    return "Browser support not available"


@app.route('/geturl', methods=["POST","GET"])
def geturl():
    browser_name=""
    if "browser" in request.args:
        browser_name = request.args["browser"]
    if browser_name == "chrome":
        return "Active Tab URL is : "+str(at.chrome_active_url())
    elif browser_name == "firefox":
        return "Active Tab URL is : "+str(at.firefox_active_url())
    return jsonify(request.args)

if __name__ == "__main__":
    app.run(debug=True)