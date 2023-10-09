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
from ProjectManagerSdk.models.projectcustomerdto import ProjectCustomerDto
import json

class ProjectCustomerClient:
    """
    API methods related to ProjectCustomer
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_project_customers(self) -> AstroResult[list[ProjectCustomerDto]]:
        """
        Retrieves all ProjectCustomers defined within your Workspace.

        A ProjectCustomer is a code used to identify costs within your
        Projects. Each ProjectCustomer has a name and a unique
        identifier. ChargeCodes are defined per Workspace and are shared
        among Projects.

        Parameters
        ----------
        """
        path = "/api/data/projects/customers"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(ProjectCustomerDto(**dict))
            return AstroResult[list[ProjectCustomerDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[ProjectCustomerDto]](result.json(), False, True, result.status_code, None)
