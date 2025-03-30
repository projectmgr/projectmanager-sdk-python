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
from ProjectManagerSdk.models.workspaceuserinfodto import WorkSpaceUserInfoDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class MeClient:
    """
    API methods related to Me
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_me(self) -> AstroResult[WorkSpaceUserInfoDto]:
        """
        Retrieve information about the currently logged on user. This
        API call will always succeed with a 200 OK if called with valid
        authentication information. If the authentication information
        provided is not valid, calling this API will return a 401
        Authentication Failed error message. If successful, this API
        returns information about the user including its home URL, email
        address, user name, and workspace name.

        Parameters
        ----------
        """
        path = "/api/data/me"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=WorkSpaceUserInfoDto, data=json.loads(result.content)['data'])
            return AstroResult[WorkSpaceUserInfoDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[WorkSpaceUserInfoDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_my_avatar(self, fileName: str) -> AstroResult[object]:
        """
        Updates the logged in user avatar

        Parameters
        ----------
        fileName : str
            The full path of a file to upload to the API
        """
        path = "/api/data/me/avatar"
        queryParams = {}
        result = self.client.send_request("POST", path, None, queryParams, fileName)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
