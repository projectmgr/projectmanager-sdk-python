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
from ProjectManagerSdk.models.createresourceteamdto import CreateResourceTeamDto
from ProjectManagerSdk.models.resourceteamdto import ResourceTeamDto
from ProjectManagerSdk.models.updateresourceteamdto import UpdateResourceTeamDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class ResourceTeamClient:
    """
    API methods related to ResourceTeam
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_resource_teams(self, top: int, skip: int, filter: str, orderby: str, expand: str) -> AstroResult[List[ResourceTeamDto]]:
        """
        Retrieves all ResourceTeams defined within your Workspace that
        match an [OData formatted query](https://www.odata.org/). A
        ResourceTeam is a grouping of Resources that allows you to keep
        track of assignments in a manner consistent with your business
        needs. You can assign Resources to be members of zero, one, or
        many ResourceTeams.

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
        path = "/api/data/resources/teams"
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
                data.append(dacite.from_dict(data_class=ResourceTeamDto, data=dict))
            return AstroResult[List[ResourceTeamDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[ResourceTeamDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

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
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ResourceTeamDto, data=json.loads(result.content)['data'])
            return AstroResult[ResourceTeamDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ResourceTeamDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

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
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

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
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ResourceTeamDto, data=json.loads(result.content)['data'])
            return AstroResult[ResourceTeamDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ResourceTeamDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
