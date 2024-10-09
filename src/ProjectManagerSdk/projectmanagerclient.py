#
# ProjectManager API for Python
#
# (c) 2023-2024 ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
#             
# @copyright  2023-2024 ProjectManager.com, Inc.
# @version    119.0.4645
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
        from ProjectManagerSdk.clients.apikeyclient import ApiKeyClient
        from ProjectManagerSdk.clients.changesetclient import ChangesetClient
        from ProjectManagerSdk.clients.dashboardclient import DashboardClient
        from ProjectManagerSdk.clients.discussionclient import DiscussionClient
        from ProjectManagerSdk.clients.fileclient import FileClient
        from ProjectManagerSdk.clients.holidayclient import HolidayClient
        from ProjectManagerSdk.clients.homefileclient import HomeFileClient
        from ProjectManagerSdk.clients.integrationcategoryclient import IntegrationCategoryClient
        from ProjectManagerSdk.clients.integrationclient import IntegrationClient
        from ProjectManagerSdk.clients.integrationproviderclient import IntegrationProviderClient
        from ProjectManagerSdk.clients.licenseclient import LicenseClient
        from ProjectManagerSdk.clients.meclient import MeClient
        from ProjectManagerSdk.clients.notificationclient import NotificationClient
        from ProjectManagerSdk.clients.nptfilesclient import NptFilesClient
        from ProjectManagerSdk.clients.projectchargecodeclient import ProjectChargeCodeClient
        from ProjectManagerSdk.clients.projectclient import ProjectClient
        from ProjectManagerSdk.clients.projectcustomerclient import ProjectCustomerClient
        from ProjectManagerSdk.clients.projectfieldclient import ProjectFieldClient
        from ProjectManagerSdk.clients.projectfileclient import ProjectFileClient
        from ProjectManagerSdk.clients.projectfolderclient import ProjectFolderClient
        from ProjectManagerSdk.clients.projectmembersclient import ProjectMembersClient
        from ProjectManagerSdk.clients.projectpriorityclient import ProjectPriorityClient
        from ProjectManagerSdk.clients.projectstatusclient import ProjectStatusClient
        from ProjectManagerSdk.clients.projecttemplateclient import ProjectTemplateClient
        from ProjectManagerSdk.clients.projectversionclient import ProjectVersionClient
        from ProjectManagerSdk.clients.resourceclient import ResourceClient
        from ProjectManagerSdk.clients.resourceskillclient import ResourceSkillClient
        from ProjectManagerSdk.clients.resourceteamclient import ResourceTeamClient
        from ProjectManagerSdk.clients.riskclient import RiskClient
        from ProjectManagerSdk.clients.tagclient import TagClient
        from ProjectManagerSdk.clients.taskassigneeclient import TaskAssigneeClient
        from ProjectManagerSdk.clients.taskclient import TaskClient
        from ProjectManagerSdk.clients.taskfieldclient import TaskFieldClient
        from ProjectManagerSdk.clients.taskfileclient import TaskFileClient
        from ProjectManagerSdk.clients.taskmetadataclient import TaskMetadataClient
        from ProjectManagerSdk.clients.taskstatusclient import TaskStatusClient
        from ProjectManagerSdk.clients.tasktagclient import TaskTagClient
        from ProjectManagerSdk.clients.teamsclient import TeamsClient
        from ProjectManagerSdk.clients.timesheetclient import TimesheetClient
        from ProjectManagerSdk.clients.userroleclient import UserRoleClient
        from ProjectManagerSdk.clients.workspaceclient import WorkSpaceClient
        self.apiKey = ApiKeyClient(self)
        self.changeset = ChangesetClient(self)
        self.dashboard = DashboardClient(self)
        self.discussion = DiscussionClient(self)
        self.file = FileClient(self)
        self.holiday = HolidayClient(self)
        self.homeFile = HomeFileClient(self)
        self.integrationCategory = IntegrationCategoryClient(self)
        self.integration = IntegrationClient(self)
        self.integrationProvider = IntegrationProviderClient(self)
        self.license = LicenseClient(self)
        self.me = MeClient(self)
        self.notification = NotificationClient(self)
        self.nptFiles = NptFilesClient(self)
        self.projectChargeCode = ProjectChargeCodeClient(self)
        self.project = ProjectClient(self)
        self.projectCustomer = ProjectCustomerClient(self)
        self.projectField = ProjectFieldClient(self)
        self.projectFile = ProjectFileClient(self)
        self.projectFolder = ProjectFolderClient(self)
        self.projectMembers = ProjectMembersClient(self)
        self.projectPriority = ProjectPriorityClient(self)
        self.projectStatus = ProjectStatusClient(self)
        self.projectTemplate = ProjectTemplateClient(self)
        self.projectVersion = ProjectVersionClient(self)
        self.resource = ResourceClient(self)
        self.resourceSkill = ResourceSkillClient(self)
        self.resourceTeam = ResourceTeamClient(self)
        self.risk = RiskClient(self)
        self.tag = TagClient(self)
        self.taskAssignee = TaskAssigneeClient(self)
        self.task = TaskClient(self)
        self.taskField = TaskFieldClient(self)
        self.taskFile = TaskFileClient(self)
        self.taskMetadata = TaskMetadataClient(self)
        self.taskStatus = TaskStatusClient(self)
        self.taskTag = TaskTagClient(self)
        self.teams = TeamsClient(self)
        self.timesheet = TimesheetClient(self)
        self.userRole = UserRoleClient(self)
        self.workSpace = WorkSpaceClient(self)
        self.serverUrl = env
        if env == "production":
            self.serverUrl = "https://api.projectmanager.com"
        self.sdkName = "Python"
        self.sdkVersion = "119.0.4645"
        self.machineName = platform.uname().node
        self.applicationName = appname
        self.bearerToken = None
    
    def with_api_key(self, key: str):
        """Configure this API client to use API Key authentication
        
        
        
        Parameters
        ----------
        key : str
            The API Key to use for authentication.
        """
        self.bearerToken = key
    
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
        if self.bearerToken:
            headers["Authorization"] = "Bearer " + self.bearerToken
    
        return requests.request(method, url, headers=headers, json=body, files=files)
        
