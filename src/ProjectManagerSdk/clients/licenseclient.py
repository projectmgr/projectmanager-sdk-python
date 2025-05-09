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
from ProjectManagerSdk.models.licensedto import LicenseDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class LicenseClient:
    """
    API methods related to License
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_licenses(self) -> AstroResult[List[LicenseDto]]:
        """
        Retrieve information about the current licenses possessed by
        this Workspace. Licenses contain information about your current
        subscription level and features that have been enabled on your
        Workspace. To modify the License information, please log on to
        the ProjectManager.com application and use the Account |
        Editions screen to review or update your Licenses.

        Parameters
        ----------
        """
        path = "/api/data/license"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=LicenseDto, data=dict))
            return AstroResult[List[LicenseDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[LicenseDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def add_license(self, bundleSku: str) -> AstroResult[List[LicenseDto]]:
        """
        Adds a new License to the current Workspace. Licenses contain
        information about your current subscription level and features
        that have been enabled on your Workspace. To modify the License
        information, please log on to the ProjectManager.com application
        and use the Account | Editions screen to review or update your
        Licenses.

        Parameters
        ----------
        bundleSku : str
            Information about the SKU you wish to add to your Workspace
        """
        path = f"/api/data/license/{bundleSku}/try"
        queryParams = {}
        result = self.client.send_request("POST", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=LicenseDto, data=dict))
            return AstroResult[List[LicenseDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[LicenseDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
