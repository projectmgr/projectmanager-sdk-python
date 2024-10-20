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
from ProjectManagerSdk.models.createtaskfielddto import CreateTaskFieldDto
from ProjectManagerSdk.models.taskfielddto import TaskFieldDto
from ProjectManagerSdk.models.taskfieldvaluedto import TaskFieldValueDto
from ProjectManagerSdk.models.updatetaskfieldvaluedto import UpdateTaskFieldValueDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class TaskFieldClient:
    """
    API methods related to TaskField
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_task_fields(self, projectId: str) -> AstroResult[List[TaskFieldDto]]:
        """
        Retrieves all TaskFields defined for a specific Project within
        your Workspace. A TaskField is a custom field defined within
        your Workspace for a specific Project. You can define TaskFields
        for any integration purpose that is important to your business.
        Each TaskField has a data type as well as options in how it is
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
                data.append(dacite.from_dict(data_class=TaskFieldDto, data=dict))
            return AstroResult[List[TaskFieldDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[TaskFieldDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_task_field(self, projectId: str, body: CreateTaskFieldDto) -> AstroResult[ChangeSetStatusDto]:
        """
        Creates a new TaskField for a specific Project within your
        Workspace. A TaskField is a custom field defined within your
        Workspace for a specific Project. You can define TaskFields for
        any integration purpose that is important to your business. Each
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
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ChangeSetStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ChangeSetStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def query_task_fields(self, top: int, skip: int, filter: str, orderby: str, expand: str) -> AstroResult[List[TaskFieldDto]]:
        """
        Retrieve a list of TaskFields that match an [OData formatted
        query](https://www.odata.org/). A TaskField is a custom field
        defined within your Workspace for a specific Project. You can
        define TaskFields for any integration purpose that is important
        to your business. Each TaskField has a data type as well as
        options in how it is handled. TaskFields can be edited for each
        Task inside a Project.

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
        path = "/api/data/projects/tasks/fields"
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
                data.append(dacite.from_dict(data_class=TaskFieldDto, data=dict))
            return AstroResult[List[TaskFieldDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[TaskFieldDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def delete_task_field(self, projectId: str, fieldId: str) -> AstroResult[object]:
        """
        Deletes a TaskField for a specific Project within your
        Workspace. A TaskField is a custom field defined within your
        Workspace for a specific Project. You can define TaskFields for
        any integration purpose that is important to your business. Each
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
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def retrieve_all_taskfield_values(self, taskId: str) -> AstroResult[List[TaskFieldValueDto]]:
        """
        Retrieves all TaskField values for a particular Task. A
        TaskField is a custom field defined within your Workspace for a
        specific Project. You can define TaskFields for any integration
        purpose that is important to your business. Each TaskField has a
        data type as well as options in how it is handled. TaskFields
        can be edited for each Task inside this Project.

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
                data.append(dacite.from_dict(data_class=TaskFieldValueDto, data=dict))
            return AstroResult[List[TaskFieldValueDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[TaskFieldValueDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def query_task_field_values(self, top: int, skip: int, filter: str, orderby: str, expand: str) -> AstroResult[List[TaskFieldValueDto]]:
        """
        Retrieve a list of TaskFieldValues that match an [OData
        formatted query](https://www.odata.org/). A TaskField is a
        custom field defined within your Workspace for a specific
        Project. You can define TaskFields for any integration purpose
        that is important to your business. Each TaskField has a data
        type as well as options in how it is handled. TaskFields can be
        edited for each Task inside this Project.

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
        path = "/api/data/tasks/fields/values"
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
                data.append(dacite.from_dict(data_class=TaskFieldValueDto, data=dict))
            return AstroResult[List[TaskFieldValueDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[TaskFieldValueDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def retrieve_task_field_value(self, taskId: str, fieldId: str) -> AstroResult[TaskFieldValueDto]:
        """
        Retrieves the current TaskField value for a particular Task and
        TaskField. A TaskField is a custom field defined within your
        Workspace for a specific Project. You can define TaskFields for
        any integration purpose that is important to your business. Each
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
            data = dacite.from_dict(data_class=TaskFieldValueDto, data=json.loads(result.content)['data'])
            return AstroResult[TaskFieldValueDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[TaskFieldValueDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_task_field_value(self, taskId: str, fieldId: str, body: UpdateTaskFieldValueDto) -> AstroResult[ChangeSetStatusDto]:
        """
        Replaces the current value of a TaskField for a specific Task
        within your Workspace. A TaskField is a custom field defined
        within your Workspace for a specific Project. You can define
        TaskFields for any integration purpose that is important to your
        business. Each TaskField has a data type as well as options in
        how it is handled. TaskFields can be edited for each Task inside
        this Project.

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
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ChangeSetStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ChangeSetStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
