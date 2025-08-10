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
from ProjectManagerSdk.models.namedto import NameDto
from ProjectManagerSdk.models.tasktagdto import TaskTagDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class NptTagClient:
    """
    API methods related to NptTag
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def replace_tasktags(self, taskId: str, body: List[NameDto]) -> AstroResult[List[TaskTagDto]]:
        """
        Replaces the existing TaskTags on a Task with a newly provided
        list of TaskTags. A TaskTag is a connection between a Task and a
        Tag. Each Task can have zero, one or many TaskTags associated
        with it. TaskTags can be assigned and removed from the Task to
        help you classify your Tasks and prioritize work.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task for which we will replace
            TaskTags
        body : List[NameDto]
            The replacement list of TaskTags for this Task
        """
        path = f"/api/data/non-project-tasks/{taskId}/tags"
        queryParams = {}
        bodyArray = []
        for item in body:
            bodyArray.append(remove_empty_elements(dataclasses.asdict(item)))
        result = self.client.send_request("POST", path, bodyArray, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=TaskTagDto, data=dict))
            return AstroResult[List[TaskTagDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[TaskTagDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def add_tasktag_to_task(self, taskId: str, body: List[NameDto]) -> AstroResult[List[TaskTagDto]]:
        """
        Add one or more new TaskTags to a Task. A TaskTag is a
        connection between a Task and a Tag. Each Task can have zero,
        one or many TaskTags associated with it. TaskTags can be
        assigned and removed from the Task to help you classify your
        Tasks and prioritize work.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task for which we will add
            TaskTags
        body : List[NameDto]
            The new TaskTags to add to this Task
        """
        path = f"/api/data/non-project-tasks/{taskId}/tags"
        queryParams = {}
        bodyArray = []
        for item in body:
            bodyArray.append(remove_empty_elements(dataclasses.asdict(item)))
        result = self.client.send_request("PUT", path, bodyArray, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=TaskTagDto, data=dict))
            return AstroResult[List[TaskTagDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[TaskTagDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def remove_tasktag_from_task(self, taskId: str, body: List[NameDto]) -> AstroResult[object]:
        """
        Removes one or more existing TaskTags from a Task. A TaskTag is
        a connection between a Task and a Tag. Each Task can have zero,
        one or many TaskTags associated with it. TaskTags can be
        assigned and removed from the Task to help you classify your
        Tasks and prioritize work.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task for which we will remove
            existing TaskTags
        body : List[NameDto]
            The TaskTags to remove from this Task
        """
        path = f"/api/data/non-project-tasks/{taskId}/tags"
        queryParams = {}
        bodyArray = []
        for item in body:
            bodyArray.append(remove_empty_elements(dataclasses.asdict(item)))
        result = self.client.send_request("DELETE", path, bodyArray, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def retrieve_tasktags(self, taskId: str) -> AstroResult[List[TaskTagDto]]:
        """
        Retrieve the existing TaskTags on a Task A TaskTag is a
        connection between a Task and a Tag. Each Task can have zero,
        one or many TaskTags associated with it. TaskTags can be
        assigned and removed from the Task to help you classify your
        Tasks and prioritize work.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task for which we will retrieve
            TaskTags
        """
        path = f"/api/data/non-project-tasks/{taskId}/tags"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=TaskTagDto, data=dict))
            return AstroResult[List[TaskTagDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[TaskTagDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
