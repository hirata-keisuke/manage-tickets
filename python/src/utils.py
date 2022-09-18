from redminelib import Redmine

def access_redmine(api_key=""):

    return Redmine("http://redmine", key=api_key)

