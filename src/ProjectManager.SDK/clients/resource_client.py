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
from ProjectManager.SDK.models.resourcecreatedto import ResourceCreateDto
from ProjectManager.SDK.models.resourcedto import ResourceDto
from ProjectManager.SDK.models.resourcedtolist import ResourceDtoList
from ProjectManager.SDK.models.resourceupdatedto import ResourceUpdateDto

class ResourceClient:
    """
    API methods related to Resource
    """
    from ProjectManager.SDK.project_manager_client import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def create_resource(self, body: ResourceCreateDto) -> AstroResult[AstroResult[ResourceDto]]:
        """
        Create a new Resource within your Workspace.

        A Resource represents a person, material, or tool that is used
        within your Projects. When you attach a Resources to more than
        one Task, the software will schedule the usage of your Resource
        so that it is not allocated to more than one Task at the same
        time. The users in your Workspace are also considered Resources.
        To invite a new User to your Workspace, create a new Resource
        for that user.

        Parameters
        ----------
        body : ResourceCreateDto
            The details for the new Resource to create
        """
        path = "/api/data/resources"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ResourceDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_resources(self, $top: int, $skip: int, $filter: str, $select: str, $orderby: str, $expand: str) -> AstroResult[AstroResult[ResourceDtoList]]:
        """
        Retrieve a list of Resources that match an [OData formatted
        query](https://www.odata.org/).

        A Resource represents a person, material, or tool that is used
        within your Projects. When you attach a Resources to more than
        one Task, the software will schedule the usage of your Resource
        so that it is not allocated to more than one Task at the same
        time. The users in your Workspace are also considered Resources.
        To invite a new User to your Workspace, create a new Resource
        for that user.

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
        path = "/api/data/resources"
        result = self.client.send_request("GET", path, None, {"$top": $top, "$skip": $skip, "$filter": $filter, "$select": $select, "$orderby": $orderby, "$expand": $expand}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ResourceDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_resource(self, resourceId: str, body: ResourceUpdateDto) -> AstroResult[AstroResult[ResourceDto]]:
        """
        Updates an existing Resource based on information you provide.

        A Resource represents a person, material, or tool that is used
        within your Projects. When you attach a Resources to more than
        one Task, the software will schedule the usage of your Resource
        so that it is not allocated to more than one Task at the same
        time. The users in your Workspace are also considered Resources.
        To invite a new User to your Workspace, create a new Resource
        for that user.

        Parameters
        ----------
        resourceId : str
            The id of the resource
        body : ResourceUpdateDto
            The information to update the resource
        """
        path = f"/api/data/resources/{resourceId}"
        result = self.client.send_request("PUT", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ResourceDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))
