#
# ProjectManager API for Python
#
# (c) ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#

from ProjectManagerSdk.models.astroresult import AstroResult
from ProjectManagerSdk.models.projectstatuscreatedto import ProjectStatusCreateDto
from ProjectManagerSdk.models.projectstatusdto import ProjectStatusDto
from ProjectManagerSdk.models.projectstatusupdatedto import ProjectStatusUpdateDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class ProjectStatusClient:
    """
    API methods related to ProjectStatus
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_project_statuses(self) -> AstroResult[List[ProjectStatusDto]]:
        """
        Retrieves all ProjectStatuses defined within your Workspace. A
        ProjectStatus is a named condition used by your business to
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
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=ProjectStatusDto, data=dict))
            return AstroResult[List[ProjectStatusDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[ProjectStatusDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_project_status(self, body: ProjectStatusCreateDto) -> AstroResult[ProjectStatusDto]:
        """
        Create a project Status

        Parameters
        ----------
        body : ProjectStatusCreateDto
            The data to create the Status
        """
        path = "/api/data/projects/statuses"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ProjectStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[ProjectStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ProjectStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_project_status(self, projectStatusId: str, body: ProjectStatusUpdateDto) -> AstroResult[ProjectStatusDto]:
        """
        Update a project Status

        Parameters
        ----------
        projectStatusId : str
            The status Id
        body : ProjectStatusUpdateDto
            The data to create the Status
        """
        path = f"/api/data/projects/statuses/{projectStatusId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ProjectStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[ProjectStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ProjectStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def delete_project_status(self, projectStatusId: str) -> AstroResult[object]:
        """
        Delete a project Status

        Parameters
        ----------
        projectStatusId : str
            The status Id
        """
        path = f"/api/data/projects/statuses/{projectStatusId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
