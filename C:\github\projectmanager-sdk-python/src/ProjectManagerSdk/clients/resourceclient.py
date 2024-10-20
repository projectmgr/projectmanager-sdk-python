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
from ProjectManagerSdk.models.resourcecreatedto import ResourceCreateDto
from ProjectManagerSdk.models.resourcedto import ResourceDto
from ProjectManagerSdk.models.resourcescreatedto import ResourcesCreateDto
from ProjectManagerSdk.models.resourcesdto import ResourcesDto
from ProjectManagerSdk.models.resourceupdatedto import ResourceUpdateDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class ResourceClient:
    """
    API methods related to Resource
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def create_resource(self, body: ResourceCreateDto) -> AstroResult[ResourceDto]:
        """
        Create a new Resource within your Workspace. A Resource
        represents a person, material, or tool that is used within your
        Projects. When you attach a Resources to more than one Task, the
        software will schedule the usage of your Resource so that it is
        not allocated to more than one Task at the same time. The users
        in your Workspace are also considered Resources. To invite a new
        User to your Workspace, create a new Resource for that user.

        Parameters
        ----------
        body : ResourceCreateDto
            The details for the new Resource to create
        """
        path = "/api/data/resources"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ResourceDto, data=json.loads(result.content)['data'])
            return AstroResult[ResourceDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ResourceDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def query_resources(self, top: int, skip: int, filter: str, orderby: str, expand: str) -> AstroResult[List[ResourceDto]]:
        """
        Retrieve a list of Resources that match an [OData formatted
        query](https://www.odata.org/). A Resource represents a person,
        material, or tool that is used within your Projects. When you
        attach a Resources to more than one Task, the software will
        schedule the usage of your Resource so that it is not allocated
        to more than one Task at the same time. The users in your
        Workspace are also considered Resources. To invite a new User to
        your Workspace, create a new Resource for that user.

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
        path = "/api/data/resources"
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
                data.append(dacite.from_dict(data_class=ResourceDto, data=dict))
            return AstroResult[List[ResourceDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[ResourceDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_resource(self, resourceId: str, body: ResourceUpdateDto) -> AstroResult[ResourceDto]:
        """
        Updates an existing Resource based on information you provide. A
        Resource represents a person, material, or tool that is used
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
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ResourceDto, data=json.loads(result.content)['data'])
            return AstroResult[ResourceDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ResourceDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def retrieve_resource(self, resourceId: str) -> AstroResult[ResourceDto]:
        """
        Retrieve the Resource matching the specified unique ID. A
        Resource represents a person, material, or tool that is used
        within your Projects. When you attach a Resources to more than
        one Task, the software will schedule the usage of your Resource
        so that it is not allocated to more than one Task at the same
        time. The users in your Workspace are also considered Resources.
        To invite a new User to your Workspace, create a new Resource
        for that user.

        Parameters
        ----------
        resourceId : str
            The id of the Resource
        """
        path = f"/api/data/resources/{resourceId}"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ResourceDto, data=json.loads(result.content)['data'])
            return AstroResult[ResourceDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ResourceDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_many_resources(self, body: ResourcesCreateDto) -> AstroResult[ResourcesDto]:
        """
        Create new Resources within your Workspace. A Resource
        represents a person, material, or tool that is used within your
        Projects. When you attach a Resources to more than one Task, the
        software will schedule the usage of your Resource so that it is
        not allocated to more than one Task at the same time. The users
        in your Workspace are also considered Resources. To invite a new
        User to your Workspace, create a new Resource for that user.

        Parameters
        ----------
        body : ResourcesCreateDto
            The details for the new Resources to create
        """
        path = "/api/data/resources/bulk"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ResourcesDto, data=json.loads(result.content)['data'])
            return AstroResult[ResourcesDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ResourcesDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def resend_invite_email(self, resourceId: str) -> AstroResult[object]:
        """
        Resend Invite Email to a Resource within your Workspace. When
        you create a Resource that is a person, ProjectManager sends
        that person an email inviting them to join your Workspace. If
        that email is accidentally deleted or sent to a spam folder, you
        can request this email be sent again using this API.

        Parameters
        ----------
        resourceId : str
            The unique identifier of the Resource to send an invitation
            email
        """
        path = f"/api/data/resources/{resourceId}/resendinvite"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
