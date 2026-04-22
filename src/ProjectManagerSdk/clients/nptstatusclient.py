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
from ProjectManagerSdk.models.nptstatuscreatedto import NptStatusCreateDto
from ProjectManagerSdk.models.nptstatusdto import NptStatusDto
from ProjectManagerSdk.models.nptstatusupdatedto import NptStatusUpdateDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class NptStatusClient:
    """
    API methods related to NptStatus
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def get_npt_task_statuses(self) -> AstroResult[List[NptStatusDto]]:
        """
        Get a list of task statuses that can be used by non-protect
        tasks.

        Parameters
        ----------
        """
        path = "/api/data/non-project-tasks/statuses"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=NptStatusDto, data=dict))
            return AstroResult[List[NptStatusDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[NptStatusDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_npt_task_status(self, body: NptStatusCreateDto) -> AstroResult[NptStatusDto]:
        """
        Creates a new status level for non-project tasks.

        Parameters
        ----------
        body : NptStatusCreateDto
            Information about the new status level to create
        """
        path = "/api/data/non-project-tasks/statuses"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=NptStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[NptStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[NptStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_npt_task_status(self, nptStatusId: str, body: NptStatusUpdateDto) -> AstroResult[NptStatusDto]:
        """
        Updates an existing status level for non-project tasks.

        Parameters
        ----------
        nptStatusId : str
            The unique identifier of the status to update
        body : NptStatusUpdateDto
            Information about the status level to update
        """
        path = f"/api/data/non-project-tasks/statuses/{nptStatusId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=NptStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[NptStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[NptStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def delete_npt_task_status(self, nptStatusId: str) -> AstroResult[object]:
        """
        Deletes an existing status level for non-project tasks. You will
        not be able to delete a status if there are tasks assigned to it
        or if it is the default status level.

        Parameters
        ----------
        nptStatusId : str
            The unique identifier of the status to delete
        """
        path = f"/api/data/non-project-tasks/statuses/{nptStatusId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
