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
from ProjectManagerSdk.models.dailyrecurringsettingsdto import DailyRecurringSettingsDto
from ProjectManagerSdk.models.deletedtasksdto import DeletedTasksDto
from ProjectManagerSdk.models.meetingcreatedto import MeetingCreateDto
from ProjectManagerSdk.models.meetingdetailsdto import MeetingDetailsDto
from ProjectManagerSdk.models.meetingdto import MeetingDto
from ProjectManagerSdk.models.meetingupdatedto import MeetingUpdateDto
from ProjectManagerSdk.models.monthlyrecurringsettingsdto import MonthlyRecurringSettingsDto
from ProjectManagerSdk.models.recurringtaskchangesetdetails import RecurringTaskChangeSetDetails
from ProjectManagerSdk.models.recurringtasksettingsdto import RecurringTaskSettingsDto
from ProjectManagerSdk.models.recurringtaskvalidationresultdto import RecurringTaskValidationResultDto
from ProjectManagerSdk.models.weeklyrecurringsettingsdto import WeeklyRecurringSettingsDto
from ProjectManagerSdk.models.yearlyrecurringsettingsdto import YearlyRecurringSettingsDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class MeetingsClient:
    """
    API methods related to Meetings
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def get_meeting(self, meetingId: str) -> AstroResult[MeetingDetailsDto]:
        """
        Retrieve a Meeting by its unique identifier or by its short ID.
        A Meeting has both a unique identifier, which is a GUID, and a
        short ID, which is a small text label that is unique only within
        your Workspace.

        Parameters
        ----------
        meetingId : str
            the id of the meeting
        """
        path = f"/api/data/meetings/{meetingId}"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=MeetingDetailsDto, data=json.loads(result.content)['data'])
            return AstroResult[MeetingDetailsDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[MeetingDetailsDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_meeting(self, meetingId: str, body: MeetingUpdateDto) -> AstroResult[MeetingDto]:
        """
        Updates a Meeting by its unique identifier, which is a GUID.

        Parameters
        ----------
        meetingId : str
            the id of the meeting
        body : MeetingUpdateDto
            the fields to update
        """
        path = f"/api/data/meetings/{meetingId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=MeetingDto, data=json.loads(result.content)['data'])
            return AstroResult[MeetingDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[MeetingDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def remove_meeting(self, meetingId: str) -> AstroResult[object]:
        """
        Removes a Meeting by its unique identifier, which is a GUID.

        Parameters
        ----------
        meetingId : str
            the id of the meeting to remove
        """
        path = f"/api/data/meetings/{meetingId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_meeting(self, body: MeetingCreateDto) -> AstroResult[MeetingDto]:
        """
        Creates a new Meeting for the current user. If you specify an
        assignee for this Meeting, that user will be assigned to it. If
        you do not specify an assignee, the Meeting will be
        automatically assigned to you.

        Parameters
        ----------
        body : MeetingCreateDto
            The data used to create the Meeting
        """
        path = "/api/data/meetings"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=MeetingDto, data=json.loads(result.content)['data'])
            return AstroResult[MeetingDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[MeetingDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_weekly_recurring_meetings(self, meetingId: str, body: WeeklyRecurringSettingsDto) -> AstroResult[RecurringTaskChangeSetDetails]:
        """
        Changes an existing Non-Project Task into a Recurring Task, so
        that it will recur regularly given the specified rules. A
        Recurring Task is one that must be completed on a specific
        regular frequency, such as Daily, Weekly, Monthly, or Yearly. To
        create a Recurring Task, you must first create a regular Task
        with the necessary information, then call one of the Create
        Recurring Task APIs. To remove an instance of a Recurring Task,
        call Delete Recurring Task and specify one or more instances of
        the Recurring Task.

        Parameters
        ----------
        meetingId : str
            The unique identifier of the Meeting
        body : WeeklyRecurringSettingsDto
            The weekly recurring settings
        """
        path = f"/api/data/meetings/{meetingId}/recurring/weekly"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=RecurringTaskChangeSetDetails, data=json.loads(result.content)['data'])
            return AstroResult[RecurringTaskChangeSetDetails](None, True, False, result.status_code, data)
        else:
            response = AstroResult[RecurringTaskChangeSetDetails](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_monthly_recurring_meetings(self, meetingId: str, body: MonthlyRecurringSettingsDto) -> AstroResult[RecurringTaskChangeSetDetails]:
        """
        Changes an existing Non-Project Task into a Recurring Task, so
        that it will recur regularly given the specified rules. A
        Recurring Task is one that must be completed on a specific
        regular frequency, such as Daily, Weekly, Monthly, or Yearly. To
        create a Recurring Task, you must first create a regular Task
        with the necessary information, then call one of the Create
        Recurring Task APIs. To remove an instance of a Recurring Task,
        call Delete Recurring Task and specify one or more instances of
        the Recurring Task.

        Parameters
        ----------
        meetingId : str
            The unique identifier of the Meeting
        body : MonthlyRecurringSettingsDto
            The monthly recurring settings
        """
        path = f"/api/data/meetings/{meetingId}/recurring/monthly"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=RecurringTaskChangeSetDetails, data=json.loads(result.content)['data'])
            return AstroResult[RecurringTaskChangeSetDetails](None, True, False, result.status_code, data)
        else:
            response = AstroResult[RecurringTaskChangeSetDetails](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_daily_recurring_meetings(self, meetingId: str, body: DailyRecurringSettingsDto) -> AstroResult[RecurringTaskChangeSetDetails]:
        """
        Changes an existing Non-Project Task into a Recurring Task, so
        that it will recur regularly given the specified rules. A
        Recurring Task is one that must be completed on a specific
        regular frequency, such as Daily, Weekly, Monthly, or Yearly. To
        create a Recurring Task, you must first create a regular Task
        with the necessary information, then call one of the Create
        Recurring Task APIs. To remove an instance of a Recurring Task,
        call Delete Recurring Task and specify one or more instances of
        the Recurring Task.

        Parameters
        ----------
        meetingId : str
            The unique identifier of the Meeting
        body : DailyRecurringSettingsDto
            The daily recurring settings
        """
        path = f"/api/data/meetings/{meetingId}/recurring/daily"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=RecurringTaskChangeSetDetails, data=json.loads(result.content)['data'])
            return AstroResult[RecurringTaskChangeSetDetails](None, True, False, result.status_code, data)
        else:
            response = AstroResult[RecurringTaskChangeSetDetails](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_yearly_recurring_meetings(self, meetingId: str, body: YearlyRecurringSettingsDto) -> AstroResult[RecurringTaskChangeSetDetails]:
        """
        Changes an existing Non-Project Task into a Recurring Task, so
        that it will recur regularly given the specified rules. A
        Recurring Task is one that must be completed on a specific
        regular frequency, such as Daily, Weekly, Monthly, or Yearly. To
        create a Recurring Task, you must first create a regular Task
        with the necessary information, then call one of the Create
        Recurring Task APIs. To remove an instance of a Recurring Task,
        call Delete Recurring Task and specify one or more instances of
        the Recurring Task.

        Parameters
        ----------
        meetingId : str
            The unique identifier of the Meeting
        body : YearlyRecurringSettingsDto
            The yearly recurring settings
        """
        path = f"/api/data/meetings/{meetingId}/recurring/yearly"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=RecurringTaskChangeSetDetails, data=json.loads(result.content)['data'])
            return AstroResult[RecurringTaskChangeSetDetails](None, True, False, result.status_code, data)
        else:
            response = AstroResult[RecurringTaskChangeSetDetails](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def delete_recurring_meetings(self, meetingId: str, option: str) -> AstroResult[DeletedTasksDto]:
        """
        Removes one or more instances of a Recurring Non-Project Task
        based on the `option` you specify: `this` means to remove a
        single instance, `all` means to remove all instances, or
        `future` means to remove all future instances of the Recurring
        Task. A Recurring Task is one that must be completed on a
        specific regular frequency, such as Daily, Weekly, Monthly, or
        Yearly. To create a Recurring Task, you must first create a
        regular Task with the necessary information, then call one of
        the Create Recurring Task APIs. To remove an instance of a
        Recurring Task, call Delete Recurring Task and specify one or
        more instances of the Recurring Task.

        Parameters
        ----------
        meetingId : str
            The unique identifier of the Recurring Meeting
        option : str
            The options for the deletion
        """
        path = f"/api/data/meetings/{meetingId}/recurring/{option}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=DeletedTasksDto, data=json.loads(result.content)['data'])
            return AstroResult[DeletedTasksDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[DeletedTasksDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def validate_recurring_meeting_settings(self, meetingId: str, body: RecurringTaskSettingsDto) -> AstroResult[RecurringTaskValidationResultDto]:
        """
        Reviews potential updates to a Recurring Non-Project Task and
        report back on the list of changes that would occur if this
        Recurring Non-Project Task was updated with these settings. When
        making changes to a Recurring Npt, you may want to investigate
        the consequences of your changes first before finalizing the
        changes. You can use the Validate Recurring Npts API to examine
        these changes. When you are happy with the changes, call Update
        Recurring Npts to complete them. A Recurring Task is one that
        must be completed on a specific regular frequency, such as
        Daily, Weekly, Monthly, or Yearly. To create a Recurring Task,
        you must first create a regular Task with the necessary
        information, then call one of the Create Recurring Task APIs. To
        remove an instance of a Recurring Task, call Delete Recurring
        Task and specify one or more instances of the Recurring Task.

        Parameters
        ----------
        meetingId : str
            The unique identifier of the Meeting
        body : RecurringTaskSettingsDto
            The new settings
        """
        path = f"/api/data/meetings/{meetingId}/recurring/settings/validate"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=RecurringTaskValidationResultDto, data=json.loads(result.content)['data'])
            return AstroResult[RecurringTaskValidationResultDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[RecurringTaskValidationResultDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_recurring_meeting_settings(self, meetingId: str, body: RecurringTaskSettingsDto) -> AstroResult[RecurringTaskChangeSetDetails]:
        """
        Updates the settings for a Recurring Non-Project Task and
        re-generates occurrences of the Recurring Non-Project Task from
        the new rules. When making changes to a Recurring Npt, you may
        want to investigate the consequences of your changes first
        before finalizing the changes. You can use the Validate
        Recurring Npts API to examine these changes. When you are happy
        with the changes, call Update Recurring Npts to complete them. A
        Recurring Task is one that must be completed on a specific
        regular frequency, such as Daily, Weekly, Monthly, or Yearly. To
        create a Recurring Task, you must first create a regular Task
        with the necessary information, then call one of the Create
        Recurring Task APIs. To remove an instance of a Recurring Task,
        call Delete Recurring Task and specify one or more instances of
        the Recurring Task.

        Parameters
        ----------
        meetingId : str
            The unique identifier of the Meeting
        body : RecurringTaskSettingsDto
            The new settings
        """
        path = f"/api/data/meetings/{meetingId}/recurring/settings"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=RecurringTaskChangeSetDetails, data=json.loads(result.content)['data'])
            return AstroResult[RecurringTaskChangeSetDetails](None, True, False, result.status_code, data)
        else:
            response = AstroResult[RecurringTaskChangeSetDetails](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
