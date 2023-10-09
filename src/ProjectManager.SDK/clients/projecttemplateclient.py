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

from models.astroresult import AstroResult
from models.projecttemplatedto import ProjectTemplateDto

class ProjectTemplateClient:
    """
    API methods related to ProjectTemplate
    """
    from projectmanagerclient import ProjectManagerClient

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
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(None, True, False, result.status_code, list[ProjectTemplateDto](**json.loads(result.content)['data']))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)
