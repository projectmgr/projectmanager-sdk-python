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
from ProjectManagerSdk.models.exportdto import ExportDto
from ProjectManagerSdk.models.riskexportsettingsdto import RiskExportSettingsDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class RiskClient:
    """
    API methods related to Risk
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def create_risk_export(self, projectId: str, body: RiskExportSettingsDto) -> AstroResult[ExportDto]:
        """
        Initiates a new Export action for Risks. Returns the identifier
        of this Risk Export.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project for which to export
            Risks
        body : RiskExportSettingsDto
            The settings to use for this export action
        """
        path = f"/api/data/projects/{projectId}/risks/export"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ExportDto, data=json.loads(result.content)['data'])
            return AstroResult[ExportDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ExportDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
