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
from ProjectManagerSdk.models.projectchargecodedto import ProjectChargeCodeDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class ProjectChargeCodeClient:
    """
    API methods related to ProjectChargeCode
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_charge_codes(self) -> AstroResult[List[ProjectChargeCodeDto]]:
        """
        Retrieve all defined ChargeCodes that can be used when creating
        Projects. A ChargeCode is a code used to identify costs within
        your Projects. Each ChargeCode has a name and a unique
        identifier. ChargeCodes are defined per Workspace and are shared
        among Projects.

        Parameters
        ----------
        """
        path = "/api/data/projects/chargecodes"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=ProjectChargeCodeDto, data=dict))
            return AstroResult[List[ProjectChargeCodeDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[ProjectChargeCodeDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
