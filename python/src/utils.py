from redminelib import Redmine

def access_redmine(api_key=""):

    return Redmine("http://redmine:3000", key=api_key)

