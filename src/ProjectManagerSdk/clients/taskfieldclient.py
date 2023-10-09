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
from ProjectManagerSdk.models.createtaskfieldrequestdto import CreateTaskFieldRequestDto
from ProjectManagerSdk.models.gettaskfieldsresponsedto import GetTaskFieldsResponseDto
from ProjectManagerSdk.models.taskfieldsvalueresponsedto import TaskFieldsValueResponseDto
from ProjectManagerSdk.models.updatetaskfieldvaluedto import UpdateTaskFieldValueDto
import json

class TaskFieldClient:
    """
    API methods related to TaskField
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_task_fields(self, projectId: str) -> AstroResult[list[GetTaskFieldsResponseDto]]:
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
                data.append(GetTaskFieldsResponseDto(**dict))
            return AstroResult[list[GetTaskFieldsResponseDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[GetTaskFieldsResponseDto]](result.json(), False, True, result.status_code, None)

    def create_task_field(self, projectId: str, body: CreateTaskFieldRequestDto) -> AstroResult[ChangeSetStatusDto]:
        """
        Creates a new TaskFields for a specific Project within your
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
        body : CreateTaskFieldRequestDto
            Information about the TaskField to create
        """
        path = f"/api/data/projects/{projectId}/tasks/fields"
        queryParams = {}
        result = self.client.send_request("POST", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, ChangeSetStatusDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ChangeSetStatusDto](result.json(), False, True, result.status_code, None)

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

    def retrieve_taskfield_value(self, taskId: str, fieldId: str) -> AstroResult[TaskFieldsValueResponseDto]:
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
        path = f"/api/data/tasks/{taskId}/fields/{fieldId}"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[TaskFieldsValueResponseDto](None, True, False, result.status_code, TaskFieldsValueResponseDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[TaskFieldsValueResponseDto](result.json(), False, True, result.status_code, None)

    def update_taskfield_value(self, taskId: str, fieldId: str, body: UpdateTaskFieldValueDto) -> AstroResult[ChangeSetStatusDto]:
        """
        Replaces the current value of a TaskFields for a specific Task
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
        path = f"/api/data/tasks/{taskId}/fields/{fieldId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, ChangeSetStatusDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ChangeSetStatusDto](result.json(), False, True, result.status_code, None)

    def retrieve_all_taskfield_values(self, taskId: str) -> AstroResult[list[TaskFieldsValueResponseDto]]:
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
        path = f"/api/data/tasks/{taskId}/fields"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(TaskFieldsValueResponseDto(**dict))
            return AstroResult[list[TaskFieldsValueResponseDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[TaskFieldsValueResponseDto]](result.json(), False, True, result.status_code, None)
