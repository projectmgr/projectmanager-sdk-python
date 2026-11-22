#
# ProjectManager API for Python
#
# (c) ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#

from ProjectManagerSdk.models.astroresult import AstroResult
from ProjectManagerSdk.models.changesetstatusdto import ChangeSetStatusDto
from ProjectManagerSdk.models.tasklinkcreatedto import TaskLinkCreateDto
from ProjectManagerSdk.models.tasklinkdto import TaskLinkDto
from ProjectManagerSdk.models.tasklinkupdatedto import TaskLinkUpdateDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class TaskLinkClient:
    """
    API methods related to TaskLink
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def create_task_link(self, taskId: str, body: TaskLinkCreateDto) -> AstroResult[ChangeSetStatusDto]:
        """
        Creates a new link (dependency) from this Task to another Task
        in the same Project. A Task Link connects a predecessor Task to
        a successor Task, indicating a scheduling dependency between
        them. The link type controls how the two Tasks' dates relate to
        each other, and lag adds (or, if negative, removes) time between
        them. Valid LinkType values (case-insensitive): finishToStart,
        startToStart, finishToFinish, startToFinish. Omitting LinkType
        defaults to finishToStart.

        Parameters
        ----------
        taskId : str
            The unique identifier of the predecessor Task for this link
        body : TaskLinkCreateDto
            The Task to link to, along with the link type and lag
        """
        path = f"/api/data/tasks/{taskId}/links-to"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ChangeSetStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ChangeSetStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_task_link(self, taskId: str, successorTaskId: str, body: TaskLinkUpdateDto) -> AstroResult[ChangeSetStatusDto]:
        """
        Updates the link type and/or lag of an existing link between
        this Task and another Task.

        Parameters
        ----------
        taskId : str
            The unique identifier of the predecessor Task for this link
        successorTaskId : str
            The unique identifier of the successor Task for this link
        body : TaskLinkUpdateDto
            The new link type and lag for this link
        """
        path = f"/api/data/tasks/{taskId}/links-to/{successorTaskId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ChangeSetStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ChangeSetStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def delete_task_link(self, taskId: str, successorTaskId: str) -> AstroResult[ChangeSetStatusDto]:
        """
        Removes an existing link between this Task and another Task.

        Parameters
        ----------
        taskId : str
            The unique identifier of the predecessor Task for this link
        successorTaskId : str
            The unique identifier of the successor Task for this link
        """
        path = f"/api/data/tasks/{taskId}/links-to/{successorTaskId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ChangeSetStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ChangeSetStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def retrieve_task_links(self, taskId: str) -> AstroResult[List[TaskLinkDto]]:
        """
        Retrieve the existing links from this Task to other Tasks.

        Parameters
        ----------
        taskId : str
            The unique identifier of the predecessor Task
        """
        path = f"/api/data/tasks/{taskId}/links"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=TaskLinkDto, data=dict))
            return AstroResult[List[TaskLinkDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[TaskLinkDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
