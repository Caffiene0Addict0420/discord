from discord_webhook import DiscordWebhook

def get_str(old_price, new_price, name, link):
    my_text = """
    **__Product Found__**
    
    **Name:** %s
    **Old Price:** %s
    **New Price:** %s
    **Link:** %s
    """ % (name, old_price, new_price, link)
    return my_text

def get_webhook():
    for line in open("webhook.txt"):
        return line.strip()
        

def send_message(old_price, new_price, name, link):
    webhook = DiscordWebhook(url=get_webhook(), content=get_str(old_price, new_price, name, link))
    webhook.execute()

send_message("[old price]", "[new_price]", "[Testing Webhooks + Formatting]", "[Insert Link]")