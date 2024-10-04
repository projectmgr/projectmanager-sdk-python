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
from ProjectManagerSdk.models.projectversiondto import ProjectVersionDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class ProjectVersionClient:
    """
    API methods related to ProjectVersion
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_project_versions(self, projectId: str) -> AstroResult[List[ProjectVersionDto]]:
        """
        Returns projects versions including version, user who made
        changes

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project
        """
        path = f"/api/data/projects/{projectId}/versions"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=ProjectVersionDto, data=dict))
            return AstroResult[List[ProjectVersionDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[ProjectVersionDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def download_msproject_xml(self, projectChangeId: str) -> AstroResult[bytes]:
        """
        Exports and returns project version as an MS Project XML
        attachment

        Parameters
        ----------
        projectChangeId : str
            Project change Guid
        """
        path = f"/api/data/projects/{projectChangeId}/version/download"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[bytes](None, True, False, result.status_code, result.content)
        else:
            response = AstroResult[bytes](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def restore_project_version(self, projectId: str, version: int) -> AstroResult[object]:
        """
        Restores a Project to the state it was in at a specific Version
        in time. If successful, all changes made to the Project since
        this Version will be undone and the Project will return to its
        former state.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project to restore
        version : int
            The version number to restore to
        """
        path = f"/api/data/projects/{projectId}/version/{version}/restore"
        queryParams = {}
        result = self.client.send_request("POST", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def copy_project_version(self, projectId: str, version: int, timezoneOffset: int) -> AstroResult[object]:
        """
        Create a Copy of a Project as of a specific Version, optionally
        moving it to a new Timezone.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project to copy
        version : int
            The version number of the Project to copy
        timezoneOffset : int
            If specified, sets the default timezone of the newly copied
            Project to this specified timezone
        """
        path = f"/api/data/projects/{projectId}/version/{version}/copy"
        queryParams = {}
        if timezoneOffset:
            queryParams['timezoneOffset'] = timezoneOffset
        result = self.client.send_request("POST", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
