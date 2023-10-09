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

from ProjectManagerSdk.models.assigneeupsertdto import AssigneeUpsertDto
from ProjectManagerSdk.models.astroresult import AstroResult
from ProjectManagerSdk.models.changesetstatusdto import ChangeSetStatusDto
from ProjectManagerSdk.models.iddto import IdDto
import json

class TaskAssigneeClient:
    """
    API methods related to TaskAssignee
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def replace_task_assignees(self, taskId: str, body: list[object]) -> AstroResult[ChangeSetStatusDto]:
        """
        Replace all TaskAssignees on a Task with new TaskAssignees.

        A TaskAssignee is an assignment of a Resource to a Task. You can
        assign multiple Resources to a Task and designate what
        proportion of their time will be allocated to this Task.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task whose TaskAssignees will
            be replaced
        body : list[object]
            The new list of TaskAssignees for this Task
        """
        path = f"/api/data/tasks/{taskId}/assignees"
        queryParams = {}
        result = self.client.send_request("POST", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, ChangeSetStatusDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ChangeSetStatusDto](result.json(), False, True, result.status_code, None)

    def create_or_update_taskassignee(self, taskId: str, body: list[object]) -> AstroResult[ChangeSetStatusDto]:
        """
        Adds or updates a TaskAssignee to a Task. If the TaskAssignee is
        already assigned to the Task, update their allocation. If the
        TaskAssignee is not yet assigned to the Task, assign them and
        set their allocation level to the correct amount.

        A TaskAssignee is an assignment of a Resource to a Task. You can
        assign multiple Resources to a Task and designate what
        proportion of their time will be allocated to this Task.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task to add or update an
            assignment
        body : list[object]
            List of Assignee data
        """
        path = f"/api/data/tasks/{taskId}/assignees"
        queryParams = {}
        result = self.client.send_request("PUT", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, ChangeSetStatusDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ChangeSetStatusDto](result.json(), False, True, result.status_code, None)

    def delete_task_assignees(self, taskId: str, body: list[object]) -> AstroResult[ChangeSetStatusDto]:
        """
        Remove one or more TaskAssignees from a Task.

        A TaskAssignee is an assignment of a Resource to a Task. You can
        assign multiple Resources to a Task and designate what
        proportion of their time will be allocated to this Task.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task whose TaskAssignee will be
            removed
        body : list[object]
            List of TaskAssignee records to remove
        """
        path = f"/api/data/tasks/{taskId}/assignees"
        queryParams = {}
        result = self.client.send_request("DELETE", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, ChangeSetStatusDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ChangeSetStatusDto](result.json(), False, True, result.status_code, None)
