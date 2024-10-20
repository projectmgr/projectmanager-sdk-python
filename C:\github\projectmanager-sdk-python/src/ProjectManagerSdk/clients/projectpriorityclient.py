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
