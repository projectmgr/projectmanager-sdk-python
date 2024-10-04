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
from ProjectManagerSdk.models.projectcreatedto import ProjectCreateDto
from ProjectManagerSdk.models.projectdto import ProjectDto
from ProjectManagerSdk.models.projectupdatedto import ProjectUpdateDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class ProjectClient:
    """
    API methods related to Project
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def query_projects(self, top: int, skip: int, filter: str, orderby: str, expand: str) -> AstroResult[List[ProjectDto]]:
        """
        Retrieve a list of Projects that match an [OData formatted
        query](https://www.odata.org/). A Project is a collection of
        Tasks that contributes towards a goal. Within a Project, Tasks
        represent individual items of work that team members must
        complete. The sum total of Tasks within a Project represents the
        work to be completed for that Project.

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
        path = "/api/data/projects"
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
                data.append(dacite.from_dict(data_class=ProjectDto, data=dict))
            return AstroResult[List[ProjectDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[ProjectDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_project(self, body: ProjectCreateDto) -> AstroResult[ProjectDto]:
        """
        Create a new project based on the details provided. A Project is
        a collection of Tasks that contributes towards a goal. Within a
        Project, Tasks represent individual items of work that team
        members must complete. The sum total of Tasks within a Project
        represents the work to be completed for that Project.

        Parameters
        ----------
        body : ProjectCreateDto
            Information about the Project you wish to create
        """
        path = "/api/data/projects"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ProjectDto, data=json.loads(result.content)['data'])
            return AstroResult[ProjectDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ProjectDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def retrieve_project(self, projectId: str) -> AstroResult[ProjectDto]:
        """
        Retrieves a project based on its unique identifier. A Project is
        a collection of Tasks that contributes towards a goal. Within a
        Project, Tasks represent individual items of work that team
        members must complete. The sum total of Tasks within a Project
        represents the work to be completed for that Project.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project to retrieve.
        """
        path = f"/api/data/projects/{projectId}"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ProjectDto, data=json.loads(result.content)['data'])
            return AstroResult[ProjectDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ProjectDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_project(self, projectId: str, body: ProjectUpdateDto) -> AstroResult[object]:
        """
        Update an existing Project and replace the values of fields
        specified. A Project is a collection of Tasks that contributes
        towards a goal. Within a Project, Tasks represent individual
        items of work that team members must complete. The sum total of
        Tasks within a Project represents the work to be completed for
        that Project. Multiple users can be working on data at the same
        time. When you call an API to update an object, this call is
        converted into a Changeset that is then applied sequentially.
        You can use RetrieveChangeset to see the status of an individual
        Changeset.

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
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def delete_project(self, projectId: str, hardDelete: bool) -> AstroResult[object]:
        """
        Delete a project based on the details provided. A Project is a
        collection of Tasks that contributes towards a goal. Within a
        Project, Tasks represent individual items of work that team
        members must complete. The sum total of Tasks within a Project
        represents the work to be completed for that Project.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project to delete
        hardDelete : bool
            Hard delete project true or false
        """
        path = f"/api/data/projects/{projectId}"
        queryParams = {}
        if hardDelete:
            queryParams['hardDelete'] = hardDelete
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
