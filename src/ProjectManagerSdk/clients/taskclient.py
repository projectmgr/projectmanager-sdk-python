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
from ProjectManagerSdk.models.changesetstatusdto import ChangeSetStatusDto
from ProjectManagerSdk.models.taskcreatedto import TaskCreateDto
from ProjectManagerSdk.models.taskdto import TaskDto
from ProjectManagerSdk.models.taskprioritydto import TaskPriorityDto
from ProjectManagerSdk.models.taskupdatedto import TaskUpdateDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class TaskClient:
    """
    API methods related to Task
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def query_tasks(self, top: int, skip: int, filter: str, orderby: str, expand: str) -> AstroResult[List[TaskDto]]:
        """
        Retrieve a list of Tasks that match an [OData formatted
        query](https://www.odata.org/). A Task is an individual element
        of work that must be performed to complete a Project. A Task can
        have one or more Resources assigned to it. Tasks can be linked
        to other Tasks to indicate whether they have a dependency or a
        connection.

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
        path = "/api/data/tasks"
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
                data.append(dacite.from_dict(data_class=TaskDto, data=dict))
            return AstroResult[List[TaskDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[TaskDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def retrieve_task(self, taskId: str) -> AstroResult[TaskDto]:
        """
        Retrieve a Task by its unique identifier or by its short ID. A
        Task has both a unique identifier, which is a GUID, and a short
        ID, which is a small text label that is unique only within your
        Workspace. A Task is an individual element of work that must be
        performed to complete a Project. A Task can have one or more
        Resources assigned to it. Tasks can be linked to other Tasks to
        indicate whether they have a dependency or a connection.

        Parameters
        ----------
        taskId : str
            The unique identifier or short ID of the Task to retrieve
        """
        path = f"/api/data/tasks/{taskId}"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=TaskDto, data=json.loads(result.content)['data'])
            return AstroResult[TaskDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[TaskDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_task(self, taskId: str, body: TaskUpdateDto) -> AstroResult[ChangeSetStatusDto]:
        """
        Update an existing Task and replace the values of fields
        specified. A Task is an individual element of work that must be
        performed to complete a Project. A Task can have one or more
        Resources assigned to it. Tasks can be linked to other Tasks to
        indicate whether they have a dependency or a connection.
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
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ChangeSetStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ChangeSetStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def delete_task(self, taskId: str) -> AstroResult[ChangeSetStatusDto]:
        """
        Delete an existing Task. A Task is an individual element of work
        that must be performed to complete a Project. A Task can have
        one or more Resources assigned to it. Tasks can be linked to
        other Tasks to indicate whether they have a dependency or a
        connection. Multiple users can be working on data at the same
        time. When you call an API to update an object, this call is
        converted into a Changeset that is then applied sequentially.
        You can use RetrieveChangeset to see the status of an individual
        Changeset.

        Parameters
        ----------
        taskId : str
            Unique identifier of the Task to delete
        """
        path = f"/api/data/tasks/{taskId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ChangeSetStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ChangeSetStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_task(self, projectId: str, body: TaskCreateDto) -> AstroResult[ChangeSetStatusDto]:
        """
        Create a new Task within a specified project. A Task is an
        individual element of work that must be performed to complete a
        Project. A Task can have one or more Resources assigned to it.
        Tasks can be linked to other Tasks to indicate whether they have
        a dependency or a connection.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project that will contain this
            Task
        body : TaskCreateDto
            The new Task to create
        """
        path = f"/api/data/projects/{projectId}/tasks"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ChangeSetStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ChangeSetStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def retrieve_task_priorities(self) -> AstroResult[List[TaskPriorityDto]]:
        """
        Retrieves all TaskPriorities defined within your Workspace. A
        TaskPriority is a named priority level used by your business to
        determine how to decide which Tasks are the most important. You
        can name your TaskPriority levels anything you like and you can
        reorganize the order of the TaskPriority levels at any time.
        Note that TaskPriority and ProjectPriority are different classes
        of priority levels. Even if they may have similar names, they
        are different objects and must be tracked separately.

        Parameters
        ----------
        """
        path = "/api/data/tasks/priorities"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=TaskPriorityDto, data=dict))
            return AstroResult[List[TaskPriorityDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[TaskPriorityDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_many_tasks(self, projectId: str, body: List[TaskCreateDto]) -> AstroResult[List[ChangeSetStatusDto]]:
        """
        Create multiple new Tasks within a specified project with a
        single API call. A Task is an individual element of work that
        must be performed to complete a Project. A Task can have one or
        more Resources assigned to it. Tasks can be linked to other
        Tasks to indicate whether they have a dependency or a
        connection.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project that will contain these
            Tasks
        body : List[TaskCreateDto]
            The list of new Tasks to create
        """
        path = f"/api/data/projects/{projectId}/tasks/bulk"
        queryParams = {}
        bodyArray = []
        for item in body:
            bodyArray.append(remove_empty_elements(dataclasses.asdict(item)))
        result = self.client.send_request("POST", path, bodyArray, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=ChangeSetStatusDto, data=dict))
            return AstroResult[List[ChangeSetStatusDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[ChangeSetStatusDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def add_parent_task(self, taskId: str, parentTaskId: str) -> AstroResult[ChangeSetStatusDto]:
        """
        Adds a task parent relationship

        Parameters
        ----------
        taskId : str
            The task that will become the child
        parentTaskId : str
            The parent task
        """
        path = f"/api/data/tasks/{taskId}/parent/{parentTaskId}"
        queryParams = {}
        result = self.client.send_request("POST", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ChangeSetStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ChangeSetStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_parent_task(self, taskId: str, parentTaskId: str) -> AstroResult[ChangeSetStatusDto]:
        """
        Updates a task parent relationship

        Parameters
        ----------
        taskId : str
            The task that will become the child
        parentTaskId : str
            The parent task
        """
        path = f"/api/data/tasks/{taskId}/parent/{parentTaskId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ChangeSetStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ChangeSetStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def remove_parent_task(self, taskId: str) -> AstroResult[ChangeSetStatusDto]:
        """
        Removes a task parent relationship completely

        Parameters
        ----------
        taskId : str
            The child task
        """
        path = f"/api/data/tasks/{taskId}/parent"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ChangeSetStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ChangeSetStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
