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
from ProjectManagerSdk.models.countrydto import CountryDto
from ProjectManagerSdk.models.statedto import StateDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class CountryClient:
    """
    API methods related to Country
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def list_countries(self) -> AstroResult[List[CountryDto]]:
        """
        This method returns a list of all countries defined by
        [ISO3166](https://www.iso.org/iso-3166-country-codes.html). Each
        country includes its unique identifier (ISO3166-2 code) and
        name.

        Parameters
        ----------
        """
        path = "/api/data/countries"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=CountryDto, data=dict))
            return AstroResult[List[CountryDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[CountryDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def get_states(self, isoCode: str) -> AstroResult[List[StateDto]]:
        """
        This method returns a list of all states for the specified
        country as defined by [ISO3166](https://www.iso.org/iso-3166-country-codes.html).
        Note that many countries may have administrative regions
        although not all countries require administrative regions to be
        used when specifying an address. Each state includes its unique
        identifier, state code, and name.

        Parameters
        ----------
        isoCode : str
            The ISO-3166-2 code of the country
        """
        path = f"/api/data/countries/{isoCode}/states"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=StateDto, data=dict))
            return AstroResult[List[StateDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[StateDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
