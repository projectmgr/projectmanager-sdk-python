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
from models.projectstatusdto import ProjectStatusDto
import json

class ProjectStatusClient:
    """
    API methods related to ProjectStatus
    """
    from projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_project_statuses(self) -> AstroResult[list[ProjectStatusDto]]:
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
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(None, True, False, result.status_code, list[ProjectStatusDto](**json.loads(result.content)['data']))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)
