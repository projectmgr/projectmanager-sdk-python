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
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class TeamsClient:
    """
    API methods related to Teams
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_zip_file_for_teams_integrations(self) -> AstroResult[bytes]:
        """
        Retrieves zip file for teams integrations. The Teams API is
        intended for use by ProjectManager and its business development
        partners. Please contact ProjectManager's sales team to request
        use of this API.

        Parameters
        ----------
        """
        path = "/api/data/integrations/teams/application"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[bytes](None, True, False, result.status_code, result.content)
        else:
            response = AstroResult[bytes](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
