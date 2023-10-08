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

from models.astroresult import AstroResult
from models.taskstatuscreatedto import TaskStatusCreateDto
from models.taskstatusdto import TaskStatusDto
from models.taskstatusupdatedto import TaskStatusUpdateDto

class TaskStatusClient:
    """
    API methods related to TaskStatus
    """
    from projectmanagerclient import ProjectManagerClient

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
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(None, True, False, result.status_code, list[TaskStatusDto](result.json(), list[TaskStatusDto]))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)

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
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(None, True, False, result.status_code, TaskStatusDto(result.json(), TaskStatusDto))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)

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
        result = self.client.send_request("PUT", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(None, True, False, result.status_code, TaskStatusDto(result.json(), TaskStatusDto))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)

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
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(None, True, False, result.status_code, object(result.json(), object))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)
