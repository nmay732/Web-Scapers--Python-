import reddit

r = reddit.Reddit(user_agent='*')

"""not case sensitive"""
print "choose a subreddit:"
subreddit = raw_input()

submissions = r.get_subreddit(subreddit).get_top(limit=None)

print "Comment Scraping..."
for submission in submissions:
    print "--SUBMISSION--"
    print submission
    print "--COMMENTS--"
    for comment in submission.comments:
            print comment
