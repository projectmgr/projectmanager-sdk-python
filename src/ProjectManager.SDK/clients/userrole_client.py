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

from ProjectManager.SDK.astro_result import AstroResult
from ProjectManager.SDK.models.errorresult import ErrorResult
from ProjectManager.SDK.astroresult import AstroResult
from ProjectManager.SDK.models.userroledtolist import UserRoleDtoList

class UserRoleClient:
    """
    API methods related to UserRole
    """
    from ProjectManager.SDK.project_manager_client import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_userroles(self, ) -> AstroResult[AstroResult[UserRoleDtoList]]:
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
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), UserRoleDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))
