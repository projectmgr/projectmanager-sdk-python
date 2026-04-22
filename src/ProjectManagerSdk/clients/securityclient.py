#
# ProjectManager API for Python
#
# (c) ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#

from ProjectManagerSdk.models.astroresult import AstroResult
from ProjectManagerSdk.models.businessroleslistdto import BusinessRolesListDto
from ProjectManagerSdk.models.rolecreatedto import RoleCreateDto
from ProjectManagerSdk.models.roledto import RoleDto
from ProjectManagerSdk.models.roleupdatechangeitemdto import RoleUpdateChangeItemDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class SecurityClient:
    """
    API methods related to Security
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def list_business_roles(self) -> AstroResult[BusinessRolesListDto]:
        """
        Returns every business role in the current workspace, including
        built-in and custom roles. Each role includes a permissions
        object with entitlement and grant state for the account security
        matrix.

        Parameters
        ----------
        """
        path = "/api/data/security/businessroles"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=BusinessRolesListDto, data=json.loads(result.content)['data'])
            return AstroResult[BusinessRolesListDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[BusinessRolesListDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_business_role(self, body: RoleCreateDto) -> AstroResult[RoleDto]:
        """
        Chargebee entitlements are evaluated read-only when saving
        permission grants; this call does not change subscription state.

        Parameters
        ----------
        body : RoleCreateDto
            Role name, optional description, and permission settings for
            the new role.
        """
        path = "/api/data/security/businessroles"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=RoleDto, data=json.loads(result.content)['data'])
            return AstroResult[RoleDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[RoleDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_business_role(self, roleId: str, body: List[RoleUpdateChangeItemDto]) -> AstroResult[RoleDto]:
        """
        Send property change sets using the same pattern as other
        workspace batch-update APIs. For permissions, include a
        permissions property with a partial or full permissions object;
        omitted keys are merged with the current role. Keys may use the
        same names as GET `permissions` (e.g. `editUsers`) or RetrieveMe
        / POST-create style (e.g. `editUser`). The response body matches
        create when successful.

        Parameters
        ----------
        roleId : str
            Business role identifier.
        body : List[RoleUpdateChangeItemDto]
            List of property name and value pairs to apply.
        """
        path = f"/api/data/security/businessroles/{roleId}"
        queryParams = {}
        bodyArray = []
        for item in body:
            bodyArray.append(remove_empty_elements(dataclasses.asdict(item)))
        result = self.client.send_request("PUT", path, bodyArray, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=RoleDto, data=json.loads(result.content)['data'])
            return AstroResult[RoleDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[RoleDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def delete_business_role(self, roleId: str) -> AstroResult[object]:
        """
        Built-in roles cannot be deleted. Users assigned to the role may
        need to be reassigned before the role can be removed.

        Parameters
        ----------
        roleId : str
            Identifier of the custom role to remove.
        """
        path = f"/api/data/security/businessroles/{roleId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def resend_email_validation(self) -> AstroResult[object]:
        """
        Sends another validation email to the authenticated user's
        workspace email address.

        Parameters
        ----------
        """
        path = "/api/data/security/email/validation/resend"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
