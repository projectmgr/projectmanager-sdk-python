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
from ProjectManagerSdk.models.hourlyratecreatedto import HourlyRateCreateDto
from ProjectManagerSdk.models.hourlyratedetailsdto import HourlyRateDetailsDto
from ProjectManagerSdk.models.hourlyratedto import HourlyRateDto
from ProjectManagerSdk.models.hourlyratevaluedto import HourlyRateValueDto
from ProjectManagerSdk.models.hourlyratevalueupdatedto import HourlyRateValueUpdateDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class HourlyRateClient:
    """
    API methods related to HourlyRate
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def create_hourly_rate(self, body: HourlyRateCreateDto) -> AstroResult[HourlyRateDto]:
        """
        Create a hourly rate

        Parameters
        ----------
        body : HourlyRateCreateDto
            The rate data.
        """
        path = "/api/data/hourly-rates"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=HourlyRateDto, data=json.loads(result.content)['data'])
            return AstroResult[HourlyRateDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[HourlyRateDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def get_hourly_rates(self) -> AstroResult[List[HourlyRateDto]]:
        """
        All hourly rates including Inactive rates

        Parameters
        ----------
        """
        path = "/api/data/hourly-rates"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=HourlyRateDto, data=dict))
            return AstroResult[List[HourlyRateDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[HourlyRateDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_hourly_rate_value(self, rateValueId: str, body: HourlyRateValueUpdateDto) -> AstroResult[HourlyRateValueDto]:
        """
        Update Hourly Rate Value

        Parameters
        ----------
        rateValueId : str
            The rate valueId
        body : HourlyRateValueUpdateDto
            The rate value data
        """
        path = f"/api/data/hourly-rates/values/{rateValueId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=HourlyRateValueDto, data=json.loads(result.content)['data'])
            return AstroResult[HourlyRateValueDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[HourlyRateValueDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def get_hourly_rate(self, rateId: str) -> AstroResult[HourlyRateDetailsDto]:
        """
        Get Hourly Rate

        Parameters
        ----------
        rateId : str
            The unique identifier for the rate
        """
        path = f"/api/data/hourly-rates/{rateId}"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=HourlyRateDetailsDto, data=json.loads(result.content)['data'])
            return AstroResult[HourlyRateDetailsDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[HourlyRateDetailsDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def delete_hourly_rate(self, rateId: str) -> AstroResult[object]:
        """
        Delete a hourly rate

        Parameters
        ----------
        rateId : str
            The rate Id.
        """
        path = f"/api/data/hourly-rates/{rateId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
