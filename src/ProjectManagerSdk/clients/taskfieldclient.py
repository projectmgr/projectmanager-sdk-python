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
from ProjectManagerSdk.models.changesetstatusdto import ChangeSetStatusDto
from ProjectManagerSdk.models.createtaskfielddto import CreateTaskFieldDto
from ProjectManagerSdk.models.taskfielddto import TaskFieldDto
from ProjectManagerSdk.models.taskfieldvaluedto import TaskFieldValueDto
from ProjectManagerSdk.models.updatetaskfieldvaluedto import UpdateTaskFieldValueDto
import json

class TaskFieldClient:
    """
    API methods related to TaskField
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_task_fields(self, projectId: str) -> AstroResult[list[TaskFieldDto]]:
        """
        Retrieves all TaskFields defined for a specific Project within
        your Workspace.

        A TaskField is a custom field defined within your Workspace for
        a specific Project. You can define TaskFields for any
        integration purpose that is important to your business. Each
        TaskField has a data type as well as options in how it is
        handled. TaskFields can be edited for each Task inside this
        Project.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project to retrieve TaskFields
        """
        path = f"/api/data/projects/{projectId}/tasks/fields"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(TaskFieldDto(**dict))
            return AstroResult[list[TaskFieldDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[TaskFieldDto]](result.json(), False, True, result.status_code, None)

    def create_task_field(self, projectId: str, body: CreateTaskFieldDto) -> AstroResult[ChangeSetStatusDto]:
        """
        Creates a new TaskField for a specific Project within your
        Workspace.

        A TaskField is a custom field defined within your Workspace for
        a specific Project. You can define TaskFields for any
        integration purpose that is important to your business. Each
        TaskField has a data type as well as options in how it is
        handled. TaskFields can be edited for each Task inside this
        Project.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project within which to create
            this TaskField
        body : CreateTaskFieldDto
            Information about the TaskField to create
        """
        path = f"/api/data/projects/{projectId}/tasks/fields"
        queryParams = {}
        result = self.client.send_request("POST", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, ChangeSetStatusDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ChangeSetStatusDto](result.json(), False, True, result.status_code, None)

    def query_task_fields(self, top: int, skip: int, filter: str, select: str, orderby: str, expand: str) -> AstroResult[list[TaskFieldDto]]:
        """
        Retrieve a list of TaskFields that match an [OData formatted
        query](https://www.odata.org/).

        A TaskField is a custom field defined within your Workspace for
        a specific Project. You can define TaskFields for any
        integration purpose that is important to your business. Each
        TaskField has a data type as well as options in how it is
        handled. TaskFields can be edited for each Task inside a
        Project.

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
        path = "/api/data/projects/tasks/fields"
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
                data.append(TaskFieldDto(**dict))
            return AstroResult[list[TaskFieldDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[TaskFieldDto]](result.json(), False, True, result.status_code, None)

    def delete_task_field(self, projectId: str, fieldId: str) -> AstroResult[object]:
        """
        Deletes a TaskField for a specific Project within your
        Workspace.

        A TaskField is a custom field defined within your Workspace for
        a specific Project. You can define TaskFields for any
        integration purpose that is important to your business. Each
        TaskField has a data type as well as options in how it is
        handled. TaskFields can be edited for each Task inside this
        Project.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project that contains this
            TaskField
        fieldId : str
            The unique identifier of the TaskField to delete
        """
        path = f"/api/data/projects/{projectId}/tasks/fields/{fieldId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[object](None, True, False, result.status_code, object(**json.loads(result.content)['data']))
        else:
            return AstroResult[object](result.json(), False, True, result.status_code, None)

    def retrieve_all_taskfield_values(self, taskId: str) -> AstroResult[list[TaskFieldValueDto]]:
        """
        Retrieves all TaskField values for a particular Task.

        A TaskField is a custom field defined within your Workspace for
        a specific Project. You can define TaskFields for any
        integration purpose that is important to your business. Each
        TaskField has a data type as well as options in how it is
        handled. TaskFields can be edited for each Task inside this
        Project.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task for which we want
            TaskField values
        """
        path = f"/api/data/tasks/{taskId}/fields/values"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(TaskFieldValueDto(**dict))
            return AstroResult[list[TaskFieldValueDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[TaskFieldValueDto]](result.json(), False, True, result.status_code, None)

    def query_task_field_values(self, top: int, skip: int, filter: str, select: str, orderby: str, expand: str) -> AstroResult[list[TaskFieldValueDto]]:
        """
        Retrieve a list of TaskFieldValues that match an [OData
        formatted query](https://www.odata.org/).

        A TaskField is a custom field defined within your Workspace for
        a specific Project. You can define TaskFields for any
        integration purpose that is important to your business. Each
        TaskField has a data type as well as options in how it is
        handled. TaskFields can be edited for each Task inside this
        Project.

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
        path = "/api/data/tasks/fields/values"
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
                data.append(TaskFieldValueDto(**dict))
            return AstroResult[list[TaskFieldValueDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[TaskFieldValueDto]](result.json(), False, True, result.status_code, None)

    def retrieve_task_field_value(self, taskId: str, fieldId: str) -> AstroResult[TaskFieldValueDto]:
        """
        Retrieves the current TaskField value for a particular Task and
        TaskField.

        A TaskField is a custom field defined within your Workspace for
        a specific Project. You can define TaskFields for any
        integration purpose that is important to your business. Each
        TaskField has a data type as well as options in how it is
        handled. TaskFields can be edited for each Task inside this
        Project.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task of the value to retrieve
        fieldId : str
            The unique identifier of the TaskField of the value to
            retrieve
        """
        path = f"/api/data/tasks/{taskId}/fields/{fieldId}/values"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[TaskFieldValueDto](None, True, False, result.status_code, TaskFieldValueDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[TaskFieldValueDto](result.json(), False, True, result.status_code, None)

    def update_task_field_value(self, taskId: str, fieldId: str, body: UpdateTaskFieldValueDto) -> AstroResult[ChangeSetStatusDto]:
        """
        Replaces the current value of a TaskField for a specific Task
        within your Workspace.

        A TaskField is a custom field defined within your Workspace for
        a specific Project. You can define TaskFields for any
        integration purpose that is important to your business. Each
        TaskField has a data type as well as options in how it is
        handled. TaskFields can be edited for each Task inside this
        Project.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task whose value you wish to
            update
        fieldId : str
            The unique identifier of the TaskField whose value you wish
            to update
        body : UpdateTaskFieldValueDto
            The new value for this TaskField for this Task
        """
        path = f"/api/data/tasks/{taskId}/fields/{fieldId}/values"
        queryParams = {}
        result = self.client.send_request("PUT", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, ChangeSetStatusDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ChangeSetStatusDto](result.json(), False, True, result.status_code, None)
