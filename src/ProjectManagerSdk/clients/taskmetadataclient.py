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
from ProjectManagerSdk.models.taskmetadatasearchdto import TaskMetadataSearchDto
from ProjectManagerSdk.models.taskmetadataupdatedto import TaskMetadataUpdateDto
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

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
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

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
            response = AstroResult[list[TaskMetadataSearchDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
