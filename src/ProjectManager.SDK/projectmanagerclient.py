#
# ProjectManager API for Python
#
# (c) 2023-2023 ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
#             
# @copyright  2023-2023 ProjectManager.com, Inc.
# @version    11.1.2053
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#

import platform
import requests
import typing
import urllib.parse

from requests.models import Response

class ProjectManagerClient:
    """
    ProjectManager API API Client object
    
    Use this object to connect to the API.
    """
    apiKey: str | None
    bearerToken: str | None

    def __init__(self, env: str, appname: str):
        """Construct a new ProjectManagerClient client object
        
        Parameters
        ----------
        env : str
            Select the environment to use for this client. You may either 
            provide an environment name or a full URL of a custom environment.
        appname : str
            Provide a name for your application for logging and debugging. This
            name will be recorded alongside API calls so that you can identify
            the source of errors. 
        """
        from clients.apikeyclient import ApiKeyClient
        from clients.changesetclient import ChangesetClient
        from clients.dashboardclient import DashboardClient
        from clients.discussionclient import DiscussionClient
        from clients.fileclient import FileClient
        from clients.homefileclient import HomeFileClient
        from clients.integrationclient import IntegrationClient
        from clients.integrationcategoryclient import IntegrationCategoryClient
        from clients.integrationproviderclient import IntegrationProviderClient
        from clients.jiraclient import JiraClient
        from clients.licenseclient import LicenseClient
        from clients.meclient import MeClient
        from clients.projectclient import ProjectClient
        from clients.projectchargecodeclient import ProjectChargeCodeClient
        from clients.projectcustomerclient import ProjectCustomerClient
        from clients.projectfieldclient import ProjectFieldClient
        from clients.projectfileclient import ProjectFileClient
        from clients.projectfolderclient import ProjectFolderClient
        from clients.projectmembersclient import ProjectMembersClient
        from clients.projectpriorityclient import ProjectPriorityClient
        from clients.projectstatusclient import ProjectStatusClient
        from clients.projecttemplateclient import ProjectTemplateClient
        from clients.resourceclient import ResourceClient
        from clients.resourceskillclient import ResourceSkillClient
        from clients.resourceteamclient import ResourceTeamClient
        from clients.tagclient import TagClient
        from clients.taskclient import TaskClient
        from clients.taskassigneeclient import TaskAssigneeClient
        from clients.taskfieldclient import TaskFieldClient
        from clients.taskfileclient import TaskFileClient
        from clients.taskstatusclient import TaskStatusClient
        from clients.tasktagclient import TaskTagClient
        from clients.timesheetclient import TimesheetClient
        from clients.userroleclient import UserRoleClient
        from clients.workspaceclient import WorkSpaceClient
        self.apiKey = ApiKeyClient(self)
        self.changeset = ChangesetClient(self)
        self.dashboard = DashboardClient(self)
        self.discussion = DiscussionClient(self)
        self.file = FileClient(self)
        self.homeFile = HomeFileClient(self)
        self.integration = IntegrationClient(self)
        self.integrationCategory = IntegrationCategoryClient(self)
        self.integrationProvider = IntegrationProviderClient(self)
        self.jira = JiraClient(self)
        self.license = LicenseClient(self)
        self.me = MeClient(self)
        self.project = ProjectClient(self)
        self.projectChargeCode = ProjectChargeCodeClient(self)
        self.projectCustomer = ProjectCustomerClient(self)
        self.projectField = ProjectFieldClient(self)
        self.projectFile = ProjectFileClient(self)
        self.projectFolder = ProjectFolderClient(self)
        self.projectMembers = ProjectMembersClient(self)
        self.projectPriority = ProjectPriorityClient(self)
        self.projectStatus = ProjectStatusClient(self)
        self.projectTemplate = ProjectTemplateClient(self)
        self.resource = ResourceClient(self)
        self.resourceSkill = ResourceSkillClient(self)
        self.resourceTeam = ResourceTeamClient(self)
        self.tag = TagClient(self)
        self.task = TaskClient(self)
        self.taskAssignee = TaskAssigneeClient(self)
        self.taskField = TaskFieldClient(self)
        self.taskFile = TaskFileClient(self)
        self.taskStatus = TaskStatusClient(self)
        self.taskTag = TaskTagClient(self)
        self.timesheet = TimesheetClient(self)
        self.userRole = UserRoleClient(self)
        self.workSpace = WorkSpaceClient(self)
        self.serverUrl = env
        if env == "production":
            self.serverUrl = "api.projectmanager.com"
        self.sdkName = "Python"
        self.sdkVersion = "11.1.2053"
        self.machineName = platform.uname().node
        self.applicationName = appname
        self.apiKey = None
        self.bearerToken = None
    
    def with_api_key(self, apiKey: str):
        """Configure this API client to use API Key authentication
        
        
        
        Parameters
        ----------
        apiKey : str
            The API Key to use for authentication.
        """
        self.apiKey = apiKey
        self.bearerToken = None
    
    def with_bearer_token(self, bearerToken: str):
        """Configure this API client to use Bearer Token authentication
        
        

        Parameters
        ----------
        bearerToken : str
            The Bearer Token to use for authentication.
        """
        self.apiKey = None
        self.bearerToken = bearerToken
    
    def send_request(self, method: str, path: str, body: object, 
        query_params: typing.Dict[str, typing.Any] | None, filename: str | None) -> Response:
        """Send a request and parse the result
        
        Parameters
        ----------
        method : str
            The HTTP method for this request
        path : str
            The path of the API endpoint for this request
        body : object
            For POST, PUT, or PATCH, represents the body of the request. For other
            requests, this value should be nil.
        query_params : object
            The list of query parameters for the request
        """
        if query_params:
            url = urllib.parse.urljoin(self.serverUrl, path) + "?" + urllib.parse.urlencode(query_params)
        else:
            url = urllib.parse.urljoin(self.serverUrl, path)

        # Determine if we're uploading a file
        files = None
        if filename:
            files = { "files": open(filename, "rb") }

        headers = {"Accept": "application/json",
                   "SdkName": self.sdkName,
                   "SdkVersion": self.sdkVersion,
                   "MachineName": self.machineName,
                   "ApplicationName": self.applicationName}
        if self.apiKey:
            headers["Api-Key"] = self.apiKey
        elif self.bearerToken:
            headers["Authorization"] = "Bearer " + self.bearerToken
    
        return requests.request(method, url, headers=headers, json=body, files=files)
        
