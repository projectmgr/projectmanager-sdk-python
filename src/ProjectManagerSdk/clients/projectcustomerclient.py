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
from ProjectManagerSdk.models.projectcustomercreatedto import ProjectCustomerCreateDto
from ProjectManagerSdk.models.projectcustomerdto import ProjectCustomerDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class ProjectCustomerClient:
    """
    API methods related to ProjectCustomer
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_project_customers(self) -> AstroResult[List[ProjectCustomerDto]]:
        """
        Retrieves all ProjectCustomers defined within your Workspace. A
        ProjectCustomer is a code used to identify customers associated
        with your Projects. Each ProjectCustomer has a name and a unique
        identifier. ProjectCustomers are defined per Workspace and are
        shared among Projects.

        Parameters
        ----------
        """
        path = "/api/data/projects/customers"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=ProjectCustomerDto, data=dict))
            return AstroResult[List[ProjectCustomerDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[ProjectCustomerDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_project_customer(self, body: ProjectCustomerCreateDto) -> AstroResult[ProjectCustomerDto]:
        """
        Create a project customer

        Parameters
        ----------
        body : ProjectCustomerCreateDto
            The data to create the customer
        """
        path = "/api/data/projects/customers"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ProjectCustomerDto, data=json.loads(result.content)['data'])
            return AstroResult[ProjectCustomerDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ProjectCustomerDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_project_customer(self, customerId: str, body: ProjectCustomerCreateDto) -> AstroResult[ProjectCustomerDto]:
        """
        Updates a project customer

        Parameters
        ----------
        customerId : str
            The id of the customer to update
        body : ProjectCustomerCreateDto
            The data to update
        """
        path = f"/api/data/projects/customers/{customerId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ProjectCustomerDto, data=json.loads(result.content)['data'])
            return AstroResult[ProjectCustomerDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ProjectCustomerDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def delete_project_customer(self, customerId: str) -> AstroResult[object]:
        """
        Delete a project customer. They will also be removed from any
        projects they were assigned too.

        Parameters
        ----------
        customerId : str
            The id of the customer to remove
        """
        path = f"/api/data/projects/customers/{customerId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
