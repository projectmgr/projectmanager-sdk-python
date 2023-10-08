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
from ProjectManager.SDK.models.projectprioritydtolist import ProjectPriorityDtoList

class ProjectPriorityClient:
    """
    API methods related to ProjectPriority
    """
    from ProjectManager.SDK.project_manager_client import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_project_priorities(self, ) -> AstroResult[AstroResult[ProjectPriorityDtoList]]:
        """
        Retrieves all ProjectPriorities defined within your Workspace.

        A ProjectPriority is a named priority level used by your
        business to determine how to decide which Tasks are the most
        important. You can name your ProjectPriority levels anything you
        like and you can reorganize the order of the ProjectPriority
        levels at any time.

        Note that TaskPriority and ProjectPriority are different classes
        of priority levels. Even if they may have similar names, they
        are different objects and must be tracked separately.

        Parameters
        ----------
        """
        path = "/api/data/projects/priorities"
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ProjectPriorityDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))
