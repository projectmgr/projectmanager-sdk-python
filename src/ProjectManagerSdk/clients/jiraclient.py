#
# ProjectManager API for Python
#
# (c) 2023-2023 ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  2023-2023 ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#

from ProjectManagerSdk.models.astroresult import AstroResult
from ProjectManagerSdk.models.retunjiraprojectsdto import RetunJiraProjectsDto
import json

class JiraClient:
    """
    API methods related to Jira
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_projects_from_jira_with_epic(self, jiraProjectId: str) -> AstroResult[RetunJiraProjectsDto]:
        """
        Retrieves a list of Projects from Jira with jiraProjectId for
        epic

        The Jira API is intended for use by ProjectManager and its
        business development partners. Please contact ProjectManager's
        sales team to request use of this API.

        Parameters
        ----------
        jiraProjectId : str
            The unique identifier of this jira project
        """
        path = f"/api/data/integrations/jira/projects/{jiraProjectId}/epics"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[RetunJiraProjectsDto](None, True, False, result.status_code, RetunJiraProjectsDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[RetunJiraProjectsDto](result.json(), False, True, result.status_code, None)

    def retrieve_projects_from_jira(self, jiraProjectId: str) -> AstroResult[RetunJiraProjectsDto]:
        """
        Retrieves a list of Projects from Jira with jiraProjectId

        The Jira API is intended for use by ProjectManager and its
        business development partners. Please contact ProjectManager's
        sales team to request use of this API.

        Parameters
        ----------
        jiraProjectId : str
            The unique identifier of this jira project
        """
        path = f"/api/data/integrations/jira/projects/{jiraProjectId}/project"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[RetunJiraProjectsDto](None, True, False, result.status_code, RetunJiraProjectsDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[RetunJiraProjectsDto](result.json(), False, True, result.status_code, None)

    def retrieve_projects_from_jira(self) -> AstroResult[list[RetunJiraProjectsDto]]:
        """
        Retrieves a list of Projects from Jira with coonectid for user

        The Jira API is intended for use by ProjectManager and its
        business development partners. Please contact ProjectManager's
        sales team to request use of this API.

        Parameters
        ----------
        """
        path = "/api/data/integrations/jira"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(RetunJiraProjectsDto(**dict))
            return AstroResult[list[RetunJiraProjectsDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[RetunJiraProjectsDto]](result.json(), False, True, result.status_code, None)
