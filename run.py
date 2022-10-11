from discord_webhook import DiscordWebhook
import dweepy
import argparse

# argument parser
ap = argparse.ArgumentParser(description='Forward new dweets to discord via webhook.')

# Add the arguments to the parser
ap.add_argument("-w", "--webhook", required=True,
   help="Discord webhook url")
ap.add_argument("-t", "--thing", required=True,
   help="Thing name on dweet.io to listen for")
ap.add_argument("-d", "--debug", default=False, action='store_const', const=True,
   help="Run in debug mode")
args = vars(ap.parse_args())

# parsed arguments
webhookurl = args['webhook']
thing = args["thing"]

webhook = DiscordWebhook(url=webhookurl, content='Starting dweet.io grabber')
if args["debug"]:
    response = webhook.execute()
    print(response)

print("Opening chunked http")
for dweet in dweepy.listen_for_dweets_from('techtec'):
    if "content" in dweet and "zprava" in dweet["content"]:
        webhook.content = dweet["content"]["zprava"]
        response = webhook.execute()
        print(dweet["content"]["zprava"])
        if args["debug"]:
            print(response)

