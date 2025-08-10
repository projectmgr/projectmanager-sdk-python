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
from ProjectManagerSdk.models.tasktodocreatedto import TaskTodoCreateDto
from ProjectManagerSdk.models.tasktododto import TaskTodoDto
from ProjectManagerSdk.models.tasktodoupdatedto import TaskTodoUpdateDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class NptTodosClient:
    """
    API methods related to NptTodos
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def get_npt_todos(self, nptId: str) -> AstroResult[List[TaskTodoDto]]:
        """
        Get todos for a npt

        Parameters
        ----------
        nptId : str
            the id of the npt
        """
        path = f"/api/data/non-project-tasks/{nptId}/todos"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=TaskTodoDto, data=dict))
            return AstroResult[List[TaskTodoDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[TaskTodoDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_npt_todo(self, nptId: str, body: TaskTodoCreateDto) -> AstroResult[TaskTodoDto]:
        """
        Creates a new todo and associates it with the npt

        Parameters
        ----------
        nptId : str
            the id of the npt
        body : TaskTodoCreateDto
            The todo to create
        """
        path = f"/api/data/non-project-tasks/{nptId}/todos"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=TaskTodoDto, data=json.loads(result.content)['data'])
            return AstroResult[TaskTodoDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[TaskTodoDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_a_npt_todo(self, todoId: str, body: TaskTodoUpdateDto) -> AstroResult[TaskTodoDto]:
        """
        Update a Todo

        Parameters
        ----------
        todoId : str
            the id of the todo
        body : TaskTodoUpdateDto
            the fields to update
        """
        path = f"/api/data/non-project-tasks/todos/{todoId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=TaskTodoDto, data=json.loads(result.content)['data'])
            return AstroResult[TaskTodoDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[TaskTodoDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def remove_npt_todo(self, todoId: str) -> AstroResult[object]:
        """
        Remove Npt Todo

        Parameters
        ----------
        todoId : str
            the id of the todo to remove
        """
        path = f"/api/data/non-project-tasks/todos/{todoId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
