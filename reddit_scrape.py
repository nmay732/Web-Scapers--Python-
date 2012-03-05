"""
Notes:
***UNSOLVED PROBLEM*** comments longer than 77 chars get cut with a "..." 
-Orders submissions by most upvotes NOT chronological
-Comments include "[deleted]" for deleted comments
-Subreddit input isn't case sensitive
-Set limit to "None" for no limit
-Reddit API limits to two requests / sec
-Currently overwites outfiles if it already exists
"""

import sys
import os
import reddit

usage = "python reddit_scrape.py subreddit limit outfile"

if len(sys.argv) < 4:
    print "\nABORTED: Too few args"
    print usage
    sys.exit();

if sys.argv[2] != 'None':
    limit_in = int(sys.argv[2])
else:
    limit_in = sys.argv[2]

r = reddit.Reddit(user_agent='*')

submissions = r.get_subreddit(sys.argv[1]).get_top(limit=limit_in)

if not os.path.isfile(sys.argv[3]):
    open(sys.argv[3], 'w').close()

with open(sys.argv[3], 'w') as f:
    print "Submissions scraped:"
    count = 0
    for submission in submissions:
        count += 1
        print count
        f.write("--SUBMISSION--\n")
        f.write(str(submission) + "\n")
        f.write("--COMMENTS--\n")
        for comment in submission.comments:
            f.write(str(comment) + "\n")
