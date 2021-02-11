from fake_useragent import UserAgent

def gen_user_agent(test_mode=False):
    return UserAgent().random