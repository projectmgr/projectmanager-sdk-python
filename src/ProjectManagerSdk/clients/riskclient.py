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
from ProjectManagerSdk.models.riskcreatedto import RiskCreateDto
from ProjectManagerSdk.models.riskdetailsdto import RiskDetailsDto
from ProjectManagerSdk.models.riskdto import RiskDto
from ProjectManagerSdk.models.riskexportsettingsdto import RiskExportSettingsDto
from ProjectManagerSdk.models.riskupdatedto import RiskUpdateDto
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

    def get_risk(self, riskId: str) -> AstroResult[RiskDetailsDto]:
        """
        Retrieve a Risk by its unique identifier or by its short ID. A
        Risk has both a unique identifier (GUID) and a short ID that is
        unique within a Workspace.

        Parameters
        ----------
        riskId : str
            The id of the risk
        """
        path = f"/api/data/risks/{riskId}"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=RiskDetailsDto, data=json.loads(result.content)['data'])
            return AstroResult[RiskDetailsDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[RiskDetailsDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_risk(self, riskId: str, body: RiskUpdateDto) -> AstroResult[RiskDto]:
        """
        Updates an existing Risk. Only the fields provided in the
        request body will be updated. Fields omitted from the request
        will remain unchanged. Authorization is enforced to ensure the
        caller has access to modify the specified Risk.

        Parameters
        ----------
        riskId : str
            The id of the risk
        body : RiskUpdateDto
            The fields to update
        """
        path = f"/api/data/risks/{riskId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=RiskDto, data=json.loads(result.content)['data'])
            return AstroResult[RiskDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[RiskDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def remove_risk(self, riskId: str) -> AstroResult[object]:
        """
        Permanently removes the specified Risk. This operation cannot be
        undone. Any related references (such as links, history, or
        notifications) will be handled according to system rules.
        Authorization is enforced to ensure the caller has permission to
        delete the Risk.

        Parameters
        ----------
        riskId : str
            The id of the risk to remove
        """
        path = f"/api/data/risks/{riskId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def get_risks_for_project(self, projectId: str) -> AstroResult[List[RiskDetailsDto]]:
        """
        Retrieves all Risks associated with the specified Project. This
        endpoint returns a flat list of Risk summaries (not details) and
        does not use OData. Results are scoped to the Project and
        respect feature flags such as Hourly Rates.

        Parameters
        ----------
        projectId : str
            The id of the project
        """
        path = f"/api/data/risks/projects/{projectId}"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=RiskDetailsDto, data=dict))
            return AstroResult[List[RiskDetailsDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[RiskDetailsDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_risk(self, projectId: str, body: RiskCreateDto) -> AstroResult[RiskDto]:
        """
        Creates a new Risk within the specified Project. The Risk will
        inherit Project context such as access permissions and workspace
        ownership. Validation is applied to ensure the Project exists
        and the caller has permission to create Risks.

        Parameters
        ----------
        projectId : str
            The id of the project
        body : RiskCreateDto
            The data used to create the Risk
        """
        path = f"/api/data/risks/{projectId}"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=RiskDto, data=json.loads(result.content)['data'])
            return AstroResult[RiskDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[RiskDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

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

    def query_risks(self, top: int, skip: int, filter: str, orderby: str, expand: str) -> AstroResult[List[RiskDto]]:
        """
        Retrieve a list of risks that match an [OData formatted
        query](https://www.odata.org/). A Risk represents a tracked item
        of concern for a project. Risks may be categorized as Changes,
        Risks, Assumptions, Issues, or Dependencies.

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
