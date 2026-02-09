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
from ProjectManagerSdk.models.hourlyrateperiodcreatedto import HourlyRatePeriodCreateDto
from ProjectManagerSdk.models.hourlyrateperioddto import HourlyRatePeriodDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class HourlyRatePeriodClient:
    """
    API methods related to HourlyRatePeriod
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def get_rate_periods(self) -> AstroResult[List[HourlyRatePeriodDto]]:
        """
        Gets a list of all rate periods in a work space

        Parameters
        ----------
        """
        path = "/api/data/hourly-rate-periods"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=HourlyRatePeriodDto, data=dict))
            return AstroResult[List[HourlyRatePeriodDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[HourlyRatePeriodDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_rate_period(self, body: HourlyRatePeriodCreateDto) -> AstroResult[HourlyRatePeriodDto]:
        """
        Creates a rate period

        Parameters
        ----------
        body : HourlyRatePeriodCreateDto
            The rate period start date.
        """
        path = "/api/data/hourly-rate-periods"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=HourlyRatePeriodDto, data=json.loads(result.content)['data'])
            return AstroResult[HourlyRatePeriodDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[HourlyRatePeriodDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
