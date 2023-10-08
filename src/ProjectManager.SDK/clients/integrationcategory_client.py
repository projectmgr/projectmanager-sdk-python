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
from ProjectManager.SDK.models.integrationcategorydtolist import IntegrationCategoryDtoList

class IntegrationCategoryClient:
    """
    API methods related to IntegrationCategory
    """
    from ProjectManager.SDK.project_manager_client import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_provider_categories(self, ) -> AstroResult[AstroResult[IntegrationCategoryDtoList]]:
        """
        Retrieves the list of available IntegrationProvider categories.

        An IntegrationProvider is the name of an external application or
        service that can be connected to ProjectManager.com. The
        Integrations API is intended for use by ProjectManager and its
        business development partners. Please contact ProjectManager's
        sales team to request use of this API.

        Parameters
        ----------
        """
        path = "/api/data/integrations/categories"
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), IntegrationCategoryDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))
