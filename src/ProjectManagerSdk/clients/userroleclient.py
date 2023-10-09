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
from ProjectManagerSdk.models.userroledto import UserRoleDto
import json

class UserRoleClient:
    """
    API methods related to UserRole
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_userroles(self) -> AstroResult[list[UserRoleDto]]:
        """
        Retrieves the list of UserRoles defined within this Workspace.

        A UserRole is a name for a privilege level granted to a specific
        User. The 'Global Admin' UserRole is granted to the owner of the
        Workspace, and this UserRole cannot be changed. You can choose
        which UserRole applies to a User within your Workspace.

        Parameters
        ----------
        """
        path = "/api/data/users/roles"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(UserRoleDto(**dict))
            return AstroResult[list[UserRoleDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[UserRoleDto]](result.json(), False, True, result.status_code, None)
