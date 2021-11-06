# Project 1
( BAU ) CYS5123 (1) Web App. Security: Hacking&Defence 21/22 (1)

----
 
Name: Ali Baker

Sid: 2100518
 
---

### Intro:
Most of website tracks user online activity and collecting data such as technology and geo location info, those data can be used to personalize the best content for you, beside it's could expose your information. (privacyrights.org, 1995)

In this project the following data has been collected using the JavaScript, Python code.


* Current location (as determined by IP AddressGeolocation).
* Current IP Address.
* Browser type and version number.
* Whether Web cookies are enabled or not.
* Whether the browser is in Private Browsing Mode.
* Screen resolution and color depth.
* User's installed browser plugins list.
* User's home webpage.
* Which of the Top 100 websites that the user has visited.


## Run project
### Requirements
* Docker
* docker-compose

### Running pojects
Follow the below commands:
```
docker-compose build
docker-compose up
```
Or
```
docker image build . -t bau:proj1
docker container run -ti -p 0.0.0.0:8989:8989 bau:proj1
```
### Home page `127.0.0.1:8989/`

* Then from the browser access `127.0.0.1:8989`
* Under docker logs you will see extra user info.
* under page `http://127.0.0.1:8989/weather` you will find all user info


### How it work

```
"Your city " + geoplugin_city() + ", Country " + geoplugin_countryName()
"Your IP adress " + geoplugin_request())
"Top 100 websites: I can't get them 👽️")
var result = bowser.getParser(window.navigator.userAgent
"You are browsing using " + result.parsedResult.browser.name + " Version " + result.parsedResult.browser.version + " On " + result.parsedResult.os.name + "/" + result.parsedResult.platform.type
if (navigator.cookieEnabled) {
    "Cookies are enabled"
} else {
    "Cookies is not enabled"
}
isPrivateWindow(function(is_private) {
    document.getElementById('result').innerHTML = is_private === null ? 'cannot detect' : is_private ? 'Browsing in private mode <span>👻</span>' : 'Browsing in normal mode<span></span>';
}
var client = new ClientJS(
var currentResolution = client.getCurrentResolution(
var colorDepth = client.getColorDepth(
var plugins = client.getPlugins(
"Your Screen Resolution: ", currentResolution 
"Your Screen Color Depth: ", colorDepth 
"The Plugins List if any: ", plugins 

```

### Geolocation Usages  (Mitchell, 2020)
* Manage Websites: Website creators use a geolocation service to track the geographic distribution of visitors to their site.
* Enforce the Law: The Recording Industry Association of America and other agencies may use geolocation to find people who illegally swap media files on the internet, although typically they work directly with internet service providers.
* Find Spammers: Individuals being harassed online often trace the IP address of the email or instant messages.

### Geolocation limitation
* IP addresses may be associated with the wrong.
* Addresses may be associated only with a broad geographic.
* Some addresses do not appear in the database and therefore cannot be mapped.

----

### Open source libraries used under the project 
1.	UNPKG bowser: A small, fast and rich-API browser/platform/engine detector for both browser and node. (lancedikson, 2020)
2.	ClientJS: Device information and digital fingerprinting written in pure JavaScript. (jackspirou, 2020)
3.	Bluebirdjs: retrieve the fulfillment value of an already fulfilled promise or the rejection reason (bluebirdjs, 2021)
4.	Nicepage: websites creator. (nicepage.com, 2021)

---

### Works Cited
* privacyrights.org, 1995. Online Privacy: Using the Internet Safely. [Online] 
Available at: https://privacyrights.org/consumer-guides/online-privacy-using-internet-safely
[Accessed 06 11 2021].
* Mitchell, B., 2020. Does IP Address Location (Geolocation) Really Work?. [Online] 
Available at: https://www.lifewire.com/does-ip-address-*  geolocation-really-work-818154
[Accessed 6 11 2021].
lancedikson, 2020. bowser. [Online] 
Available at: https://github.com/lancedikson/bowser/releases/tag/2.10.0
[Accessed 06 11 2021].
*  jackspirou, 2020. clientjs.org. [Online] 
Available at: https://clientjs.org/
[Accessed 06 11 2021].
*  bluebirdjs, 2021. bluebirdjs. [Online] 
Available at: http://bluebirdjs.com/docs/features.html
[Accessed 6 11 2021].
*  nicepage.com, 2021. nicepage.com. [Online] 
Available at: https://nicepage.com/
[Accessed 6 11 2021].