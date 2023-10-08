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
from ProjectManager.SDK.models.apikeycreatedto import ApiKeyCreateDto
from ProjectManager.SDK.models.apikeydto import ApiKeyDto
from ProjectManager.SDK.models.apikeydtolist import ApiKeyDtoList

class ApiKeyClient:
    """
    API methods related to ApiKey
    """
    from ProjectManager.SDK.project_manager_client import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def creates_an_api_key_for_the_current_user(self, body: ApiKeyCreateDto) -> AstroResult[AstroResult[ApiKeyDto]]:
        """
        Returns new api key

        Parameters
        ----------
        body : ApiKeyCreateDto
            api key details
        """
        path = "/api/data/api-keys"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ApiKeyDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def returns_list_of_created_api_keys_for_current_workspace(self, ) -> AstroResult[AstroResult[ApiKeyDtoList]]:
        """
        Returns list of workspace's api keys

        Parameters
        ----------
        """
        path = "/api/data/api-keys"
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ApiKeyDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def revokes_all_api_keys(self, ) -> AstroResult[AstroResult[]]:
        """
        Revokes all api keys in given workspace

        Parameters
        ----------
        """
        path = "/api/data/api-keys/revoke-all"
        result = self.client.send_request("DELETE", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def revoke_single_api_key(self, id: str) -> AstroResult[AstroResult[]]:
        """
        Revoke single api key in given workspace

        Parameters
        ----------
        id : str
            Internal key id
        """
        path = f"/api/data/api-keys/{id}/revoke"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))
