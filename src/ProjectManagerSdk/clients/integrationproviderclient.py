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
from ProjectManagerSdk.models.authenticationstatusdto import AuthenticationStatusDto
from ProjectManagerSdk.models.directlinkdto import DirectLinkDto
from ProjectManagerSdk.models.integrationproviderdto import IntegrationProviderDto
import json

class IntegrationProviderClient:
    """
    API methods related to IntegrationProvider
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def list_providers(self) -> AstroResult[list[IntegrationProviderDto]]:
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
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(IntegrationProviderDto(**dict))
            return AstroResult[list[IntegrationProviderDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[IntegrationProviderDto]](result.json(), False, True, result.status_code, None)

    def activate_integration_provider(self, providerId: str) -> AstroResult[DirectLinkDto]:
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
        queryParams = {}
        result = self.client.send_request("POST", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[DirectLinkDto](None, True, False, result.status_code, DirectLinkDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[DirectLinkDto](result.json(), False, True, result.status_code, None)

    def update_integration_provider(self, providerId: str, body: AuthenticationStatusDto) -> AstroResult[object]:
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
        queryParams = {}
        result = self.client.send_request("PUT", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[object](None, True, False, result.status_code, object(**json.loads(result.content)['data']))
        else:
            return AstroResult[object](result.json(), False, True, result.status_code, None)

    def deactivate_integration_provider(self, providerId: str) -> AstroResult[object]:
        """
        Allows you to deactivate an integration provider

        Parameters
        ----------
        providerId : str
            The identifier to the provider
        """
        path = f"/api/data/integrations/providers/{providerId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[object](None, True, False, result.status_code, object(**json.loads(result.content)['data']))
        else:
            return AstroResult[object](result.json(), False, True, result.status_code, None)

    def create_user_integration_provider_connection(self, providerId: str) -> AstroResult[DirectLinkDto]:
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
        queryParams = {}
        result = self.client.send_request("POST", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[DirectLinkDto](None, True, False, result.status_code, DirectLinkDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[DirectLinkDto](result.json(), False, True, result.status_code, None)

    def update_user_integration_provider_connection(self, providerId: str, body: AuthenticationStatusDto) -> AstroResult[object]:
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
        queryParams = {}
        result = self.client.send_request("PUT", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[object](None, True, False, result.status_code, object(**json.loads(result.content)['data']))
        else:
            return AstroResult[object](result.json(), False, True, result.status_code, None)
