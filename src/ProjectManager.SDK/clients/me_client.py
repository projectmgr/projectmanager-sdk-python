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
from ProjectManager.SDK.models.workspaceuserinfodto import WorkSpaceUserInfoDto

class MeClient:
    """
    API methods related to Me
    """
    from ProjectManager.SDK.project_manager_client import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_me(self, ) -> AstroResult[AstroResult[WorkSpaceUserInfoDto]]:
        """
        Retrieve information about the currently logged on user.

        This API call will always succeed with a 200 OK if called with
        valid authentication information. If the authentication
        information provided is not valid, calling this API will return
        a 401 Authentication Failed error message. If successful, this
        API returns information about the user including its home URL,
        email address, user name, and workspace name.

        Parameters
        ----------
        """
        path = "/api/data/me"
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), WorkSpaceUserInfoDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))
