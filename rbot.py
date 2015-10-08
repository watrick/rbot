import praw
import time

r = praw.Reddit(user_agent = "pfed bot by pfed /u/pfedsays")
r.login()
print("logging in")
words_to_match = ['pfed?', 'pfed!', 'pfedsays']
cache = []

def run_bot():
    print("Grabbing subreddit...")
    subreddit = r.get_subreddit("shitpfedsays")
    print("Grabbing comments...")
    comments = subreddit.get_comments(limit=25)
    for comment in comments:
        comment_text = comment.body.lower()
        isMatch = any(string in comment_text for string in words_to_match)
        if comment.id not in cache and isMatch:
            print("Match Found! Comment ID " + comment.id)
            cache.append(comment.id)
            cache.append(comment.body)
            print("added to cache")
            print(cache)
            comment.reply('this is a test message from pfedbot, pleaze ignore')
            print("reply succesful")
    print("loop finished, sleep")


while True:
    try:
        run_bot()
    except praw.errors.PRAWException:
        print("Comment to old, looking again")
    time.sleep(15)
