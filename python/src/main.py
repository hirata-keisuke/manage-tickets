import argparse

from utils import access_redmine

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Redmineにアクセスする')
    parser.add_argument("api_key", help="API Key")

    args = parser.parse_args()

    redmine = access_redmine(args.api_key)

    print(redmine.issue.get(10).subject)