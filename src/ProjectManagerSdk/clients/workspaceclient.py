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
from ProjectManagerSdk.models.workspacedto import WorkSpaceDto
from ProjectManagerSdk.models.workspacesettingsupdatedto import WorkspaceSettingsUpdateDto
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

    def retrieve_current_workspace(self) -> AstroResult[List[WorkSpaceDto]]:
        """
        Returns the workspace the user is currently logged on to as a
        single-item list. This endpoint does not return every workspace
        the user can access. To switch workspaces or list all accessible
        workspaces, use workspace selection flows (for example
        `/api/data/me` and the workspace selector).

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

    def update_current_workspace_settings(self, body: WorkspaceSettingsUpdateDto) -> AstroResult[WorkSpaceDto]:
        """
        Updates workspace-level scheduling defaults for the workspace
        the user is currently logged on to, including default planned
        hours and working-day hours (Monday through Sunday). Only
        properties included in the request body are updated; omitted
        properties are left unchanged. When workingDays is provided,
        only the weekdays included in that object are updated. Values
        must be between 0 and 24.

        Parameters
        ----------
        body : WorkspaceSettingsUpdateDto
            Workspace settings to update
        """
        path = "/api/data/workspaces/settings"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=WorkSpaceDto, data=json.loads(result.content)['data'])
            return AstroResult[WorkSpaceDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[WorkSpaceDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
