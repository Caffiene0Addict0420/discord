from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from discord_webhook import DiscordWebhook

def startBrowser():
        #return webdriver.Chrome()
        return webdriver.PhantomJS()
        #//*[@id="101_dealView_0"]/div/div[2]
        #//*[@id="101_dealView_1"]/div/div[2]
        #//*[@id="101_dealView_2"]/div/div[2]
        #//*[@id="101_dealView_3"]/div/div[2]

def get_str(old_price, new_price, name, link, type = "Discount"):
    my_text = """
**__%s Found__** (Amazon UK)
    
**Product:** %s
**Old Price:** ~~%s~~
**New Price:** %s
**Link:** %s
    """ % (type, name, old_price, new_price, link)
    return my_text
#//*[@id="101_dealView_0"]/div/div[2]/div[0]/a
def get_webhook():
    for line in open("webhook.txt"):
        return line.strip()
        

def send_message(old_price, new_price, name, link):
    webhook = DiscordWebhook(url=get_webhook(), content=get_str(old_price, new_price, name, link))
    webhook.execute()

browser = startBrowser()
print(1)
browser.get("https://www.amazon.co.uk/gp/browse.html?node=14351804031&ref=nav_cs_gb")
print(2)
for i in range(0, 29):
    try:
        new = browser.find_element_by_xpath("//*[@id='102_dealView_0']/div/div[2]/div/div/div[3]/div[1]/span").text
    except:continue
    
    try:
        old = browser.find_element_by_xpath("//*[@id='102_dealView_%s']/div/div[2]/div/div/div[3]/div[2]/span[2]" % str(i)).text
    except:
        try:
            old = browser.find_element_by_xpath("//*[@id='102_dealView_%s']/div/div[2]/div/div/div[3]/div[1]/span" % str(i)).text
        except Exception as e:
            print(e)
            continue 
    if "-" in old:continue
    try:link = browser.find_element_by_xpath("//*[@id='102_dealView_%s']/div/div[2]/div/a" % str(i)).get_attribute('href')
    except Exception as e:
        print(e)
        continue
    name = link.split(".co.uk/")[1]
    name = name.split("/")[0]
    print((old, new, name, link))
    #send_message(old, "[new_price]", "[Testing Webhooks + Formatting]", "[Insert Link]")
print("done")
while True:pass
