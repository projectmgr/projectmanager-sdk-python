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

from ProjectManager.SDK.astro_result import AstroResult
from ProjectManager.SDK.models.errorresult import ErrorResult
from ProjectManager.SDK.astroresult import AstroResult
from ProjectManager.SDK.models.projecttemplatedtolist import ProjectTemplateDtoList

class ProjectTemplateClient:
    """
    API methods related to ProjectTemplate
    """
    from ProjectManager.SDK.project_manager_client import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_project_templates(self, ) -> AstroResult[AstroResult[ProjectTemplateDtoList]]:
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
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ProjectTemplateDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))
