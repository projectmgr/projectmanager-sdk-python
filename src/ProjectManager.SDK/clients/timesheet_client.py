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
from ProjectManager.SDK.models.timesheetadmintypedtolist import TimesheetAdminTypeDtoList
from ProjectManager.SDK.models.timesheetcreaterequestdto import TimesheetCreateRequestDto
from ProjectManager.SDK.models.timesheetgetresponsedtolist import TimesheetGetResponseDtoList
from ProjectManager.SDK.models.timesheetresponsedto import TimesheetResponseDto
from ProjectManager.SDK.models.timesheetupdaterequestdto import TimesheetUpdateRequestDto

class TimesheetClient:
    """
    API methods related to Timesheet
    """
    from ProjectManager.SDK.project_manager_client import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def create_time_entry(self, body: TimesheetCreateRequestDto) -> AstroResult[AstroResult[TimesheetResponseDto]]:
        """
        Creates new time entry for given resource on given day.

        Parameters
        ----------
        body : TimesheetCreateRequestDto
            Payload
        """
        path = "/api/data/timesheets"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), TimesheetResponseDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_timesheets(self, $top: int, $skip: int, $filter: str, $select: str, $orderby: str, $expand: str) -> AstroResult[AstroResult[TimesheetGetResponseDtoList]]:
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
        result = self.client.send_request("GET", path, None, {"$top": $top, "$skip": $skip, "$filter": $filter, "$select": $select, "$orderby": $orderby, "$expand": $expand}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), TimesheetGetResponseDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_time_entry(self, timesheetId: str) -> AstroResult[AstroResult[]]:
        """
        Delete time entry by id.

        Parameters
        ----------
        timesheetId : str
            time entry id
        """
        path = f"/api/data/timesheets/{timesheetId}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), ), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_time_entry(self, timesheetId: str, body: TimesheetUpdateRequestDto) -> AstroResult[AstroResult[TimesheetResponseDto]]:
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
        result = self.client.send_request("PUT", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), TimesheetResponseDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def returns_active_admin_tasks_that_are_used_to_report_time(self, ) -> AstroResult[AstroResult[TimesheetAdminTypeDtoList]]:
        """
        Returns active admin tasks that are used to report time not
        related to work on projects. I.e. annual/sick leave etc

        Parameters
        ----------
        """
        path = "/api/data/timesheets/admin-tasks"
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), TimesheetAdminTypeDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))
