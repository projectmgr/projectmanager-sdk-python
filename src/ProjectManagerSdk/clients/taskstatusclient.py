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
from ProjectManagerSdk.models.taskstatuscreatedto import TaskStatusCreateDto
from ProjectManagerSdk.models.taskstatusdto import TaskStatusDto
from ProjectManagerSdk.models.taskstatusupdatedto import TaskStatusUpdateDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class TaskStatusClient:
    """
    API methods related to TaskStatus
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_task_statuses(self, projectId: str) -> AstroResult[List[TaskStatusDto]]:
        """
        Retrieves the list of TaskStatus levels for a specific Project
        within your Workspace. A TaskStatus is a named status level used
        by your business to determine how to measure the progress of
        Tasks. You can define your own named status levels that are
        appropriate for your business and determine which status levels
        are considered done.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project to retrieve
            TaskStatuses
        """
        path = f"/api/data/projects/{projectId}/tasks/statuses"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=TaskStatusDto, data=dict))
            return AstroResult[List[TaskStatusDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[TaskStatusDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_taskstatus(self, projectId: str, body: TaskStatusCreateDto) -> AstroResult[TaskStatusDto]:
        """
        Creates a new TaskStatus level for a specific Project within
        your Workspace. A TaskStatus is a named status level used by
        your business to determine how to measure the progress of Tasks.
        You can define your own named status levels that are appropriate
        for your business.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project for the new TaskStatus
        body : TaskStatusCreateDto
            Information about the new TaskStatus level to create within
            this Project
        """
        path = f"/api/data/projects/{projectId}/tasks/statuses"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=TaskStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[TaskStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[TaskStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_taskstatus(self, projectId: str, body: TaskStatusUpdateDto) -> AstroResult[TaskStatusDto]:
        """
        Updates an existing TaskStatus level for a specific Project
        within your Workspace. A TaskStatus is a named status level used
        by your business to determine how to measure the progress of
        Tasks. You can define your own named status levels that are
        appropriate for your business.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project for the new TaskStatus
        body : TaskStatusUpdateDto
            Information about the existing TaskStatus level to update
            within this Project
        """
        path = f"/api/data/projects/{projectId}/tasks/statuses"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=TaskStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[TaskStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[TaskStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def delete_taskstatus(self, projectId: str, taskStatusId: str) -> AstroResult[object]:
        """
        The endpoint is used to delete a TaskStatus. You will not be
        able to delete a TaskStatus if there are tasks that have been
        assigned to this status level or if the TaskStatus is the
        default status level.

        Parameters
        ----------
        projectId : str
            The unique identifier of the Project for the TaskStatus
            level to delete
        taskStatusId : str
            The Id of the TaskStatus level to be removed.
        """
        path = f"/api/data/projects/{projectId}/tasks/statuses/{taskStatusId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
