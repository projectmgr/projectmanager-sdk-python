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
from ProjectManagerSdk.models.countryholidaydto import CountryHolidayDto
from ProjectManagerSdk.models.globalholidaydto import GlobalHolidayDto
from ProjectManagerSdk.models.resourceholidaydto import ResourceHolidayDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class HolidayClient:
    """
    API methods related to Holiday
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def query_resource_holidays(self, top: int, skip: int, filter: str, orderby: str, expand: str) -> AstroResult[List[ResourceHolidayDto]]:
        """
        Retrieve a list of resource holidays that match an [OData
        formatted query](https://www.odata.org/).

        Parameters
        ----------
        $top : int
            The number of records to return
        $skip : int
            Skips the given number of records and then returns $top
            records
        $filter : str
            Filter the expression according to oData queries
        $orderby : str
            Order collection by this field.
        $expand : str
            Include related data in the response
        """
        path = "/api/data/holidays/resource"
        queryParams = {}
        if top:
            queryParams['$top'] = top
        if skip:
            queryParams['$skip'] = skip
        if filter:
            queryParams['$filter'] = filter
        if orderby:
            queryParams['$orderby'] = orderby
        if expand:
            queryParams['$expand'] = expand
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=ResourceHolidayDto, data=dict))
            return AstroResult[List[ResourceHolidayDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[ResourceHolidayDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def query_country_holidays(self, top: int, skip: int, filter: str, orderby: str, expand: str) -> AstroResult[List[CountryHolidayDto]]:
        """
        Retrieve a list of country holidays that match an [OData
        formatted query](https://www.odata.org/).

        Parameters
        ----------
        $top : int
            The number of records to return
        $skip : int
            Skips the given number of records and then returns $top
            records
        $filter : str
            Filter the expression according to oData queries
        $orderby : str
            Order collection by this field.
        $expand : str
            Include related data in the response
        """
        path = "/api/data/holidays/country"
        queryParams = {}
        if top:
            queryParams['$top'] = top
        if skip:
            queryParams['$skip'] = skip
        if filter:
            queryParams['$filter'] = filter
        if orderby:
            queryParams['$orderby'] = orderby
        if expand:
            queryParams['$expand'] = expand
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=CountryHolidayDto, data=dict))
            return AstroResult[List[CountryHolidayDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[CountryHolidayDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def query_global_holidays(self, top: int, skip: int, filter: str, orderby: str, expand: str) -> AstroResult[List[GlobalHolidayDto]]:
        """
        Retrieve a list of global holidays that match an [OData
        formatted query](https://www.odata.org/).

        Parameters
        ----------
        $top : int
            The number of records to return
        $skip : int
            Skips the given number of records and then returns $top
            records
        $filter : str
            Filter the expression according to oData queries
        $orderby : str
            Order collection by this field.
        $expand : str
            Include related data in the response
        """
        path = "/api/data/holidays/global"
        queryParams = {}
        if top:
            queryParams['$top'] = top
        if skip:
            queryParams['$skip'] = skip
        if filter:
            queryParams['$filter'] = filter
        if orderby:
            queryParams['$orderby'] = orderby
        if expand:
            queryParams['$expand'] = expand
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=GlobalHolidayDto, data=dict))
            return AstroResult[List[GlobalHolidayDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[GlobalHolidayDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
