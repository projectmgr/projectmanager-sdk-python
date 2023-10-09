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
from ProjectManagerSdk.models.namedto import NameDto
import json

class TaskTagClient:
    """
    API methods related to TaskTag
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def replace_tasktags(self, taskId: str, body: list[object]) -> AstroResult[ChangeSetStatusDto]:
        """
        Replaces the existing TaskTags on a Task with a newly provided
        list of TaskTags.

        A TaskTag is a connection between a Task and a Tag. Each Task
        can have zero, one or many TaskTags associated with it. TaskTags
        can be assigned and removed from the Task to help you classify
        your Tasks and prioritize work.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task for which we will replace
            TaskTags
        body : list[object]
            The replacement list of TaskTags for this Task
        """
        path = f"/api/data/tasks/{taskId}/tags"
        queryParams = {}
        result = self.client.send_request("POST", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, ChangeSetStatusDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ChangeSetStatusDto](result.json(), False, True, result.status_code, None)

    def add_tasktag_to_task(self, taskId: str, body: list[object]) -> AstroResult[ChangeSetStatusDto]:
        """
        Add one or more new TaskTags to a Task.

        A TaskTag is a connection between a Task and a Tag. Each Task
        can have zero, one or many TaskTags associated with it. TaskTags
        can be assigned and removed from the Task to help you classify
        your Tasks and prioritize work.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task for which we will add
            TaskTags
        body : list[object]
            The new TaskTags to add to this Task
        """
        path = f"/api/data/tasks/{taskId}/tags"
        queryParams = {}
        result = self.client.send_request("PUT", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, ChangeSetStatusDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ChangeSetStatusDto](result.json(), False, True, result.status_code, None)

    def remove_tasktag_from_task(self, taskId: str, body: list[object]) -> AstroResult[ChangeSetStatusDto]:
        """
        Removes one or more existing TaskTags from a Task.

        A TaskTag is a connection between a Task and a Tag. Each Task
        can have zero, one or many TaskTags associated with it. TaskTags
        can be assigned and removed from the Task to help you classify
        your Tasks and prioritize work.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task for which we will remove
            existing TaskTags
        body : list[object]
            The TaskTags to remove from this Task
        """
        path = f"/api/data/tasks/{taskId}/tags"
        queryParams = {}
        result = self.client.send_request("DELETE", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, ChangeSetStatusDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ChangeSetStatusDto](result.json(), False, True, result.status_code, None)
