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
from ProjectManagerSdk.models.dashboardsettingcreatedto import DashboardSettingCreateDto
from ProjectManagerSdk.models.dashboardsettingdto import DashboardSettingDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class DashboardClient:
    """
    API methods related to Dashboard
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_dashboard_user_settings(self, type: str) -> AstroResult[DashboardSettingDto]:
        """
        Returns user dashboard settings

        Parameters
        ----------
        type : str
            The dashboard type that is not custom
        """
        path = f"/api/data/dashboards/settings/{type}"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=DashboardSettingDto, data=json.loads(result.content)['data'])
            return AstroResult[DashboardSettingDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[DashboardSettingDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_or_update_user_dashboard_settings(self, body: DashboardSettingCreateDto) -> AstroResult[DashboardSettingDto]:
        """
        Create or Update User Dashboard Settings

        Parameters
        ----------
        body : DashboardSettingCreateDto
            User dashboard settings object
        """
        path = "/api/data/dashboards/settings"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=DashboardSettingDto, data=json.loads(result.content)['data'])
            return AstroResult[DashboardSettingDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[DashboardSettingDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
