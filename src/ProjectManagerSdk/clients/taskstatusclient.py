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
from ProjectManagerSdk.models.taskstatuscreatedto import TaskStatusCreateDto
from ProjectManagerSdk.models.taskstatusdto import TaskStatusDto
from ProjectManagerSdk.models.taskstatusupdatedto import TaskStatusUpdateDto
import json

class TaskStatusClient:
    """
    API methods related to TaskStatus
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_task_statuses(self, projectId: str) -> AstroResult[list[TaskStatusDto]]:
        """
        Retrieves the list of TaskStatus levels for a specific Project
        within your Workspace.

        A TaskStatus is a named status level used by your business to
        determine how to measure the progress of Tasks. You can define
        your own named status levels that are appropriate for your
        business and determine which status levels are considered done.

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
                data.append(TaskStatusDto(**dict))
            return AstroResult[list[TaskStatusDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[TaskStatusDto]](result.json(), False, True, result.status_code, None)

    def create_taskstatus(self, projectId: str, body: TaskStatusCreateDto) -> AstroResult[TaskStatusDto]:
        """
        Creates a new TaskStatus level for a specific Project within
        your Workspace.

        A TaskStatus is a named status level used by your business to
        determine how to measure the progress of Tasks. You can define
        your own named status levels that are appropriate for your
        business.

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
        result = self.client.send_request("POST", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[TaskStatusDto](None, True, False, result.status_code, TaskStatusDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[TaskStatusDto](result.json(), False, True, result.status_code, None)

    def update_taskstatus(self, projectId: str, body: TaskStatusUpdateDto) -> AstroResult[TaskStatusDto]:
        """
        Updates an existing TaskStatus level for a specific Project
        within your Workspace.

        A TaskStatus is a named status level used by your business to
        determine how to measure the progress of Tasks. You can define
        your own named status levels that are appropriate for your
        business.

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
        result = self.client.send_request("PUT", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[TaskStatusDto](None, True, False, result.status_code, TaskStatusDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[TaskStatusDto](result.json(), False, True, result.status_code, None)

    def delete_taskstatus(self, projectId: str, taskStatusId: str) -> AstroResult[object]:
        """
        The endpoint is used to delete a TaskStatus.

        You will not be able to delete a TaskStatus if there are tasks
        that have been assigned to this status level or if the
        TaskStatus is the default status level.

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
            return AstroResult[object](None, True, False, result.status_code, object(**json.loads(result.content)['data']))
        else:
            return AstroResult[object](result.json(), False, True, result.status_code, None)
