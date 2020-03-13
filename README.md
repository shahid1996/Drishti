# Drishti : A fast HTTP response status inspector

![Drishti](https://raw.githubusercontent.com/devanshbatham/Drishti/master/static/drishti.PNG)
## What is Drishti 
**_Drishti_** is a Sanskrit word _meaning_ "**sight**" and refers to the **gazing technique** . I create this tool to gaze at the HTTP response of the urls . I created this tool for my personal use. Now making it public !

## Why 

During Recon you sometimes might get a lot of domains/subdomains/url endpoints , and ofcourse it is not possible for a normal human being to look into each domain/subdomain/url endpoint one by one (atleast not possible for me). Using **Drishti** you can automate this task, just paste the domains/urls in `raw_urls.txt` file and run the program. It will return the status code of the domains/subdomains/urls. **Drishti** uses aiohttp/asyncio which makes this tool asynchronous , and hence it is way much faster than a traditional python script using `requests` or `urllib` 

## How to use :
```
mkdir Drishti
cd Drishti
git clone https://github.com/devanshbatham/Drishti
sudo apt install python3.7 python3-venv python3.7-venv
python3.7 -m venv py37-venv
. py37-venv/bin/activate
cd Drishti
pip install -r requirements.txt
"paste the urls/domains/subdomains in raw_urls.txt"
python drishti.py
```
## Example : 

```
file : raw_urls.txt

https://google.com/
stackoverflow.com
https://facebook.com
http://twitter.com/
https://upload.twitter.com
https://platform.twitter.com
https://twitter.com/notapathxdlol
https://hackerone.com
https://test.com/nonexistentpath
```

### Output : 
![output](https://raw.githubusercontent.com/devanshbatham/Drishti/master/static/drishti2.PNG)
```
colors =>
         404            : Red
         200            : Green
         403 or 401     : Yellow
         any other code : Cyan
         
```
### Files : 
```
After the program execution is completed
Two files will be created
=> Result-200.txt    : urls with 200 OK response .
=> Result-other.txt  : urls with other than 200 response.
```
## Contact : 

[Say Hello : My twitter](https://twitter.com/0xAsm0d3us)
## Wanna show support for the tool ?

**I will be more than happy if you will show some love for Animals by donating to [Animal Aid Unlimited](https://animalaidunlimited.org/)** **,Animal Aid Unlimited saves animals through street animal rescue, spay/neuter and education. Their mission is dedicated to the day when all living beings are treated with compassion and love.** ✨
