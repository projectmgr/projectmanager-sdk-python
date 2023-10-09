![PyPI - Version](https://img.shields.io/pypi/v/ProjectManagerSdk)

# ProjectManager.com SDK API v4

This software development kit contains all API definitions for the [ProjectManager.com](https://www.projectmanager.com) REST API v4 for Python.

# Why use the SDK?

The ProjectManager API v4 is available as a REST definition in OpenAPI format.  You can read the documentation online at [developer.projectmanager.com](https://developer.projectmanager.com).

# Using this SDK

Here's how to add this SDK to create a project.

```powershell
pip install ProjectManagerSdk
```

To create an API client for ProjectManager, you must specify:
* Your API key, and
* Your environment URL.

For the ProjectManager production environment, the environment URL is `https://api.projectmanager.com`.

To [obtain a ProjectManager.com API key](https://softwaredeveloper.projectmanager.com/v4/reference/api-keys):
* Log on to ProjectManager.com
* Click your name in the bottom left hand corner
* Select Account, then API
* Follow the instructions on the page to create a new API key

This example code demonstrates how to retrieve your API key from an environment variable and use it in Python:

```python
import ProjectManagerSdk
import os

# Retrieve API key and create a client
apiKey = os.environ.get('PM_API_KEY')
client = ProjectManagerSdk.ProjectManagerClient('production', 'EXAMPLE_JUPYTER_NOTEBOOK')
client.with_api_key(apiKey)

# Test connectivity to the server
status_results = client.me.retrieve_me()
if not status_results.success or not status_results.data:
    print("Your API key is not valid.")
    print("Please set the environment variable PM_API_KEY and PM_ENV and try again.")
    exit()
print(f"Logged in as {status_results.data.fullName} ({status_results.data.emailAddress})")
```
