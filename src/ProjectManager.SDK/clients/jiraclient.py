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

from models.astroresult import AstroResult
from models.retunjiraprojectsdto import RetunJiraProjectsDto

class JiraClient:
    """
    API methods related to Jira
    """
    from projectmanagerclient import ProjectManagerClient

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
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(None, True, False, result.status_code, RetunJiraProjectsDto(result.json(), RetunJiraProjectsDto))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)

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
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(None, True, False, result.status_code, RetunJiraProjectsDto(result.json(), RetunJiraProjectsDto))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)

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
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(None, True, False, result.status_code, list[RetunJiraProjectsDto](result.json(), list[RetunJiraProjectsDto]))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)
