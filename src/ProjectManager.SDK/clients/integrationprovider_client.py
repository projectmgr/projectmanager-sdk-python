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
from ProjectManager.SDK.models.authenticationstatusdto import AuthenticationStatusDto
from ProjectManager.SDK.models.directlinkdto import DirectLinkDto
from ProjectManager.SDK.models.integrationproviderdtolist import IntegrationProviderDtoList

class IntegrationProviderClient:
    """
    API methods related to IntegrationProvider
    """
    from ProjectManager.SDK.project_manager_client import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def list_providers(self, ) -> AstroResult[AstroResult[IntegrationProviderDtoList]]:
        """
        List all available IntegrationProviders that can be activated.

        An IntegrationProvider is the name of an external application or
        service that can be connected to ProjectManager.com. The
        Integrations API is intended for use by ProjectManager and its
        business development partners. Please contact ProjectManager's
        sales team to request use of this API.

        Parameters
        ----------
        """
        path = "/api/data/integrations/providers"
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), IntegrationProviderDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def activate_integration_provider(self, providerId: str) -> AstroResult[AstroResult[DirectLinkDto]]:
        """
        Activates an Integration Provider and retrieves authentication
        information about a specific IntegrationProvider.

        An IntegrationProvider is the name of an external application or
        service that can be connected to ProjectManager.com. The
        Integrations API is intended for use by ProjectManager and its
        business development partners. Please contact ProjectManager's
        sales team to request use of this API.

        Parameters
        ----------
        providerId : str
            The unique identifier of the IntegrationProvider for which
            you are requesting authentication information
        """
        path = f"/api/data/integrations/providers/{providerId}"
        result = self.client.send_request("POST", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), DirectLinkDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_integration_provider(self, providerId: str, body: AuthenticationStatusDto) -> AstroResult[AstroResult[]]:
        """
        Allows you to update the auth status of the provider specific
        connection.

        Parameters
        ----------
        providerId : str
            The identifier to the provider
        body : AuthenticationStatusDto
            Specify the auth status
        """
        path = f"/api/data/integrations/providers/{providerId}"
        result = self.client.send_request("PUT", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def deactivate_integration_provider(self, providerId: str) -> AstroResult[AstroResult[]]:
        """
        Allows you to deactivate an integration provider

        Parameters
        ----------
        providerId : str
            The identifier to the provider
        """
        path = f"/api/data/integrations/providers/{providerId}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_user_integration_provider_connection(self, providerId: str) -> AstroResult[AstroResult[DirectLinkDto]]:
        """
        Retrieves user authentication information about a specific
        IntegrationProvider.

        This connection can be used for requests to Providers that
        require specific user data.

        Parameters
        ----------
        providerId : str
            The unique identifier of the IntegrationProvider for which
            you are requesting authentication information
        """
        path = f"/api/data/integrations/providers/{providerId}/user-connection"
        result = self.client.send_request("POST", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), DirectLinkDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_user_integration_provider_connection(self, providerId: str, body: AuthenticationStatusDto) -> AstroResult[AstroResult[]]:
        """
        Allows you to update the auth status of the provider specific
        user connection.

        Parameters
        ----------
        providerId : str
            The identifier to the provider
        body : AuthenticationStatusDto
            Specify the auth status
        """
        path = f"/api/data/integrations/providers/{providerId}/user-connection"
        result = self.client.send_request("PUT", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))
