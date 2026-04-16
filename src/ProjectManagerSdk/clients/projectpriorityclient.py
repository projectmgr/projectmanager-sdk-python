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
from ProjectManagerSdk.models.projectprioritycreatedto import ProjectPriorityCreateDto
from ProjectManagerSdk.models.projectprioritydto import ProjectPriorityDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class ProjectPriorityClient:
    """
    API methods related to ProjectPriority
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_project_priorities(self) -> AstroResult[List[ProjectPriorityDto]]:
        """
        Retrieves all ProjectPriorities defined within your Workspace. A
        ProjectPriority is a named priority level used by your business
        to determine how to decide which Projects are the most
        important. You can name your ProjectPriority levels anything you
        like and you can reorganize the order of the ProjectPriority
        levels at any time. Note that TaskPriority and ProjectPriority
        are different classes of priority levels. Even if they may have
        similar names, they are different objects and must be tracked
        separately.

        Parameters
        ----------
        """
        path = "/api/data/projects/priorities"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=ProjectPriorityDto, data=dict))
            return AstroResult[List[ProjectPriorityDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[ProjectPriorityDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_project_priority(self, body: ProjectPriorityCreateDto) -> AstroResult[ProjectPriorityDto]:
        """
        Create a project priority

        Parameters
        ----------
        body : ProjectPriorityCreateDto
            The data to create the priority
        """
        path = "/api/data/projects/priorities"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ProjectPriorityDto, data=json.loads(result.content)['data'])
            return AstroResult[ProjectPriorityDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ProjectPriorityDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_project_priority(self, priorityId: str, body: ProjectPriorityCreateDto) -> AstroResult[ProjectPriorityDto]:
        """
        Updates a project priority

        Parameters
        ----------
        priorityId : str
            The id of the priority to update
        body : ProjectPriorityCreateDto
            The data to update
        """
        path = f"/api/data/projects/priorities/{priorityId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ProjectPriorityDto, data=json.loads(result.content)['data'])
            return AstroResult[ProjectPriorityDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ProjectPriorityDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def delete_project_priority(self, priorityId: str) -> AstroResult[object]:
        """
        Delete a project priority. They will also be removed from any
        projects they were assigned too.

        Parameters
        ----------
        priorityId : str
            The id of the priority to remove
        """
        path = f"/api/data/projects/priorities/{priorityId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
