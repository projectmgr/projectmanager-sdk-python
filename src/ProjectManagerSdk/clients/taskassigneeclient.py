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

from ProjectManagerSdk.models.assigneeupsertdto import AssigneeUpsertDto
from ProjectManagerSdk.models.astroresult import AstroResult
from ProjectManagerSdk.models.changesetstatusdto import ChangeSetStatusDto
from ProjectManagerSdk.models.iddto import IdDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class TaskAssigneeClient:
    """
    API methods related to TaskAssignee
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def replace_task_assignees(self, taskId: str, body: List[AssigneeUpsertDto]) -> AstroResult[ChangeSetStatusDto]:
        """
        Replace all TaskAssignees on a Task with new TaskAssignees. A
        TaskAssignee is an assignment of a Resource to a Task. You can
        assign multiple Resources to a Task and designate how much of
        their time will be allocated to this Task.

        In the request body, id is the id of the Resource you would like
        to assign to the Task, and assignedEffort is the amount of time
        that Resource is expected to spend on the task. assignedEffort
        should be entered in minutes.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task whose TaskAssignees will
            be replaced
        body : List[AssigneeUpsertDto]
            The new list of TaskAssignees for this Task
        """
        path = f"/api/data/tasks/{taskId}/assignees"
        queryParams = {}
        bodyArray = []
        for item in body:
            bodyArray.append(remove_empty_elements(dataclasses.asdict(item)))
        result = self.client.send_request("POST", path, bodyArray, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ChangeSetStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ChangeSetStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_or_update_taskassignee(self, taskId: str, body: List[AssigneeUpsertDto]) -> AstroResult[ChangeSetStatusDto]:
        """
        Adds or updates a TaskAssignee to a Task. If the TaskAssignee is
        already assigned to the Task, update their allocation. If the
        TaskAssignee is not yet assigned to the Task, assign them and
        set their allocation level to the correct amount. A TaskAssignee
        is an assignment of a Resource to a Task. You can assign
        multiple Resources to a Task and designate what proportion of
        their time will be allocated to this Task.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task to add or update an
            assignment
        body : List[AssigneeUpsertDto]
            List of Assignee data
        """
        path = f"/api/data/tasks/{taskId}/assignees"
        queryParams = {}
        bodyArray = []
        for item in body:
            bodyArray.append(remove_empty_elements(dataclasses.asdict(item)))
        result = self.client.send_request("PUT", path, bodyArray, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ChangeSetStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ChangeSetStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def delete_task_assignees(self, taskId: str, body: List[IdDto]) -> AstroResult[ChangeSetStatusDto]:
        """
        Remove one or more TaskAssignees from a Task. A TaskAssignee is
        an assignment of a Resource to a Task. You can assign multiple
        Resources to a Task and designate what proportion of their time
        will be allocated to this Task.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task whose TaskAssignee will be
            removed
        body : List[IdDto]
            List of TaskAssignee records to remove
        """
        path = f"/api/data/tasks/{taskId}/assignees"
        queryParams = {}
        bodyArray = []
        for item in body:
            bodyArray.append(remove_empty_elements(dataclasses.asdict(item)))
        result = self.client.send_request("DELETE", path, bodyArray, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ChangeSetStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ChangeSetStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
