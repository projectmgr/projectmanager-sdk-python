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
from models.projectfolderdto import ProjectFolderDto

class ProjectFolderClient:
    """
    API methods related to ProjectFolder
    """
    from projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_project_folders(self) -> AstroResult[list[ProjectFolderDto]]:
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
            return AstroResult(None, True, False, result.status_code, list[ProjectFolderDto](**json.loads(result.content)['data']))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)
