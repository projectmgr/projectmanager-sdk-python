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

class TaskTodoClient:
    """
    API methods related to TaskTodo
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def get_todos(self, taskId: str) -> AstroResult[List[TaskTodoDto]]:
        """
        Retrieve a list of todos for a task

        Parameters
        ----------
        taskId : str
            the id of the task
        """
        path = f"/api/data/tasks/{taskId}/todos"
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

    def create_todo(self, taskId: str, body: TaskTodoCreateDto) -> AstroResult[TaskTodoDto]:
        """
        Create a todo for a task

        Parameters
        ----------
        taskId : str
            the id of the task
        body : TaskTodoCreateDto
            the data for creating a todo
        """
        path = f"/api/data/tasks/{taskId}/todos"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=TaskTodoDto, data=json.loads(result.content)['data'])
            return AstroResult[TaskTodoDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[TaskTodoDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_todo(self, todoId: str, body: TaskTodoUpdateDto) -> AstroResult[TaskTodoDto]:
        """
        Update a todo for a task

        Parameters
        ----------
        todoId : str
            the id of the task
        body : TaskTodoUpdateDto
            the data for updating a todo
        """
        path = f"/api/data/tasks/todos/{todoId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=TaskTodoDto, data=json.loads(result.content)['data'])
            return AstroResult[TaskTodoDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[TaskTodoDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def delete_todo(self, todoId: str) -> AstroResult[object]:
        """
        Remove a todo

        Parameters
        ----------
        todoId : str
            the id of the todo
        """
        path = f"/api/data/tasks/todos/{todoId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
