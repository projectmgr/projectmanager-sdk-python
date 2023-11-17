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
from ProjectManagerSdk.models.integrationcategorydto import IntegrationCategoryDto
import json

class IntegrationCategoryClient:
    """
    API methods related to IntegrationCategory
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_provider_categories(self) -> AstroResult[list[IntegrationCategoryDto]]:
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
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(IntegrationCategoryDto(**dict))
            return AstroResult[list[IntegrationCategoryDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[IntegrationCategoryDto]](result.json(), False, True, result.status_code, None)
