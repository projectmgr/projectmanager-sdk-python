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
from models.licensedto import LicenseDto
import json

class LicenseClient:
    """
    API methods related to License
    """
    from projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_licenses(self) -> AstroResult[list[LicenseDto]]:
        """
        Retrieve information about the current licenses possessed by
        this Workspace.

        Licenses contain information about your current subscription
        level and features that have been enabled on your Workspace. To
        modify the License information, please log on to the
        ProjectManager.com application and use the Account | Editions
        screen to review or update your Licenses.

        Parameters
        ----------
        """
        path = "/api/data/license"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(None, True, False, result.status_code, list[LicenseDto](**json.loads(result.content)['data']))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)

    def add_license(self, bundleSku: str) -> AstroResult[list[LicenseDto]]:
        """
        Adds a new License to the current Workspace.

        Licenses contain information about your current subscription
        level and features that have been enabled on your Workspace. To
        modify the License information, please log on to the
        ProjectManager.com application and use the Account | Editions
        screen to review or update your Licenses.

        Parameters
        ----------
        bundleSku : str
            Information about the SKU you wish to add to your Workspace
        """
        path = f"/api/data/license/{bundleSku}/try"
        queryParams = {}
        result = self.client.send_request("POST", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(None, True, False, result.status_code, list[LicenseDto](**json.loads(result.content)['data']))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)
