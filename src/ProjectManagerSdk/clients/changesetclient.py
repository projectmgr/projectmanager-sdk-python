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
from ProjectManagerSdk.models.projectchangedto import ProjectChangeDto
from ProjectManagerSdk.models.projectchangestatusdto import ProjectChangeStatusDto
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class ChangesetClient:
    """
    API methods related to Changeset
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_changeset_status(self, changeSetId: str) -> AstroResult[ProjectChangeStatusDto]:
        """
        Retrieve a Changeset by its unique ID.

        A Changeset is an individual edit that has been made to a
        project. Since multiple users can edit a project at the same
        time, individual Changesets are applied in a sequential fashion.
        If a Changeset causes a conflict or cannot be applied, it will
        be rejected. You can examine a Changeset to determine its
        conflict resolution status.

        When checking the status of a Changeset, you can call either
        RetrieveChangeset or RetrieveCompletedChangeset. Using
        RetrieveChangeset will give you the immediate status of the
        Changeset. Using RetrieveCompletedChangeset will delay the
        response until the Changeset has finished processing.

        Parameters
        ----------
        changeSetId : str
            The unique ID number of the Changeset to retrieve
        """
        path = f"/api/data/changesets/{changeSetId}"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ProjectChangeStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[ProjectChangeStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ProjectChangeStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def retrieve_completed_changeset_status(self, changeSetId: str) -> AstroResult[ProjectChangeStatusDto]:
        """
        Retrieve a Changeset by its unique ID. This endpoint waits for
        the Changeset to complete its processing prior to returning a
        result.

        A Changeset is an individual edit that has been made to a
        project. Since multiple users can edit a project at the same
        time, individual Changesets are applied in a sequential fashion.
        If a Changeset causes a conflict or cannot be applied, it will
        be rejected. You can examine a Changeset to determine its
        conflict resolution status.

        When checking the status of a Changeset, you can call either
        RetrieveChangeset or RetrieveCompletedChangeset. Using
        RetrieveChangeset will give you the immediate status of the
        Changeset. Using RetrieveCompletedChangeset will delay the
        response until the Changeset has finished processing.

        Although most Changesets complete instantly, some Changesets may
        need additional time to complete. If the Changeset cannot be
        processed within a reasonable length of time, this API call may
        fail. If this API fails, it will return a status error
        indicating the Changeset is still being processed.

        Parameters
        ----------
        changeSetId : str
            The unique ID number of the Changeset to retrieve
        """
        path = f"/api/data/changesets/{changeSetId}/poll"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ProjectChangeStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[ProjectChangeStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ProjectChangeStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def retrieve_project_changes_by_project_id(self, projectId: str, version: int, page: int, take: int) -> AstroResult[list[ProjectChangeDto]]:
        """
        Retrieve specific Project Changes by Project ID

        Parameters
        ----------
        projectId : str

        version : int

        page : int

        take : int

        """
        path = f"/api/data/projects/{projectId}/changes"
        queryParams = {}
        if version:
            queryParams['version'] = version
        if page:
            queryParams['page'] = page
        if take:
            queryParams['take'] = take
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(ProjectChangeDto(**dict))
            return AstroResult[list[ProjectChangeDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[list[ProjectChangeDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
