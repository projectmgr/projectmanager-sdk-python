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

from ProjectManagerSdk.models.astroresult import AstroResult
from ProjectManagerSdk.models.stringobjectdictionary import StringObjectDictionary
from ProjectManagerSdk.models.taskmetadatasearchdto import TaskMetadataSearchDto
from ProjectManagerSdk.models.taskmetadataupdatedto import TaskMetadataUpdateDto
import json

class TaskMetadataClient:
    """
    API methods related to TaskMetadata
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def add_metadata(self, taskId: str, isSystem: bool, isOverride: bool, body: TaskMetadataUpdateDto) -> AstroResult[object]:
        """
        Adds a metadata to a task

        Parameters
        ----------
        taskId : str
            Task ID
        isSystem : bool
            If metadata is for system or customer, isSystem = true is
            only of ProjectManager
        isOverride : bool
            If false we merge with the keys
        body : TaskMetadataUpdateDto
            The metadata
        """
        path = f"/api/data/tasks/{taskId}/metadata"
        queryParams = {}
        if isSystem:
            queryParams['isSystem'] = isSystem
        if isOverride:
            queryParams['isOverride'] = isOverride
        result = self.client.send_request("PUT", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[object](None, True, False, result.status_code, object(**json.loads(result.content)['data']))
        else:
            return AstroResult[object](result.json(), False, True, result.status_code, None)

    def get_task_metadata(self, taskId: str, isSystem: bool) -> AstroResult[StringObjectDictionary]:
        path = f"/api/data/tasks/{taskId}/metadata"
        queryParams = {}
        if isSystem:
            queryParams['isSystem'] = isSystem
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[StringObjectDictionary](None, True, False, result.status_code, StringObjectDictionary(**json.loads(result.content)['data']))
        else:
            return AstroResult[StringObjectDictionary](result.json(), False, True, result.status_code, None)

    def get_tasks_by_project_id_and_foreign_key_id(self, foreignKey: str, projectId: str, isSystem: bool) -> AstroResult[list[TaskMetadataSearchDto]]:
        path = f"/api/data/projects/{projectId}/tasks/metadata"
        queryParams = {}
        if foreignKey:
            queryParams['foreignKey'] = foreignKey
        if isSystem:
            queryParams['isSystem'] = isSystem
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(TaskMetadataSearchDto(**dict))
            return AstroResult[list[TaskMetadataSearchDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[TaskMetadataSearchDto]](result.json(), False, True, result.status_code, None)
