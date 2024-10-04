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
from ProjectManagerSdk.models.integrationdto import IntegrationDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class IntegrationClient:
    """
    API methods related to Integration
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_integration(self, integrationId: str) -> AstroResult[IntegrationDto]:
        """
        Retrieves an Integration specified by a unique identifier. The
        Integrations API is intended for use by ProjectManager and its
        business development partners. Please contact ProjectManager's
        sales team to request use of this API.

        Parameters
        ----------
        integrationId : str
            The unique identifier of this Integration
        """
        path = f"/api/data/integrations/{integrationId}"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=IntegrationDto, data=json.loads(result.content)['data'])
            return AstroResult[IntegrationDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[IntegrationDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def enable_integration(self, integrationId: str) -> AstroResult[IntegrationDto]:
        """
        Enable a specific Integration for the current Workspace. The
        Integrations API is intended for use by ProjectManager and its
        business development partners. Please contact ProjectManager's
        sales team to request use of this API.

        Parameters
        ----------
        integrationId : str
            The unique identifier of the Integration to enable
        """
        path = f"/api/data/integrations/{integrationId}"
        queryParams = {}
        result = self.client.send_request("POST", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=IntegrationDto, data=json.loads(result.content)['data'])
            return AstroResult[IntegrationDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[IntegrationDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def disable_integration(self, integrationId: str) -> AstroResult[object]:
        """
        Disable a specific Integration for the current Workspace. The
        Integrations API is intended for use by ProjectManager and its
        business development partners. Please contact ProjectManager's
        sales team to request use of this API.

        Parameters
        ----------
        integrationId : str
            The unique identifier of the Integration to disable
        """
        path = f"/api/data/integrations/{integrationId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def retrieve_all_integrations(self) -> AstroResult[List[IntegrationDto]]:
        """
        Retrieves all Integrations for the current Workspace. The
        Integrations API is intended for use by ProjectManager and its
        business development partners. Please contact ProjectManager's
        sales team to request use of this API.

        Parameters
        ----------
        """
        path = "/api/data/integrations"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=IntegrationDto, data=dict))
            return AstroResult[List[IntegrationDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[IntegrationDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
