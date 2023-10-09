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

from ProjectManagerSdk.models.astroresult import AstroResult
from ProjectManagerSdk.models.changesetgetresponsedto import ChangesetGetResponseDto
import json

class ChangesetClient:
    """
    API methods related to Changeset
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_changeset(self, changeSetId: str) -> AstroResult[ChangesetGetResponseDto]:
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
            return AstroResult[ChangesetGetResponseDto](None, True, False, result.status_code, ChangesetGetResponseDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ChangesetGetResponseDto](result.json(), False, True, result.status_code, None)

    def retrieve_completed_changeset(self, changeSetId: str) -> AstroResult[ChangesetGetResponseDto]:
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
            return AstroResult[ChangesetGetResponseDto](None, True, False, result.status_code, ChangesetGetResponseDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ChangesetGetResponseDto](result.json(), False, True, result.status_code, None)
