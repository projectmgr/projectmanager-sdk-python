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
from ProjectManager.SDK.models. import 
from ProjectManager.SDK.models.createintegrationinstancedto import CreateIntegrationInstanceDto
from ProjectManager.SDK.models.integrationdto import IntegrationDto
from ProjectManager.SDK.models.integrationdtolist import IntegrationDtoList
from ProjectManager.SDK.models.newintegrationinstancedto import NewIntegrationInstanceDto

class IntegrationClient:
    """
    API methods related to Integration
    """
    from ProjectManager.SDK.project_manager_client import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_integration(self, integrationId: str) -> AstroResult[AstroResult[IntegrationDto]]:
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
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), IntegrationDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def enable_integration(self, integrationId: str) -> AstroResult[AstroResult[IntegrationDto]]:
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
        result = self.client.send_request("POST", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), IntegrationDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def disable_integration(self, integrationId: str) -> AstroResult[AstroResult[]]:
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
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def retrieve_all_integrations(self, ) -> AstroResult[AstroResult[IntegrationDtoList]]:
        """
        Retrieves all Integrations for the current Workspace.

        The Integrations API is intended for use by ProjectManager and
        its business development partners. Please contact
        ProjectManager's sales team to request use of this API.

        Parameters
        ----------
        """
        path = "/api/data/integrations"
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), IntegrationDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def add_integration_instance(self, integrationId: str, body: CreateIntegrationInstanceDto) -> AstroResult[AstroResult[NewIntegrationInstanceDto]]:
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
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), NewIntegrationInstanceDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def remove_integration_instance(self, integrationInstanceId: str) -> AstroResult[AstroResult[]]:
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
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))
