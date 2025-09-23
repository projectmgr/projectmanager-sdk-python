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
from ProjectManagerSdk.models.nptcreatedto import NptCreateDto
from ProjectManagerSdk.models.nptdetailsdto import NptDetailsDto
from ProjectManagerSdk.models.nptdto import NptDto
from ProjectManagerSdk.models.nptupdatedto import NptUpdateDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class NptClient:
    """
    API methods related to Npt
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def get_npt(self, nptId: str) -> AstroResult[NptDetailsDto]:
        """
        Retrieve a Non-Project Task (NPT) by its unique identifier or by
        its short ID. An NPT has both a unique identifier, which is a
        GUID, and a short ID, which is a small text label that is unique
        only within your Workspace.

        A Non-Project Task (NPT) is an individual element of work that
        is outside of a project. Many people use NPTs to track personal
        work or general administrative work. NPTs have nearly all the
        same features as other tasks, but since they are not part of a
        project, they can be tracked separately by individuals.

        Parameters
        ----------
        nptId : str
            the id of the npt
        """
        path = f"/api/data/non-project-tasks/{nptId}"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=NptDetailsDto, data=json.loads(result.content)['data'])
            return AstroResult[NptDetailsDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[NptDetailsDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_npt(self, nptId: str, body: NptUpdateDto) -> AstroResult[NptDto]:
        """
        Updates a Non-Project Task (NPT) by its unique identifier, which
        is a GUID.

        A Non-Project Task (NPT) is an individual element of work that
        is outside of a project. Many people use NPTs to track personal
        work or general administrative work. NPTs have nearly all the
        same features as other tasks, but since they are not part of a
        project, they can be tracked separately by individuals.

        Parameters
        ----------
        nptId : str
            the id of the npt
        body : NptUpdateDto
            the fields to update
        """
        path = f"/api/data/non-project-tasks/{nptId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=NptDto, data=json.loads(result.content)['data'])
            return AstroResult[NptDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[NptDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def remove_npt(self, nptId: str) -> AstroResult[object]:
        """
        Removes a Non-Project Task (NPT) by its unique identifier, which
        is a GUID. A Non-Project Task (NPT) is an individual element of
        work that is outside of a project. Many people use NPTs to track
        personal work or general administrative work. NPTs have nearly
        all the same features as other tasks, but since they are not
        part of a project, they can be tracked separately by
        individuals.

        Parameters
        ----------
        nptId : str
            the id of the npt to remove
        """
        path = f"/api/data/non-project-tasks/{nptId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_npt(self, body: NptCreateDto) -> AstroResult[NptDto]:
        """
        Creates a new Non-Project Task (NPT) for the current user. If
        you specify an assignee for this NPT, that user will be assigned
        to this task. If you do not specify an assignee, the NPT will be
        automatically assigned to you. A Non-Project Task (NPT) is an
        individual element of work that is outside of a project. Many
        people use NPTs to track personal work or general administrative
        work. NPTs have nearly all the same features as other tasks, but
        since they are not part of a project, they can be tracked
        separately by individuals.

        Parameters
        ----------
        body : NptCreateDto
            The data used to create the Npt
        """
        path = "/api/data/non-project-tasks"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=NptDto, data=json.loads(result.content)['data'])
            return AstroResult[NptDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[NptDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
