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
from ProjectManager.SDK.models.dashboardsettingcreatedto import DashboardSettingCreateDto
from ProjectManager.SDK.models.dashboardsettingdto import DashboardSettingDto

class DashboardClient:
    """
    API methods related to Dashboard
    """
    from ProjectManager.SDK.project_manager_client import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_dashboard_user_settings(self, type: str) -> AstroResult[AstroResult[DashboardSettingDto]]:
        """
        Returns user dashboard settings

        Parameters
        ----------
        type : str
            The dashboard type that is not custom
        """
        path = f"/api/data/dashboards/settings/{type}"
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), DashboardSettingDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_or_update_user_dashboard_settings(self, body: DashboardSettingCreateDto) -> AstroResult[AstroResult[DashboardSettingDto]]:
        """
        Create or Update User Dashboard Settings

        Parameters
        ----------
        body : DashboardSettingCreateDto
            User dashboard settings object
        """
        path = "/api/data/dashboards/settings"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), DashboardSettingDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))
