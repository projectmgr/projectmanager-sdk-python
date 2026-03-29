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
from ProjectManagerSdk.models.meetingtodocreatedto import MeetingTodoCreateDto
from ProjectManagerSdk.models.meetingtododto import MeetingTodoDto
from ProjectManagerSdk.models.meetingtodoupdatedto import MeetingTodoUpdateDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class MeetingTodosClient:
    """
    API methods related to MeetingTodos
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def get_meeting_todos(self, meetingId: str) -> AstroResult[List[MeetingTodoDto]]:
        """
        Get todos for a meeting

        Parameters
        ----------
        meetingId : str
            The id of the meeting
        """
        path = f"/api/data/meetings/{meetingId}/todos"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=MeetingTodoDto, data=dict))
            return AstroResult[List[MeetingTodoDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[MeetingTodoDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_meeting_todos(self, meetingId: str, body: MeetingTodoCreateDto) -> AstroResult[MeetingTodoDto]:
        """
        Creates a new todos and associates it with the meeting

        Parameters
        ----------
        meetingId : str
            The id of the meeting
        body : MeetingTodoCreateDto
            The todos to create
        """
        path = f"/api/data/meetings/{meetingId}/todos"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=MeetingTodoDto, data=json.loads(result.content)['data'])
            return AstroResult[MeetingTodoDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[MeetingTodoDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_a_meeting_todos(self, todoId: str, body: MeetingTodoUpdateDto) -> AstroResult[MeetingTodoDto]:
        """
        Update a todos

        Parameters
        ----------
        todoId : str
            The id of the todos
        body : MeetingTodoUpdateDto
            The fields to update
        """
        path = f"/api/data/meetings/todos/{todoId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=MeetingTodoDto, data=json.loads(result.content)['data'])
            return AstroResult[MeetingTodoDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[MeetingTodoDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def remove_meeting_todos(self, todoId: str) -> AstroResult[object]:
        """
        Remove meeting todos

        Parameters
        ----------
        todoId : str
            The id of the todos to remove
        """
        path = f"/api/data/meetings/todos/{todoId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
