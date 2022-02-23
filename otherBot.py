# imports
from instapy import InstaPy
from instapy import smart_run
from credentials import username, password

# login credentials
insta_username = username
insta_password = password

# comments = ['Nice shot! @{}',
#             'I love your profile! @{}',
#             'Your feed is an inspiration :thumbsup:',
#             'Just incredible :open_mouth:',
#             'What camera did you use @{}?',
#             'Love your posts @{}',
#             'Looks awesome @{}',
#             'Getting inspired by you @{}',
#             ':raised_hands: Yes!',
#             'I can feel your passion @{} :muscle:']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    # session.set_dont_include(["friend1", "friend2", "friend3"])
    # session.set_dont_like(["pizza", "#store"])

    # activities

    """ Massive Follow of users followers (I suggest to follow not less than
    3500/4000 users for better results)...
    """
    session.follow_user_followers(['goodfoodmix'], amount=600,
                                  randomize=False, interact=False)