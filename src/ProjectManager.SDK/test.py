import os

from projectmanagerclient import ProjectManagerClient

def retrieve_api_key():
    API_KEY = os.environ.get('PM_API_KEY')
    if API_KEY is None:
        print('Your API key is not set.  Please configure the environment variable PM_API_KEY.')
        quit()
    else:
        return API_KEY


def create_client(apikey):
    env = 'production'
    client = ProjectManagerClient(env, 'EXAMPLE_PYTHON_APP')
    client.with_api_key(apikey)
    if not client:
        print("Problem creating client; either missing an API key or an environment.")
    else:
        return client


def main():
    API_KEY = retrieve_api_key()
    client = create_client(API_KEY)
    status_results = client.me.retrieve_me()
    print(f"StatusResult: {status_results}")
    if not status_results.success or not status_results.data:
        print("Your API key is not valid.")
        print("Please set the environment variable PM_API_KEY and PM_ENV and try again.")
        exit()
    print(f"Logged in as {status_results.data.fullName} ({status_results.data.emailAddress})")

    page_num = 0
    count = 1

    while page_num < 5:
        tasks = client.task.query_tasks(None, None, None, None, None, None)

        if tasks.data == None or len(tasks.data) == 0:
            print("No records found matching this query.")
            break

        for task in tasks.data:
            print(f"Task {count}: {task.Id}")
            count += 1

        page_num += 1



if __name__ == '__main__':
    main()