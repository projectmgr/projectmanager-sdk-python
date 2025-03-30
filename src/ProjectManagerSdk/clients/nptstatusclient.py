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
from ProjectManagerSdk.models.nptstatusdto import NptStatusDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class NptStatusClient:
    """
    API methods related to NptStatus
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def get_npt_task_statuses(self) -> AstroResult[List[NptStatusDto]]:
        """
        Get a list of task statuses that can be used by npt tasks.

        Parameters
        ----------
        """
        path = "/api/data/non-project-tasks/statuses"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=NptStatusDto, data=dict))
            return AstroResult[List[NptStatusDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[NptStatusDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
