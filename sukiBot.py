import instagram_api

# Set up the Instagram API and authenticate your app
api = instagram_api.API(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET")
api.authenticate()

# Log into your business account
api.login(username="YOUR_USERNAME", password="YOUR_PASSWORD")

# Search for the hashtags that you are interested in
hashtags = ["dog", "puppy", "villagedog"]
results = api.search_hashtags(hashtags)

# Like each of the posts that you find
for result in results:
    api.like_post(result["id"])



#todo: Set up cron job for this script to run every so often (TBD)