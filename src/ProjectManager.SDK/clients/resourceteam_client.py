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
from ProjectManager.SDK.models. import 
from ProjectManager.SDK.models.createresourceteamdto import CreateResourceTeamDto
from ProjectManager.SDK.models.resourceteamdto import ResourceTeamDto
from ProjectManager.SDK.models.resourceteamdtolist import ResourceTeamDtoList
from ProjectManager.SDK.models.updateresourceteamdto import UpdateResourceTeamDto

class ResourceTeamClient:
    """
    API methods related to ResourceTeam
    """
    from ProjectManager.SDK.project_manager_client import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_resource_teams(self, $top: int, $skip: int, $filter: str, $select: str, $orderby: str, $expand: str) -> AstroResult[AstroResult[ResourceTeamDtoList]]:
        """
        Retrieves all ResourceTeams defined within your Workspace that
        match an [OData formatted query](https://www.odata.org/).

        A ResourceTeam is a grouping of Resources that allows you to
        keep track of assignments in a manner consistent with your
        business needs. You can assign Resources to be members of zero,
        one, or many ResourceTeams.

        Parameters
        ----------
        $top : int
            The number of records to return
        $skip : int
            Skips the given number of records and then returns $top
            records
        $filter : str
            Filter the expression according to oData queries
        $select : str
            Specify which properties should be returned
        $orderby : str
            Order collection by this field.
        $expand : str
            Include related data in the response
        """
        path = "/api/data/resources/teams"
        result = self.client.send_request("GET", path, None, {"$top": $top, "$skip": $skip, "$filter": $filter, "$select": $select, "$orderby": $orderby, "$expand": $expand}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ResourceTeamDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_resource_team(self, body: CreateResourceTeamDto) -> AstroResult[AstroResult[ResourceTeamDto]]:
        """
        Create a Resource Team.

        Parameters
        ----------
        body : CreateResourceTeamDto
            The name of the team to create.
        """
        path = "/api/data/resources/teams"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ResourceTeamDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_resource_team(self, resourceTeamId: str) -> AstroResult[AstroResult[]]:
        """
        The endpoint is used to delete a resource team. Users assigned
        to this team will no longer be assigned thereafter.

        Parameters
        ----------
        resourceTeamId : str
            The Id of the team to be removed.
        """
        path = f"/api/data/resources/teams/{resourceTeamId}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_resource_team(self, teamresourceId: str, body: UpdateResourceTeamDto) -> AstroResult[AstroResult[ResourceTeamDto]]:
        """
        Update a Resource Team.

        Parameters
        ----------
        teamresourceId : str
            The id of the resource team
        body : UpdateResourceTeamDto
            The name of the team to Update.
        """
        path = f"/api/data/resources/teams/{teamresourceId}"
        result = self.client.send_request("PUT", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ResourceTeamDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))
