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

from ProjectManagerSdk.models.astroresult import AstroResult
from ProjectManagerSdk.models.createresourceteamdto import CreateResourceTeamDto
from ProjectManagerSdk.models.resourceteamdto import ResourceTeamDto
from ProjectManagerSdk.models.updateresourceteamdto import UpdateResourceTeamDto
import json

class ResourceTeamClient:
    """
    API methods related to ResourceTeam
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_resource_teams(self, top: int, skip: int, filter: str, select: str, orderby: str, expand: str) -> AstroResult[list[ResourceTeamDto]]:
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
        queryParams = {}
        if top:
            queryParams['$top'] = top
        if skip:
            queryParams['$skip'] = skip
        if filter:
            queryParams['$filter'] = filter
        if select:
            queryParams['$select'] = select
        if orderby:
            queryParams['$orderby'] = orderby
        if expand:
            queryParams['$expand'] = expand
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(ResourceTeamDto(**dict))
            return AstroResult[list[ResourceTeamDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[ResourceTeamDto]](result.json(), False, True, result.status_code, None)

    def create_resource_team(self, body: CreateResourceTeamDto) -> AstroResult[ResourceTeamDto]:
        """
        Create a Resource Team.

        Parameters
        ----------
        body : CreateResourceTeamDto
            The name of the team to create.
        """
        path = "/api/data/resources/teams"
        queryParams = {}
        result = self.client.send_request("POST", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[ResourceTeamDto](None, True, False, result.status_code, ResourceTeamDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ResourceTeamDto](result.json(), False, True, result.status_code, None)

    def delete_resource_team(self, resourceTeamId: str) -> AstroResult[object]:
        """
        The endpoint is used to delete a resource team. Users assigned
        to this team will no longer be assigned thereafter.

        Parameters
        ----------
        resourceTeamId : str
            The Id of the team to be removed.
        """
        path = f"/api/data/resources/teams/{resourceTeamId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[object](None, True, False, result.status_code, object(**json.loads(result.content)['data']))
        else:
            return AstroResult[object](result.json(), False, True, result.status_code, None)

    def update_resource_team(self, teamresourceId: str, body: UpdateResourceTeamDto) -> AstroResult[ResourceTeamDto]:
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
        queryParams = {}
        result = self.client.send_request("PUT", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[ResourceTeamDto](None, True, False, result.status_code, ResourceTeamDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ResourceTeamDto](result.json(), False, True, result.status_code, None)
