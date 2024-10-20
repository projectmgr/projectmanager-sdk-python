#
# ProjectManager API for Python
#
# (c) 2023-2024 ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  2023-2024 ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#

from ProjectManagerSdk.models.astroresult import AstroResult
from ProjectManagerSdk.models.projectfolderdto import ProjectFolderDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class ProjectFolderClient:
    """
    API methods related to ProjectFolder
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_project_folders(self) -> AstroResult[List[ProjectFolderDto]]:
        """
        Retrieves all ProjectFolders defined within your Workspace. A
        ProjectFolder is a named storage location that can contain
        Projects.

        Parameters
        ----------
        """
        path = "/api/data/project-folders"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=ProjectFolderDto, data=dict))
            return AstroResult[List[ProjectFolderDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[ProjectFolderDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
