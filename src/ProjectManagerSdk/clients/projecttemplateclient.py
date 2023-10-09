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
from ProjectManagerSdk.models.projecttemplatedto import ProjectTemplateDto
import json

class ProjectTemplateClient:
    """
    API methods related to ProjectTemplate
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_project_templates(self) -> AstroResult[list[ProjectTemplateDto]]:
        """
        Retrieves all ProjectTemplates defined in the system.

        A ProjectTemplate is a definition of default project related
        data (eg. Tasks) that can be applied to a new project when it is
        created.

        Parameters
        ----------
        """
        path = "/api/data/projects/templates"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(ProjectTemplateDto(**dict))
            return AstroResult[list[ProjectTemplateDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[ProjectTemplateDto]](result.json(), False, True, result.status_code, None)
