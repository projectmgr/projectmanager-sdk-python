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
# @version    11.1.2012
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
        from ProjectManager.SDK.clients.api_key_client import ApiKeyClient
        from ProjectManager.SDK.clients.changeset_client import ChangesetClient
        from ProjectManager.SDK.clients.dashboard_client import DashboardClient
        from ProjectManager.SDK.clients.discussion_client import DiscussionClient
        from ProjectManager.SDK.clients.file_client import FileClient
        from ProjectManager.SDK.clients.home_file_client import HomeFileClient
        from ProjectManager.SDK.clients.integration_client import IntegrationClient
        from ProjectManager.SDK.clients.integration_category_client import IntegrationCategoryClient
        from ProjectManager.SDK.clients.integration_provider_client import IntegrationProviderClient
        from ProjectManager.SDK.clients.jira_client import JiraClient
        from ProjectManager.SDK.clients.license_client import LicenseClient
        from ProjectManager.SDK.clients.me_client import MeClient
        from ProjectManager.SDK.clients.project_client import ProjectClient
        from ProjectManager.SDK.clients.project_charge_code_client import ProjectChargeCodeClient
        from ProjectManager.SDK.clients.project_customer_client import ProjectCustomerClient
        from ProjectManager.SDK.clients.project_field_client import ProjectFieldClient
        from ProjectManager.SDK.clients.project_file_client import ProjectFileClient
        from ProjectManager.SDK.clients.project_folder_client import ProjectFolderClient
        from ProjectManager.SDK.clients.project_members_client import ProjectMembersClient
        from ProjectManager.SDK.clients.project_priority_client import ProjectPriorityClient
        from ProjectManager.SDK.clients.project_status_client import ProjectStatusClient
        from ProjectManager.SDK.clients.project_template_client import ProjectTemplateClient
        from ProjectManager.SDK.clients.resource_client import ResourceClient
        from ProjectManager.SDK.clients.resource_skill_client import ResourceSkillClient
        from ProjectManager.SDK.clients.resource_team_client import ResourceTeamClient
        from ProjectManager.SDK.clients.tag_client import TagClient
        from ProjectManager.SDK.clients.task_client import TaskClient
        from ProjectManager.SDK.clients.task_assignee_client import TaskAssigneeClient
        from ProjectManager.SDK.clients.task_field_client import TaskFieldClient
        from ProjectManager.SDK.clients.task_file_client import TaskFileClient
        from ProjectManager.SDK.clients.task_status_client import TaskStatusClient
        from ProjectManager.SDK.clients.task_tag_client import TaskTagClient
        from ProjectManager.SDK.clients.timesheet_client import TimesheetClient
        from ProjectManager.SDK.clients.user_role_client import UserRoleClient
        from ProjectManager.SDK.clients.work_space_client import WorkSpaceClient
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
        self.sdkVersion = "11.1.2012"
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
        
