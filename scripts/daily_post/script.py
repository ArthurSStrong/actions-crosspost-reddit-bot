import os
import praw

LOG_FILE = './processed_elements.txt'
ELEMENTS_FILE = './elements.txt'

CLIENT_ID = (os.environ['CLIENT_ID'] if 'CLIENT_ID'
             in os.environ else '')
CLIENT_SECRET = (os.environ['CLIENT_SECRET'] if 'CLIENT_SECRET'
                 in os.environ else '')
USERNAME = (os.environ['USERNAME'] if 'USERNAME' in os.environ else '')
PASSWORD = (os.environ['PASSWORD'] if 'PASSWORD' in os.environ else '')

# We create the Reddit instance.

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     username=USERNAME, password=PASSWORD,
                     user_agent='testscript by /u/Disentibot')


def load_file(file):
    """Load the log file and creates it if it doesn't exist.

     Parameters
    ----------
    file : str
        The file to write down
    Returns
    -------
    list
        A list of urls.

    """

    try:
        with open(file, 'r', encoding='utf-8') as temp_file:
            return temp_file.read().splitlines()
    except Exception:

        with open(LOG_FILE, 'w', encoding='utf-8') as temp_file:
            return []


def update_file(file, data):
    """Update the log file.

    Parameters
    ----------
    file : str
        The file to write down.
    data : str
        The data to log.

    """

    with open(file, 'a', encoding='utf-8') as temp_file:
        temp_file.write(data + '\n')


def init_bot():
    elements = load_file(ELEMENTS_FILE)

    log = load_file(LOG_FILE)

    print("running script")

    for element in elements:
        if element in log:
            continue
        title = "Que chingue(n) a su madre {}...".format(element)
        body = "**Que chingue(n) a su madre {}**.\n\n_este es un bot automatizado que todo los días manda a chingar a su madre a un presidente de México_".format(element)
        print(title)
        print(body)
        reddit.subreddit("mejico").submit(title, text=body, flair_id="c3fa602e-a2a0-11eb-9d8a-0e8071724771")
        #reddit.subreddit("mejico").submit(title, text=body, flair_id="f3008236-73ad-11ea-b8b9-0ed3c0dc399d")

        update_file(LOG_FILE, element)
        break

if __name__ == '__main__':
    # Start main as a process
    init_bot()
