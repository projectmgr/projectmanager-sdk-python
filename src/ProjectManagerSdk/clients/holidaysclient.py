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
from ProjectManagerSdk.models.holidaycreatedto import HolidayCreateDto
from ProjectManagerSdk.models.holidaydetaildto import HolidayDetailDto
from ProjectManagerSdk.models.holidaylistitemdto import HolidayListItemDto
from ProjectManagerSdk.models.holidayupdatedto import HolidayUpdateDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class HolidaysClient:
    """
    API methods related to Holidays
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def list_holidays(self) -> AstroResult[List[HolidayListItemDto]]:
        """
        Returns all Holidays defined in the current workspace, sorted by
        name. This "list" API returns basic information about Holidays
        and may be restricted to partial information. To receive all
        information about a specific Holiday, use RetrieveHoliday. A
        Holiday is a defined date when one or more Resources are not
        available for work. Holidays may be defined by Workspace, by
        Country, or by Resource. A Workspace Holiday means that no
        Resources in the Workspace are working for that date. A Country
        Holiday means that no Resources in the Workspace located within
        the country are working for that date. A Resource Holiday means
        that the specified Resource is not working on that date.

        Parameters
        ----------
        """
        path = "/api/data/holidays"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=HolidayListItemDto, data=dict))
            return AstroResult[List[HolidayListItemDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[HolidayListItemDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_holidays(self, body: HolidayCreateDto) -> AstroResult[List[HolidayDetailDto]]:
        """
        Creates one or more Holiday for a Resource, a Country, or the
        entire Workspace. A Holiday can be created based on multiple
        crtieria, including a date range, a list of Resource
        identifiers, and a list of countries. You may use one or more of
        these criteria when calling CreateHolidays, and the API will
        expand your criteria into individual Holiday records for each
        combination of criteria. A Holiday is a defined date when one or
        more Resources are not available for work. Holidays may be
        defined by Workspace, by Country, or by Resource. A Workspace
        Holiday means that no Resources in the Workspace are working for
        that date. A Country Holiday means that no Resources in the
        Workspace located within the country are working for that date.
        A Resource Holiday means that the specified Resource is not
        working on that date.

        Parameters
        ----------
        body : HolidayCreateDto
            The information about the Holiday to create
        """
        path = "/api/data/holidays"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=HolidayDetailDto, data=dict))
            return AstroResult[List[HolidayDetailDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[HolidayDetailDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def retrieve_holiday(self, id: str) -> AstroResult[HolidayDetailDto]:
        """
        Retrieve all detail about a single Holiday defined by its unique
        identifier. A Holiday is a defined date when one or more
        Resources are not available for work. Holidays may be defined by
        Workspace, by Country, or by Resource. A Workspace Holiday means
        that no Resources in the Workspace are working for that date. A
        Country Holiday means that no Resources in the Workspace located
        within the country are working for that date. A Resource Holiday
        means that the specified Resource is not working on that date.

        Parameters
        ----------
        id : str
            Unique identifier of the holiday
        """
        path = f"/api/data/holidays/{id}"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=HolidayDetailDto, data=json.loads(result.content)['data'])
            return AstroResult[HolidayDetailDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[HolidayDetailDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_holiday_name(self, id: str, body: HolidayUpdateDto) -> AstroResult[HolidayDetailDto]:
        """
        Update the name of a Holiday based on the information provided.
        The Holiday record has a "name" or "reason" that can be used to
        identify the name of the Holiday. When a Holiday is specific to
        an individual person, it may have a reason identifying why the
        resource is taking paid time off. You can update this name or
        reason, but you cannot change the other values for a Holiday. To
        change a Holiday's date, resource ID, or country, you must
        delete the Holiday and create a new one. A Holiday is a defined
        date when one or more Resources are not available for work.
        Holidays may be defined by Workspace, by Country, or by
        Resource. A Workspace Holiday means that no Resources in the
        Workspace are working for that date. A Country Holiday means
        that no Resources in the Workspace located within the country
        are working for that date. A Resource Holiday means that the
        specified Resource is not working on that date.

        Parameters
        ----------
        id : str
            Unique identifier of the holiday
        body : HolidayUpdateDto
            Information to be updated for the Holiday
        """
        path = f"/api/data/holidays/{id}"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=HolidayDetailDto, data=json.loads(result.content)['data'])
            return AstroResult[HolidayDetailDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[HolidayDetailDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def delete_holiday(self, id: str) -> AstroResult[object]:
        """
        Removes the Holiday identified by its unique identifier. Some
        information about a Holiday cannot be updated once the Holiday
        is created. If you want to change the name or reason for a
        Holiday, you can use `UpdateHoliday`. To change other
        information, you should delete the old Holiday and create a new
        one with the correct information. A Holiday is a defined date
        when one or more Resources are not available for work. Holidays
        may be defined by Workspace, by Country, or by Resource. A
        Workspace Holiday means that no Resources in the Workspace are
        working for that date. A Country Holiday means that no Resources
        in the Workspace located within the country are working for that
        date. A Resource Holiday means that the specified Resource is
        not working on that date.

        Parameters
        ----------
        id : str
            Unique identifier of the holiday
        """
        path = f"/api/data/holidays/{id}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
