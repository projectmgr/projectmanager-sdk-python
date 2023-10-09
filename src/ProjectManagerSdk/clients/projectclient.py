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
from ProjectManagerSdk.models.projectcreaterequestdto import ProjectCreateRequestDto
from ProjectManagerSdk.models.projectcreateresponsedto import ProjectCreateResponseDto
from ProjectManagerSdk.models.projectdto import ProjectDto
from ProjectManagerSdk.models.projectupdatedto import ProjectUpdateDto
import json

class ProjectClient:
    """
    API methods related to Project
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def query_projects(self, top: int, skip: int, filter: str, select: str, orderby: str, expand: str) -> AstroResult[list[ProjectDto]]:
        """
        Retrieve a list of Projects that match an [OData formatted
        query](https://www.odata.org/).

        A Project is a collection of Tasks that contributes towards a
        goal. Within a Project, Tasks represent individual items of work
        that team members must complete. The sum total of Tasks within a
        Project represents the work to be completed for that Project.

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
        path = "/api/data/projects"
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
                data.append(ProjectDto(**dict))
            return AstroResult[list[ProjectDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[ProjectDto]](result.json(), False, True, result.status_code, None)

    def create_project(self, body: ProjectCreateRequestDto) -> AstroResult[ProjectCreateResponseDto]:
        """
        Create a new project based on the details provided.

        A Project is a collection of Tasks that contributes towards a
        goal. Within a Project, Tasks represent individual items of work
        that team members must complete. The sum total of Tasks within a
        Project represents the work to be completed for that Project.

        Parameters
        ----------
        body : ProjectCreateRequestDto
            Information about the Project you wish to create
        """
        path = "/api/data/projects"
        queryParams = {}
        result = self.client.send_request("POST", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[ProjectCreateResponseDto](None, True, False, result.status_code, ProjectCreateResponseDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ProjectCreateResponseDto](result.json(), False, True, result.status_code, None)

    def retrieve_project(self, projectId: str) -> AstroResult[ProjectDto]:
        """
        Retrieves a project based on its unique identifier.

        A Project is a collection of Tasks that contributes towards a
        goal. Within a Project, Tasks represent individual items of work
        that team members must complete. The sum total of Tasks within a
        Project represents the work to be completed for that Project.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project to retrieve.
        """
        path = f"/api/data/projects/{projectId}"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[ProjectDto](None, True, False, result.status_code, ProjectDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ProjectDto](result.json(), False, True, result.status_code, None)

    def update_project(self, projectId: str, body: ProjectUpdateDto) -> AstroResult[object]:
        """
        Update an existing Project and replace the values of fields
        specified.

        A Project is a collection of Tasks that contributes towards a
        goal. Within a Project, Tasks represent individual items of work
        that team members must complete. The sum total of Tasks within a
        Project represents the work to be completed for that Project.

        Multiple users can be working on data at the same time. When you
        call an API to update an object, this call is converted into a
        Changeset that is then applied sequentially. You can use
        RetrieveChangeset to see the status of an individual Changeset.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project to update
        body : ProjectUpdateDto
            All non-null fields in this object will replace previous
            data within the Project
        """
        path = f"/api/data/projects/{projectId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[object](None, True, False, result.status_code, object(**json.loads(result.content)['data']))
        else:
            return AstroResult[object](result.json(), False, True, result.status_code, None)
