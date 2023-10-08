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
from ProjectManager.SDK.models.bulktaskcreatedto import BulkTaskCreateDto
from ProjectManager.SDK.models.changesetstatusdto import ChangeSetStatusDto
from ProjectManager.SDK.models.changesetstatusdtolist import ChangeSetStatusDtoList
from ProjectManager.SDK.models.taskcreatedto import TaskCreateDto
from ProjectManager.SDK.models.taskdetailsdto import TaskDetailsDto
from ProjectManager.SDK.models.taskdtolist import TaskDtoList
from ProjectManager.SDK.models.taskprioritydtolist import TaskPriorityDtoList
from ProjectManager.SDK.models.taskupdatedto import TaskUpdateDto

class TaskClient:
    """
    API methods related to Task
    """
    from ProjectManager.SDK.project_manager_client import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def query_tasks(self, $top: int, $skip: int, $filter: str, $select: str, $orderby: str, $expand: str) -> AstroResult[AstroResult[TaskDtoList]]:
        """
        Retrieve a list of Tasks that match an [OData formatted
        query](https://www.odata.org/).

        A Task is an individual element of work that must be performed
        to complete a Project. A Task can have one or more Resources
        assigned to it. Tasks can be linked to other Tasks to indicate
        whether they have a dependency or a connection.

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
        path = "/api/data/tasks"
        result = self.client.send_request("GET", path, None, {"$top": $top, "$skip": $skip, "$filter": $filter, "$select": $select, "$orderby": $orderby, "$expand": $expand}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), TaskDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def retrieve_task(self, taskId: str) -> AstroResult[AstroResult[TaskDetailsDto]]:
        """
        Retrieve a Task by its unique identifier or by its short ID. A
        Task has both a unique identifier, which is a GUID, and a short
        ID, which is a small text label that is unique only within your
        Workspace.

        A Task is an individual element of work that must be performed
        to complete a Project. A Task can have one or more Resources
        assigned to it. Tasks can be linked to other Tasks to indicate
        whether they have a dependency or a connection.

        Parameters
        ----------
        taskId : str
            The unique identifier or short ID of the Task to retrieve
        """
        path = f"/api/data/tasks/{taskId}"
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), TaskDetailsDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_task(self, taskId: str, body: TaskUpdateDto) -> AstroResult[AstroResult[ChangeSetStatusDto]]:
        """
        Update an existing Task and replace the values of fields
        specified.

        A Task is an individual element of work that must be performed
        to complete a Project. A Task can have one or more Resources
        assigned to it. Tasks can be linked to other Tasks to indicate
        whether they have a dependency or a connection.

        Multiple users can be working on data at the same time. When you
        call an API to update an object, this call is converted into a
        Changeset that is then applied sequentially. You can use
        RetrieveChangeset to see the status of an individual Changeset.

        Known Issues: This API returns an error if your Update call
        includes too many changes in a single API call. Please restrict
        usage to one change per API request. This API will be deprecated
        and replaced with an improved API call in a future release.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task to update
        body : TaskUpdateDto
            All non-null fields in this object will replace existing
            data in the Task
        """
        path = f"/api/data/tasks/{taskId}"
        result = self.client.send_request("PUT", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ChangeSetStatusDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_task(self, taskId: str) -> AstroResult[AstroResult[ChangeSetStatusDto]]:
        """
        Delete an existing Task.

        A Task is an individual element of work that must be performed
        to complete a Project. A Task can have one or more Resources
        assigned to it. Tasks can be linked to other Tasks to indicate
        whether they have a dependency or a connection.

        Multiple users can be working on data at the same time. When you
        call an API to update an object, this call is converted into a
        Changeset that is then applied sequentially. You can use
        RetrieveChangeset to see the status of an individual Changeset.

        Parameters
        ----------
        taskId : str
            Unique identifier of the Task to delete
        """
        path = f"/api/data/tasks/{taskId}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ChangeSetStatusDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_task(self, projectId: str, body: TaskCreateDto) -> AstroResult[AstroResult[ChangeSetStatusDto]]:
        """
        Create a new Task within a specified project.

        A Task is an individual element of work that must be performed
        to complete a Project. A Task can have one or more Resources
        assigned to it. Tasks can be linked to other Tasks to indicate
        whether they have a dependency or a connection.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project that will contain this
            Task
        body : TaskCreateDto
            The new Task to create
        """
        path = f"/api/data/projects/{projectId}/tasks"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ChangeSetStatusDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def retrieve_task_priorities(self, ) -> AstroResult[AstroResult[TaskPriorityDtoList]]:
        """
        Retrieves all TaskPriorities defined within your Workspace.

        A TaskPriority is a named priority level used by your business
        to determine how to decide which Tasks are the most important.
        You can name your TaskPriority levels anything you like and you
        can reorganize the order of the TaskPriority levels at any time.


        Note that TaskPriority and ProjectPriority are different classes
        of priority levels. Even if they may have similar names, they
        are different objects and must be tracked separately.

        Parameters
        ----------
        """
        path = "/api/data/tasks/priorities"
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), TaskPriorityDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_many_tasks(self, projectId: str, body: list[object]) -> AstroResult[AstroResult[ChangeSetStatusDtoList]]:
        """
        Create multiple new Tasks within a specified project with a
        single API call.

        A Task is an individual element of work that must be performed
        to complete a Project. A Task can have one or more Resources
        assigned to it. Tasks can be linked to other Tasks to indicate
        whether they have a dependency or a connection.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project that will contain these
            Tasks
        body : list[object]
            The list of new Tasks to create
        """
        path = f"/api/data/projects/{projectId}/tasks/bulk"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ChangeSetStatusDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))
