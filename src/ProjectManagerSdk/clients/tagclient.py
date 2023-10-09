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
from ProjectManagerSdk.models.tagcreatedto import TagCreateDto
from ProjectManagerSdk.models.tagdto import TagDto
from ProjectManagerSdk.models.tagupdatedto import TagUpdateDto
import json

class TagClient:
    """
    API methods related to Tag
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def query_tags(self, top: int, skip: int, filter: str, select: str, orderby: str, expand: str) -> AstroResult[list[TagDto]]:
        """
        Retrieve a list of Tags that match an [OData formatted
        query](https://www.odata.org/).

        A Tag is a named categorization you can use to distinguish
        objects from each other. Tags each have a unique identifier, a
        name, and a color.

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
        path = "/api/data/tags"
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
                data.append(TagDto(**dict))
            return AstroResult[list[TagDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[TagDto]](result.json(), False, True, result.status_code, None)

    def create_tag(self, body: TagCreateDto) -> AstroResult[TagDto]:
        """
        Creates a new Tag based on information you provide.

        A Tag is a named categorization you can use to distinguish
        objects from each other. Tags each have a unique identifier, a
        name, and a color.

        Parameters
        ----------
        body : TagCreateDto
            The information for the new Tag to create
        """
        path = "/api/data/tags"
        queryParams = {}
        result = self.client.send_request("POST", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[TagDto](None, True, False, result.status_code, TagDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[TagDto](result.json(), False, True, result.status_code, None)

    def update_tag(self, tagId: str, body: TagUpdateDto) -> AstroResult[TagDto]:
        """
        Updates a new Tag based on information you provide.

        A Tag is a named categorization you can use to distinguish
        objects from each other. Tags each have a unique identifier, a
        name, and a color.

        Parameters
        ----------
        tagId : str
            The id of the tag
        body : TagUpdateDto
            The information to update the tag
        """
        path = f"/api/data/tags/{tagId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[TagDto](None, True, False, result.status_code, TagDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[TagDto](result.json(), False, True, result.status_code, None)
