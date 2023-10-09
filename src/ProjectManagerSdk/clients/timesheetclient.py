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

from ProjectManagerSdk.models.astroresult import AstroResult
from ProjectManagerSdk.models.timesheetadmintypedto import TimesheetAdminTypeDto
from ProjectManagerSdk.models.timesheetcreaterequestdto import TimesheetCreateRequestDto
from ProjectManagerSdk.models.timesheetgetresponsedto import TimesheetGetResponseDto
from ProjectManagerSdk.models.timesheetresponsedto import TimesheetResponseDto
from ProjectManagerSdk.models.timesheetupdaterequestdto import TimesheetUpdateRequestDto
import json

class TimesheetClient:
    """
    API methods related to Timesheet
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def create_time_entry(self, body: TimesheetCreateRequestDto) -> AstroResult[TimesheetResponseDto]:
        """
        Creates new time entry for given resource on given day.

        Parameters
        ----------
        body : TimesheetCreateRequestDto
            Payload
        """
        path = "/api/data/timesheets"
        queryParams = {}
        result = self.client.send_request("POST", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[TimesheetResponseDto](None, True, False, result.status_code, TimesheetResponseDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[TimesheetResponseDto](result.json(), False, True, result.status_code, None)

    def query_timesheets(self, top: int, skip: int, filter: str, select: str, orderby: str, expand: str) -> AstroResult[list[TimesheetGetResponseDto]]:
        """
        Retrieve a list of TimeSheets that match an [OData formatted
        query](https://www.odata.org/).

        Time Sheets is a list of times per task

        Parameters
        ----------
        $top : int
            The number of records to return
        $skip : int
            Skips the given number of records and then returns $top
            records
        $filter : str
            Filter the expression according to oData queries
        $select : str
            Specify which properties should be returned
        $orderby : str
            Order collection by this field.
        $expand : str
            Include related data in the response
        """
        path = "/api/data/timesheets"
        queryParams = {}
        if top:
            queryParams['$top'] = top
        if skip:
            queryParams['$skip'] = skip
        if filter:
            queryParams['$filter'] = filter
        if select:
            queryParams['$select'] = select
        if orderby:
            queryParams['$orderby'] = orderby
        if expand:
            queryParams['$expand'] = expand
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(TimesheetGetResponseDto(**dict))
            return AstroResult[list[TimesheetGetResponseDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[TimesheetGetResponseDto]](result.json(), False, True, result.status_code, None)

    def delete_time_entry(self, timesheetId: str) -> AstroResult[object]:
        """
        Delete time entry by id.

        Parameters
        ----------
        timesheetId : str
            time entry id
        """
        path = f"/api/data/timesheets/{timesheetId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[object](None, True, False, result.status_code, object(**json.loads(result.content)['data']))
        else:
            return AstroResult[object](result.json(), False, True, result.status_code, None)

    def update_time_entry(self, timesheetId: str, body: TimesheetUpdateRequestDto) -> AstroResult[TimesheetResponseDto]:
        """
        Updates a time entry by its unique identifier.

        Parameters
        ----------
        timesheetId : str
            time entry id
        body : TimesheetUpdateRequestDto
            payload
        """
        path = f"/api/data/timesheets/{timesheetId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[TimesheetResponseDto](None, True, False, result.status_code, TimesheetResponseDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[TimesheetResponseDto](result.json(), False, True, result.status_code, None)

    def returns_active_admin_tasks_that_are_used_to_report_time(self) -> AstroResult[list[TimesheetAdminTypeDto]]:
        """
        Returns active admin tasks that are used to report time not
        related to work on projects. I.e. annual/sick leave etc

        Parameters
        ----------
        """
        path = "/api/data/timesheets/admin-tasks"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(TimesheetAdminTypeDto(**dict))
            return AstroResult[list[TimesheetAdminTypeDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[TimesheetAdminTypeDto]](result.json(), False, True, result.status_code, None)
