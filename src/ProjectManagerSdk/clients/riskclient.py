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
from ProjectManagerSdk.models.exportdto import ExportDto
from ProjectManagerSdk.models.riskdto import RiskDto
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

    def get_risk_list(self, top: int, skip: int, filter: str, orderby: str, expand: str) -> AstroResult[List[RiskDto]]:
        """
        Retrieve a list of risks that match an [OData formatted
        query](https://www.odata.org/).

        Parameters
        ----------
        $top : int
            The number of records to return
        $skip : int
            Skips the given number of records and then returns $top
            records
        $filter : str
            Filter the expression according to oData queries
        $orderby : str
            Order collection by this field.
        $expand : str
            Include related data in the response
        """
        path = "/api/data/risks"
        queryParams = {}
        if top:
            queryParams['$top'] = top
        if skip:
            queryParams['$skip'] = skip
        if filter:
            queryParams['$filter'] = filter
        if orderby:
            queryParams['$orderby'] = orderby
        if expand:
            queryParams['$expand'] = expand
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=RiskDto, data=dict))
            return AstroResult[List[RiskDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[RiskDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
