#
# ProjectManager API for Python
#
# (c) 2023-2024 ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  2023-2024 ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#

from ProjectManagerSdk.models.astroresult import AstroResult
from ProjectManagerSdk.models.authenticationdto import AuthenticationDto
from ProjectManagerSdk.models.authenticationstatusdto import AuthenticationStatusDto
from ProjectManagerSdk.models.connectionschemadto import ConnectionSchemaDto
from ProjectManagerSdk.models.directlinkdto import DirectLinkDto
from ProjectManagerSdk.models.integrationproviderdto import IntegrationProviderDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class IntegrationProviderClient:
    """
    API methods related to IntegrationProvider
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def list_providers(self) -> AstroResult[List[IntegrationProviderDto]]:
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
                data.append(dacite.from_dict(data_class=IntegrationProviderDto, data=dict))
            return AstroResult[List[IntegrationProviderDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[IntegrationProviderDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def activate_integration_provider(self, providerId: str) -> AstroResult[ConnectionSchemaDto]:
        """
        Activates an Integration Provider and retrieves authentication
        information about a specific IntegrationProvider. An
        IntegrationProvider is the name of an external application or
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
            data = dacite.from_dict(data_class=ConnectionSchemaDto, data=json.loads(result.content)['data'])
            return AstroResult[ConnectionSchemaDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ConnectionSchemaDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_integration_provider(self, providerId: str, body: AuthenticationDto) -> AstroResult[object]:
        """
        Allows you to update the auth status of the provider specific
        connection.

        An IntegrationProvider is the name of an external application or
        service that can be connected to ProjectManager.com. The
        Integrations API is intended for use by ProjectManager and its
        business development partners. Please contact ProjectManager's
        sales team to request use of this API.

        Parameters
        ----------
        providerId : str
            The identifier to the provider
        body : AuthenticationDto
            Specify the auth status
        """
        path = f"/api/data/integrations/providers/{providerId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def deactivate_integration_provider(self, providerId: str) -> AstroResult[object]:
        """
        Allows you to deactivate an integration provider.

        An IntegrationProvider is the name of an external application or
        service that can be connected to ProjectManager.com. The
        Integrations API is intended for use by ProjectManager and its
        business development partners. Please contact ProjectManager's
        sales team to request use of this API.

        Parameters
        ----------
        providerId : str
            The identifier to the provider
        """
        path = f"/api/data/integrations/providers/{providerId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_user_integration_provider_connection(self, providerId: str) -> AstroResult[DirectLinkDto]:
        """
        Retrieves user authentication information about a specific
        IntegrationProvider. This connection can be used for requests to
        Providers that require specific user data.

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
        path = f"/api/data/integrations/providers/{providerId}/user-connection"
        queryParams = {}
        result = self.client.send_request("POST", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=DirectLinkDto, data=json.loads(result.content)['data'])
            return AstroResult[DirectLinkDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[DirectLinkDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_user_integration_provider_connection(self, providerId: str, body: AuthenticationStatusDto) -> AstroResult[object]:
        """
        Allows you to update the auth status of the provider specific
        user connection.

        An IntegrationProvider is the name of an external application or
        service that can be connected to ProjectManager.com. The
        Integrations API is intended for use by ProjectManager and its
        business development partners. Please contact ProjectManager's
        sales team to request use of this API.

        Parameters
        ----------
        providerId : str
            The identifier to the provider
        body : AuthenticationStatusDto
            Specify the auth status
        """
        path = f"/api/data/integrations/providers/{providerId}/user-connection"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def disconnect_user_integration_provider_connection(self, providerId: str) -> AstroResult[object]:
        """
        Allows you to disconnect the provider specific user connection.

        An IntegrationProvider is the name of an external application or
        service that can be connected to ProjectManager.com. The
        Integrations API is intended for use by ProjectManager and its
        business development partners. Please contact ProjectManager's
        sales team to request use of this API.

        Parameters
        ----------
        providerId : str
            The identifier to the provider
        """
        path = f"/api/data/integrations/providers/{providerId}/user-connection"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
