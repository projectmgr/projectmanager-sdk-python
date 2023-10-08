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
from ProjectManager.SDK.models.projectfolderdtolist import ProjectFolderDtoList

class ProjectFolderClient:
    """
    API methods related to ProjectFolder
    """
    from ProjectManager.SDK.project_manager_client import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_project_folders(self, ) -> AstroResult[AstroResult[ProjectFolderDtoList]]:
        """
        Retrieves all ProjectFolders defined within your Workspace.

        A ProjectFolder is a named storage location that can contain
        Projects.

        Parameters
        ----------
        """
        path = "/api/data/project-folders"
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ProjectFolderDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))
