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
from ProjectManagerSdk.models.workspacedto import WorkSpaceDto
from ProjectManagerSdk.models.workspacejoindto import WorkSpaceJoinDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class WorkSpaceClient:
    """
    API methods related to WorkSpace
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_workspaces(self) -> AstroResult[List[WorkSpaceDto]]:
        """
        Retrieve the list of Workspaces to which the currently logged on
        user has access. A single User may have access to multiple
        Workspaces, although they can only be logged on to one Workspace
        at a time. This API lists all Workspaces to which the currently
        logged on user is entitled to access. To determine which
        Workspace a user is currently logged on use the `/api/data/me`
        endpoint.

        Parameters
        ----------
        """
        path = "/api/data/workspaces"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=WorkSpaceDto, data=dict))
            return AstroResult[List[WorkSpaceDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[WorkSpaceDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def invite_to_workspace(self, organizationId: str, body: WorkSpaceJoinDto) -> AstroResult[object]:
        """
        Invite a specific user to join a Workspace to which the current
        user has administrator rights. A single User may have access to
        multiple Workspaces, although they can only be logged on to one
        Workspace at a time. This API lists all Workspaces to which the
        currently logged on user is entitled to access. To determine
        which Workspace a user is currently logged on use the
        `/api/data/me` endpoint. This API allows you to invite a
        specific an invitation to join a specific Workspace.

        Parameters
        ----------
        organizationId : str
            The unique identifier of the Organization that you are
            inviting a User to joi
        body : WorkSpaceJoinDto
            Information about the user which will receive the invitation
        """
        path = f"/api/data/workspaces/{organizationId}/join"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
