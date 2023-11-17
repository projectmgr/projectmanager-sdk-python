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

from ProjectManagerSdk.models.apikeycreatedto import ApiKeyCreateDto
from ProjectManagerSdk.models.apikeydto import ApiKeyDto
from ProjectManagerSdk.models.astroresult import AstroResult
import json

class ApiKeyClient:
    """
    API methods related to ApiKey
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def create_api_key(self, body: ApiKeyCreateDto) -> AstroResult[ApiKeyDto]:
        """
        Creates a new API key for the current user with the specified
        options.

        An API key is a credential that you can use to make REST v4 API
        calls for ProjectManager.com. When you create a new API key,
        that API key is only visible in the response JSON for the
        `CreateApiKey` method. If you do not preserve this information,
        it cannot be recreated.

        Some best practices for working with API keys: * An API key is
        valid for a two year period after it is created. We encourage
        you to rotate your API keys regularly according to your
        company's security policies. * You should create separate API
        keys for each system that works with your API. If that API key
        is exposed or if that program needs to be shut down, you can
        revoke that one key and reissue it. * An API key is tied to the
        workspace that created it. A single API key can only interact
        with one workspace.

        Parameters
        ----------
        body : ApiKeyCreateDto
            Options for the API key to create
        """
        path = "/api/data/api-keys"
        queryParams = {}
        result = self.client.send_request("POST", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[ApiKeyDto](None, True, False, result.status_code, ApiKeyDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ApiKeyDto](result.json(), False, True, result.status_code, None)

    def list_api_keys(self) -> AstroResult[list[ApiKeyDto]]:
        """
        Returns a list of all API keys within the current workspace.

        An API key is a credential that you can use to make REST v4 API
        calls for ProjectManager.com. When you create a new API key,
        that API key is only visible in the response JSON for the
        `CreateApiKey` method. If you do not preserve this information,
        it cannot be recreated.

        Some best practices for working with API keys: * An API key is
        valid for a two year period after it is created. We encourage
        you to rotate your API keys regularly according to your
        company's security policies. * You should create separate API
        keys for each system that works with your API. If that API key
        is exposed or if that program needs to be shut down, you can
        revoke that one key and reissue it. * An API key is tied to the
        workspace that created it. A single API key can only interact
        with one workspace.

        Parameters
        ----------
        """
        path = "/api/data/api-keys"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(ApiKeyDto(**dict))
            return AstroResult[list[ApiKeyDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[ApiKeyDto]](result.json(), False, True, result.status_code, None)

    def revoke_all_api_keys(self) -> AstroResult[object]:
        """
        This API call revokes all existing API keys in given workspace.
        No existing keys will continue to work after this call
        completes. We strongly encourage you to revoke a single API key
        at a time; this method should only be used if you need to
        rapidly halt access to your product for automated systems.

        An API key is a credential that you can use to make REST v4 API
        calls for ProjectManager.com. When you create a new API key,
        that API key is only visible in the response JSON for the
        `CreateApiKey` method. If you do not preserve this information,
        it cannot be recreated.

        Some best practices for working with API keys: * An API key is
        valid for a two year period after it is created. We encourage
        you to rotate your API keys regularly according to your
        company's security policies. * You should create separate API
        keys for each system that works with your API. If that API key
        is exposed or if that program needs to be shut down, you can
        revoke that one key and reissue it. * An API key is tied to the
        workspace that created it. A single API key can only interact
        with one workspace.

        Parameters
        ----------
        """
        path = "/api/data/api-keys/revoke-all"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[object](None, True, False, result.status_code, object(**json.loads(result.content)['data']))
        else:
            return AstroResult[object](result.json(), False, True, result.status_code, None)

    def revoke_api_key(self, id: str) -> AstroResult[object]:
        """
        Revokes a single API key in the current workspace.

        An API key is a credential that you can use to make REST v4 API
        calls for ProjectManager.com. When you create a new API key,
        that API key is only visible in the response JSON for the
        `CreateApiKey` method. If you do not preserve this information,
        it cannot be recreated.

        Some best practices for working with API keys: * An API key is
        valid for a two year period after it is created. We encourage
        you to rotate your API keys regularly according to your
        company's security policies. * You should create separate API
        keys for each system that works with your API. If that API key
        is exposed or if that program needs to be shut down, you can
        revoke that one key and reissue it. * An API key is tied to the
        workspace that created it. A single API key can only interact
        with one workspace.

        Parameters
        ----------
        id : str
            The unique identifier of the API key to revoke
        """
        path = f"/api/data/api-keys/{id}/revoke"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[object](None, True, False, result.status_code, object(**json.loads(result.content)['data']))
        else:
            return AstroResult[object](result.json(), False, True, result.status_code, None)
