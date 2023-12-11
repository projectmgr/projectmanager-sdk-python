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
from requests.models import Response
import json

class TeamsClient:
    """
    API methods related to Teams
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_zip_file_for_teams_integrations(self) -> Response:
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
        return result
