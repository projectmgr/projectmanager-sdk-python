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

from ProjectManager.SDK.astro_result import AstroResult
from ProjectManager.SDK.models.errorresult import ErrorResult
from ProjectManager.SDK.astroresult import AstroResult
from ProjectManager.SDK.models.projectstatusdtolist import ProjectStatusDtoList

class ProjectStatusClient:
    """
    API methods related to ProjectStatus
    """
    from ProjectManager.SDK.project_manager_client import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_project_statuses(self, ) -> AstroResult[AstroResult[ProjectStatusDtoList]]:
        """
        Retrieves all ProjectStatuses defined within your Workspace.

        A ProjectStatus is a named condition used by your business to
        categorize the completion level of Tasks and Projects within
        your Workspace. You can name your ProjectStatus levels anything
        you like and you can reorganize the order of the ProjectPriority
        levels at any time.

        Parameters
        ----------
        """
        path = "/api/data/projects/statuses"
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ProjectStatusDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))
