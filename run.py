from flask import Flask, render_template, request
from user_agents import parse
import logging
from urllib.request import urlopen
from json import load

app = Flask(__name__)


def ipInfo(addr):
    addr = addr.split(":")[0]
    url = "https://ipinfo.io/{0}?token=66b474300a8af1".format(addr)
    print(url)
    res = urlopen(url)
    data = load(res)
    return data


@app.route("/")
def index():
    return render_template("check.html")


@app.route("/weather", methods=["GET", "POST"])
def weather():
    return render_template("weather.html")


@app.route("/postman", methods=["POST"])
def postman():
    content = request.json
    data = request.headers
    ua_string = data["User-Agent"]
    user_agent = parse(ua_string)
    location = ipInfo(content["ip"])

    app.logger.info(
    f"""
    IP: {location['ip']}
    City: {location['city']}
    Region: {location['region']}
    ISP: {location['org']}
    Host: {data['Host']}
    browser: {user_agent.browser.family}
    browser version: {user_agent.browser.version_string}
    OS: {user_agent.os.family}
    OS Version: {user_agent.os.version_string}
    Machine Family: {user_agent.device.family}
    Machine Brand: {user_agent.device.brand}
    Is PC: {user_agent.is_pc}
    """)
    values= {"IP": location['ip'],
    "City": location['city'],
    "Region": location['region'],
    "ISP": location['org'],
    "Host": data['Host'],
    "browser": user_agent.browser.family,
    "browser version": user_agent.browser.version_string,
    "OS": user_agent.os.family,
    "OS Version": user_agent.os.version_string,
    "Machine Family": user_agent.device.family,
    "Machine Brand": user_agent.device.brand,
    "Is PC": user_agent.is_pc}
    app.logger.info( values)
    return {}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8989)
