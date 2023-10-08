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
from ProjectManager.SDK.models. import 
from ProjectManager.SDK.models.changesetstatusdto import ChangeSetStatusDto
from ProjectManager.SDK.models.createtaskfieldrequestdto import CreateTaskFieldRequestDto
from ProjectManager.SDK.models.gettaskfieldsresponsedtolist import GetTaskFieldsResponseDtoList
from ProjectManager.SDK.models.taskfieldsvalueresponsedto import TaskFieldsValueResponseDto
from ProjectManager.SDK.models.taskfieldsvalueresponsedtolist import TaskFieldsValueResponseDtoList
from ProjectManager.SDK.models.updatetaskfieldvaluedto import UpdateTaskFieldValueDto

class TaskFieldClient:
    """
    API methods related to TaskField
    """
    from ProjectManager.SDK.project_manager_client import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_task_fields(self, projectId: str) -> AstroResult[AstroResult[GetTaskFieldsResponseDtoList]]:
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
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), GetTaskFieldsResponseDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_task_field(self, projectId: str, body: CreateTaskFieldRequestDto) -> AstroResult[AstroResult[ChangeSetStatusDto]]:
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
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ChangeSetStatusDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_task_field(self, projectId: str, fieldId: str) -> AstroResult[AstroResult[]]:
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
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def retrieve_taskfield_value(self, taskId: str, fieldId: str) -> AstroResult[AstroResult[TaskFieldsValueResponseDto]]:
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
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), TaskFieldsValueResponseDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_taskfield_value(self, taskId: str, fieldId: str, body: UpdateTaskFieldValueDto) -> AstroResult[AstroResult[ChangeSetStatusDto]]:
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
        result = self.client.send_request("PUT", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ChangeSetStatusDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def retrieve_all_taskfield_values(self, taskId: str) -> AstroResult[AstroResult[TaskFieldsValueResponseDtoList]]:
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
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), TaskFieldsValueResponseDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))
