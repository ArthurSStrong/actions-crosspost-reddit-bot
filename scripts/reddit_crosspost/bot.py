#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Look on one subredit and crosspost submissions with certain conditions.
"""

import os
import praw
from datetime import datetime
from datetime import timedelta

CLIENT_ID = (os.environ['CLIENT_ID'] if 'CLIENT_ID'
             in os.environ else '')
CLIENT_SECRET = (os.environ['CLIENT_SECRET'] if 'CLIENT_SECRET'
                 in os.environ else '')
USERNAME = (os.environ['USERNAME'] if 'USERNAME' in os.environ else '')
PASSWORD = (os.environ['PASSWORD'] if 'PASSWORD' in os.environ else '')


def init_bot():
    """Initilize Praw and explore sub by new."""

    # We create the Reddit instance.

    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         username=USERNAME, password=PASSWORD,
                         user_agent='testscript by /u/Disentibot')

    tolerance_time = datetime.today() - timedelta(hours=4)

    for submission in reddit.subreddit('mexico').new(limit=100):
        submission_date = datetime.fromtimestamp(submission.created_utc)
        if submission_date >= tolerance_time:
            if submission.link_flair_text is None:
              continue
            if any(submission.link_flair_text in s for s in ['Humor',
                   'Noticias', 'Meme', 'Ask Mexico', 'Info']):
                print(submission.title)
                submission.crosspost('mejico', title=submission.title,
                        send_replies=False)


if __name__ == '__main__':

    init_bot()
