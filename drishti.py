'''
A FAST HTTP RESPONSE STATUS INSPECTOR
'''


import time
import os
import sys
import aiohttp
import asyncio
from aiohttp import *
start_time = time.time()


def main():
    asyncio.run(download_url_contents())


def collector_alive(uri ):
    with open('Results-200.txt', 'a') as f1:
        f1.write(uri+"\n")

def collector_alive_but_other(uri):
    with open('Results-other.txt', 'a') as f2:
        f2.write(uri+"\n")

async def download_url_contents():
    async with aiohttp.ClientSession() as session:
        await gen_url_tasks(session, 'raw_urls.txt')
async def fetch_url(session, url):
    # Get the response text of the supplied url
    try:
        async with session.get(url) as response:
            reason = response.reason
            status = response.status

            if status == 404: # status other than 200
                collector_alive_but_other(url)
                print(f"\u001b[31;1m[{status}]  : {url}  \u001b[0m")
                pass
            elif status == 200: # status : 200
                # print(f"{url} : {status} {reason}")
                collector_alive(url)
                print(f"\u001b[32;1m[{status}]  : {url} \u001b[0m")
            elif status==401 or status == 403:
                collector_alive_but_other(url)
                print(f"\u001b[33m[{status}]  : {url} \u001b[0m")
            else:
                collector_alive_but_other(url)
                print(f"\u001b[36m[{status}]  : {url} \u001b[0m")
    except ClientConnectorError:
        return (url, 500) 
    except ClientOSError:
        return (url, 500)
    except ServerDisconnectedError:
        return (url,500)
    except asyncio.TimeoutError:
        return (url, 500)
    except UnicodeDecodeError:
        return (url, 500)
    except TooManyRedirects:
        return (url, 500)
    except ServerTimeoutError:
        return (url, 500)
    except ServerConnectionError:
        return (url, 500)
    except RuntimeError:
        pass

async def gen_url_tasks(session, url_list):
    # Generate the tasks for each url in supplied url list.

    with open('raw_urls.txt' , 'r' , encoding='utf-8') as f:
	    temp_urls = f.read().splitlines()

    urls = []
    for url in temp_urls:
        if "http://" and "https://" not in url:
            urls.append(f"https://{url}")
            urls.append(f"http://{url}")
        
        else : 
            urls.append(url)


    tasks = []
    for url in urls:
        task = asyncio.ensure_future(fetch_url(session, url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    print(f"\n    \u001b[36;1m[+] URLs Checked  : {len(urls)}\u001b[0m\n")
    return results

if __name__ == "__main__":
    if os.name =="nt":
        os.system("cls")
    banner = """\u001b[36m

            ██▄   █▄▄▄▄ ▄█    ▄▄▄▄▄    ▄  █    ▄▄▄▄▀ ▄█ 
            █  █  █  ▄▀ ██   █     ▀▄ █   █ ▀▀▀ █    ██ 
            █   █ █▀▀▌  ██ ▄  ▀▀▀▀▄   ██▀▀█     █    ██ 
            █  █  █  █  ▐█  ▀▄▄▄▄▀    █   █    █     ▐█ 
            ███▀    █    ▐               █    ▀       ▐ 
                   ▀                    ▀               
                         -coded with <3 by Devansh Batham
\u001b[0m

    """
    print(banner)
    time.sleep(0.5)
    assert sys.version_info >= (3, 7), "Use Python 3.7+"
    if not os.path.isfile('raw_urls.txt'):
        print("\u001b[31m  [!]File raw_urls.txt does not exist ! ")
        quit()
    print(" \u001b[32m[~] Loading URLs")
    time.sleep(0.5)
    print(
        " \u001b[32m[~] Sending Requests\n")

    if os.path.isfile('Results-200.txt'):
        os.remove("Results-200.txt")
    if os.path.isfile('Results-other.txt'):
        os.remove("Results-other.txt")

    main()
    print("\n \u001b[31m [!] Total execution time    : %ss\u001b[0m" % str((time.time() - start_time))[:-12])