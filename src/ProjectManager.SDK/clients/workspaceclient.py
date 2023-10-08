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
from models.workspacedto import WorkSpaceDto
from models.workspacejoindto import WorkSpaceJoinDto

class WorkSpaceClient:
    """
    API methods related to WorkSpace
    """
    from projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_workspaces(self) -> AstroResult[list[WorkSpaceDto]]:
        """
        Retrieve the list of Workspaces to which the currently logged on
        user has access.

        A single User may have access to multiple Workspaces, although
        they can only be logged on to one Workspace at a time. This API
        lists all Workspaces to which the currently logged on user is
        entitled to access. To determine which Workspace a user is
        currently logged on use the `/api/data/me` endpoint.

        Parameters
        ----------
        """
        path = "/api/data/workspaces"
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(None, True, False, result.status_code, list[WorkSpaceDto](result.json(), list[WorkSpaceDto]))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)

    def invite_to_workspace(self, organizationId: str, body: WorkSpaceJoinDto) -> AstroResult[object]:
        """
        Invite a specific user to join a Workspace to which the current
        user has administrator rights.

        A single User may have access to multiple Workspaces, although
        they can only be logged on to one Workspace at a time. This API
        lists all Workspaces to which the currently logged on user is
        entitled to access. To determine which Workspace a user is
        currently logged on use the `/api/data/me` endpoint.

        This API allows you to invite a specific an invitation to join a
        specific Workspace.

        Parameters
        ----------
        organizationId : str
            The unique identifier of the Organization that you are
            inviting a User to joi
        body : WorkSpaceJoinDto
            Information about the user which will receive the invitation
        """
        path = f"/api/data/workspaces/{organizationId}/join"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(None, True, False, result.status_code, object(result.json(), object))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)
