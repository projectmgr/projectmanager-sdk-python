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
from ProjectManagerSdk.models.createintegrationinstancedto import CreateIntegrationInstanceDto
from ProjectManagerSdk.models.integrationdto import IntegrationDto
from ProjectManagerSdk.models.newintegrationinstancedto import NewIntegrationInstanceDto
import json

class IntegrationClient:
    """
    API methods related to Integration
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_integration(self, integrationId: str) -> AstroResult[IntegrationDto]:
        """
        Retrieves an Integration specified by a unique identifier.

        The Integrations API is intended for use by ProjectManager and
        its business development partners. Please contact
        ProjectManager's sales team to request use of this API.

        Parameters
        ----------
        integrationId : str
            The unique identifier of this Integration
        """
        path = f"/api/data/integrations/{integrationId}"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[IntegrationDto](None, True, False, result.status_code, IntegrationDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[IntegrationDto](result.json(), False, True, result.status_code, None)

    def enable_integration(self, integrationId: str) -> AstroResult[IntegrationDto]:
        """
        Enable a specific Integration for the current Workspace.

        The Integrations API is intended for use by ProjectManager and
        its business development partners. Please contact
        ProjectManager's sales team to request use of this API.

        Parameters
        ----------
        integrationId : str
            The unique identifier of the Integration to enable
        """
        path = f"/api/data/integrations/{integrationId}"
        queryParams = {}
        result = self.client.send_request("POST", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[IntegrationDto](None, True, False, result.status_code, IntegrationDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[IntegrationDto](result.json(), False, True, result.status_code, None)

    def disable_integration(self, integrationId: str) -> AstroResult[object]:
        """
        Disable a specific Integration for the current Workspace.

        The Integrations API is intended for use by ProjectManager and
        its business development partners. Please contact
        ProjectManager's sales team to request use of this API.

        Parameters
        ----------
        integrationId : str
            The unique identifier of the Integration to disable
        """
        path = f"/api/data/integrations/{integrationId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[object](None, True, False, result.status_code, object(**json.loads(result.content)['data']))
        else:
            return AstroResult[object](result.json(), False, True, result.status_code, None)

    def retrieve_all_integrations(self) -> AstroResult[list[IntegrationDto]]:
        """
        Retrieves all Integrations for the current Workspace.

        The Integrations API is intended for use by ProjectManager and
        its business development partners. Please contact
        ProjectManager's sales team to request use of this API.

        Parameters
        ----------
        """
        path = "/api/data/integrations"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(IntegrationDto(**dict))
            return AstroResult[list[IntegrationDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[IntegrationDto]](result.json(), False, True, result.status_code, None)

    def add_integration_instance(self, integrationId: str, body: CreateIntegrationInstanceDto) -> AstroResult[NewIntegrationInstanceDto]:
        """
        Adds a new Integration instance to a Workspace.

        The Integrations API is intended for use by ProjectManager and
        its business development partners. Please contact
        ProjectManager's sales team to request use of this API.

        Parameters
        ----------
        integrationId : str
            The unique identifier of the Integration to add to this
            Workspace
        body : CreateIntegrationInstanceDto
            The information about this Integration to add
        """
        path = f"/api/data/integrations/{integrationId}/instance"
        queryParams = {}
        result = self.client.send_request("POST", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[NewIntegrationInstanceDto](None, True, False, result.status_code, NewIntegrationInstanceDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[NewIntegrationInstanceDto](result.json(), False, True, result.status_code, None)

    def remove_integration_instance(self, integrationInstanceId: str) -> AstroResult[object]:
        """
        Removes an existing Integration instance from a Workspace.

        The Integrations API is intended for use by ProjectManager and
        its business development partners. Please contact
        ProjectManager's sales team to request use of this API.

        Parameters
        ----------
        integrationInstanceId : str
            The unique identifier of the IntegrationInstance to remove
            from this Workspace
        """
        path = f"/api/data/integrations/instances/{integrationInstanceId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[object](None, True, False, result.status_code, object(**json.loads(result.content)['data']))
        else:
            return AstroResult[object](result.json(), False, True, result.status_code, None)
