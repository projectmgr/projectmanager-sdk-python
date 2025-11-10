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
from ProjectManagerSdk.models.timesheetadmintypedto import TimesheetAdminTypeDto
from ProjectManagerSdk.models.timesheetapprovaldto import TimeSheetApprovalDto
from ProjectManagerSdk.models.timesheetapprovalrejectdto import TimeSheetApprovalRejectDto
from ProjectManagerSdk.models.timesheetapprovalresponsedto import TimeSheetApprovalResponseDto
from ProjectManagerSdk.models.timesheetcreaterequestdto import TimesheetCreateRequestDto
from ProjectManagerSdk.models.timesheetdto import TimesheetDto
from ProjectManagerSdk.models.timesheetresponsedto import TimesheetResponseDto
from ProjectManagerSdk.models.timesheetupdaterequestdto import TimesheetUpdateRequestDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class TimesheetClient:
    """
    API methods related to Timesheet
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def create_time_entry(self, body: TimesheetCreateRequestDto) -> AstroResult[TimesheetResponseDto]:
        """
        Creates new time entry for Resource on a given day. A Timesheet
        is a collection of time entries for a particular Resource for a
        specific week. Each time entry records the number of whole
        minutes spent by this Resource on an activity. An activity can
        be a Task in any project that Resource can access, or the
        activity can be an administrative task such as "Sick Leave" or
        "Meetings". When a time entry is linked to a Task, the number of
        minutes spent on the time entry are recorded as time spent on
        the Task. Time entries linked to an administrative tasks are
        grouped for reporting but are not added to any Task within your
        Workspace. Time entries are recorded in whole minutes. If you
        specify a time entry in fractional hours, either using the API
        or via the web application, the amount you specify will be
        converted to minutes and rounded to the nearest neighbor using
        the rounding algorithm Midpoint-Away-From-Zero. When a Timesheet
        is submitted for approval or approved, users are no longer
        permitted to create, update, or delete time entries for that
        week. Users with Global Admin level access can override this
        restriction and continue to make changes to a Timesheet after
        approval.

        Parameters
        ----------
        body : TimesheetCreateRequestDto
            The time entry you wish to create
        """
        path = "/api/data/timesheets"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=TimesheetResponseDto, data=json.loads(result.content)['data'])
            return AstroResult[TimesheetResponseDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[TimesheetResponseDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def query_time_entries(self, top: int, skip: int, filter: str, orderby: str, expand: str) -> AstroResult[List[TimesheetDto]]:
        """
        Retrieve a list of time entries that match an [OData formatted
        query](https://www.odata.org/). A Timesheet is a collection of
        time entries for a particular Resource for a specific week. Each
        time entry records the number of whole minutes spent by this
        Resource on an activity. An activity can be a Task in any
        project that Resource can access, or the activity can be an
        administrative task such as "Sick Leave" or "Meetings". When a
        time entry is linked to a Task, the number of minutes spent on
        the time entry are recorded as time spent on the Task. Time
        entries linked to an administrative tasks are grouped for
        reporting but are not added to any Task within your Workspace.
        Time entries are recorded in whole minutes. If you specify a
        time entry in fractional hours, either using the API or via the
        web application, the amount you specify will be converted to
        minutes and rounded to the nearest neighbor using the rounding
        algorithm Midpoint-Away-From-Zero. When a Timesheet is submitted
        for approval or approved, users are no longer permitted to
        create, update, or delete time entries for that week. Users with
        Global Admin level access can override this restriction and
        continue to make changes to a Timesheet after approval.

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
        path = "/api/data/timesheets"
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
                data.append(dacite.from_dict(data_class=TimesheetDto, data=dict))
            return AstroResult[List[TimesheetDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[TimesheetDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def delete_time_entry(self, timesheetId: str) -> AstroResult[object]:
        """
        Delete time entry by its unique identifier. A Timesheet is a
        collection of time entries for a particular Resource for a
        specific week. Each time entry records the number of whole
        minutes spent by this Resource on an activity. An activity can
        be a Task in any project that Resource can access, or the
        activity can be an administrative task such as "Sick Leave" or
        "Meetings". When a time entry is linked to a Task, the number of
        minutes spent on the time entry are recorded as time spent on
        the Task. Time entries linked to an administrative tasks are
        grouped for reporting but are not added to any Task within your
        Workspace. Time entries are recorded in whole minutes. If you
        specify a time entry in fractional hours, either using the API
        or via the web application, the amount you specify will be
        converted to minutes and rounded to the nearest neighbor using
        the rounding algorithm Midpoint-Away-From-Zero. When a Timesheet
        is submitted for approval or approved, users are no longer
        permitted to create, update, or delete time entries for that
        week. Users with Global Admin level access can override this
        restriction and continue to make changes to a Timesheet after
        approval.

        Parameters
        ----------
        timesheetId : str
            The unique identifier of the time entry to delete
        """
        path = f"/api/data/timesheets/{timesheetId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_time_entry(self, timesheetId: str, body: TimesheetUpdateRequestDto) -> AstroResult[TimesheetResponseDto]:
        """
        Updates a time entry by its unique identifier. A Timesheet is a
        collection of time entries for a particular Resource for a
        specific week. Each time entry records the number of whole
        minutes spent by this Resource on an activity. An activity can
        be a Task in any project that Resource can access, or the
        activity can be an administrative task such as "Sick Leave" or
        "Meetings". When a time entry is linked to a Task, the number of
        minutes spent on the time entry are recorded as time spent on
        the Task. Time entries linked to an administrative tasks are
        grouped for reporting but are not added to any Task within your
        Workspace. Time entries are recorded in whole minutes. If you
        specify a time entry in fractional hours, either using the API
        or via the web application, the amount you specify will be
        converted to minutes and rounded to the nearest neighbor using
        the rounding algorithm Midpoint-Away-From-Zero. When a Timesheet
        is submitted for approval or approved, users are no longer
        permitted to create, update, or delete time entries for that
        week. Users with Global Admin level access can override this
        restriction and continue to make changes to a Timesheet after
        approval.

        Parameters
        ----------
        timesheetId : str
            The unique identifier of the time entry to update
        body : TimesheetUpdateRequestDto
            The new information that should replace the previous time
            entry
        """
        path = f"/api/data/timesheets/{timesheetId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=TimesheetResponseDto, data=json.loads(result.content)['data'])
            return AstroResult[TimesheetResponseDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[TimesheetResponseDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def retrieve_administrative_tasks(self) -> AstroResult[List[TimesheetAdminTypeDto]]:
        """
        Retrieves a list of Administrative Tasks that are defined for
        use within your Workspace. Administrative tasks are a list of
        regular, recurring non-Task actions that are typically
        associated with overhead, such as sick leave, travel, or
        attending meetings. A Timesheet is a collection of time entries
        for a particular Resource for a specific week. Each time entry
        records the number of whole minutes spent by this Resource on an
        activity. An activity can be a Task in any project that Resource
        can access, or the activity can be an administrative task such
        as "Sick Leave" or "Meetings". When a time entry is linked to a
        Task, the number of minutes spent on the time entry are recorded
        as time spent on the Task. Time entries linked to an
        administrative tasks are grouped for reporting but are not added
        to any Task within your Workspace. Time entries are recorded in
        whole minutes. If you specify a time entry in fractional hours,
        either using the API or via the web application, the amount you
        specify will be converted to minutes and rounded to the nearest
        neighbor using the rounding algorithm Midpoint-Away-From-Zero.
        When a Timesheet is submitted for approval or approved, users
        are no longer permitted to create, update, or delete time
        entries for that week. Users with Global Admin level access can
        override this restriction and continue to make changes to a
        Timesheet after approval.

        Parameters
        ----------
        """
        path = "/api/data/timesheets/admin-tasks"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=TimesheetAdminTypeDto, data=dict))
            return AstroResult[List[TimesheetAdminTypeDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[TimesheetAdminTypeDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def submit_timesheet(self, body: TimeSheetApprovalDto) -> AstroResult[TimeSheetApprovalResponseDto]:
        """
        Submit a Timesheet for approval for a specific Resource and
        week. A Timesheet is a collection of time entries for a
        particular Resource for a specific week. Each time entry records
        the number of whole minutes spent by this Resource on an
        activity. An activity can be a Task in any project that Resource
        can access, or the activity can be an administrative task such
        as "Sick Leave" or "Meetings". When a time entry is linked to a
        Task, the number of minutes spent on the time entry are recorded
        as time spent on the Task. Time entries linked to an
        administrative tasks are grouped for reporting but are not added
        to any Task within your Workspace. Time entries are recorded in
        whole minutes. If you specify a time entry in fractional hours,
        either using the API or via the web application, the amount you
        specify will be converted to minutes and rounded to the nearest
        neighbor using the rounding algorithm Midpoint-Away-From-Zero.
        When a Timesheet is submitted for approval or approved, users
        are no longer permitted to create, update, or delete time
        entries for that week. Users with Global Admin level access can
        override this restriction and continue to make changes to a
        Timesheet after approval.

        Parameters
        ----------
        body : TimeSheetApprovalDto
            The Timesheet to be submitted for approval
        """
        path = "/api/data/timesheets/approvals"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=TimeSheetApprovalResponseDto, data=json.loads(result.content)['data'])
            return AstroResult[TimeSheetApprovalResponseDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[TimeSheetApprovalResponseDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def approve_timesheet(self, body: TimeSheetApprovalDto) -> AstroResult[TimeSheetApprovalResponseDto]:
        """
        Approve an existing Timesheet approval request. A Timesheet is a
        collection of time entries for a particular Resource for a
        specific week. Each time entry records the number of whole
        minutes spent by this Resource on an activity. An activity can
        be a Task in any project that Resource can access, or the
        activity can be an administrative task such as "Sick Leave" or
        "Meetings". When a time entry is linked to a Task, the number of
        minutes spent on the time entry are recorded as time spent on
        the Task. Time entries linked to an administrative tasks are
        grouped for reporting but are not added to any Task within your
        Workspace. Time entries are recorded in whole minutes. If you
        specify a time entry in fractional hours, either using the API
        or via the web application, the amount you specify will be
        converted to minutes and rounded to the nearest neighbor using
        the rounding algorithm Midpoint-Away-From-Zero. When a Timesheet
        is submitted for approval or approved, users are no longer
        permitted to create, update, or delete time entries for that
        week. Users with Global Admin level access can override this
        restriction and continue to make changes to a Timesheet after
        approval.

        Parameters
        ----------
        body : TimeSheetApprovalDto
            The Timesheet to approve
        """
        path = "/api/data/timesheets/approvals/approve"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=TimeSheetApprovalResponseDto, data=json.loads(result.content)['data'])
            return AstroResult[TimeSheetApprovalResponseDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[TimeSheetApprovalResponseDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def reject_timesheet(self, body: TimeSheetApprovalRejectDto) -> AstroResult[TimeSheetApprovalResponseDto]:
        """
        Rejects a specific resource's Timesheet approval request for a
        specific week. A Timesheet is a collection of time entries for a
        particular Resource for a specific week. Each time entry records
        the number of whole minutes spent by this Resource on an
        activity. An activity can be a Task in any project that Resource
        can access, or the activity can be an administrative task such
        as "Sick Leave" or "Meetings". When a time entry is linked to a
        Task, the number of minutes spent on the time entry are recorded
        as time spent on the Task. Time entries linked to an
        administrative tasks are grouped for reporting but are not added
        to any Task within your Workspace. Time entries are recorded in
        whole minutes. If you specify a time entry in fractional hours,
        either using the API or via the web application, the amount you
        specify will be converted to minutes and rounded to the nearest
        neighbor using the rounding algorithm Midpoint-Away-From-Zero.
        When a Timesheet is submitted for approval or approved, users
        are no longer permitted to create, update, or delete time
        entries for that week. Users with Global Admin level access can
        override this restriction and continue to make changes to a
        Timesheet after approval.

        Parameters
        ----------
        body : TimeSheetApprovalRejectDto
            Information about the Timesheet approval request to be
            rejected
        """
        path = "/api/data/timesheets/approvals/reject"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=TimeSheetApprovalResponseDto, data=json.loads(result.content)['data'])
            return AstroResult[TimeSheetApprovalResponseDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[TimeSheetApprovalResponseDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
