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
from ProjectManagerSdk.models.changesetstatusdto import ChangeSetStatusDto
from ProjectManagerSdk.models.dailyrecurringsettingsdto import DailyRecurringSettingsDto
from ProjectManagerSdk.models.monthlyrecurringsettingsdto import MonthlyRecurringSettingsDto
from ProjectManagerSdk.models.recurringtaskchangesetdetails import RecurringTaskChangeSetDetails
from ProjectManagerSdk.models.recurringtaskchangesetdetailschangesetstatusdto import RecurringTaskChangeSetDetailsChangeSetStatusDto
from ProjectManagerSdk.models.recurringtasksettingsdto import RecurringTaskSettingsDto
from ProjectManagerSdk.models.recurringtaskvalidationresultdto import RecurringTaskValidationResultDto
from ProjectManagerSdk.models.weeklyrecurringsettingsdto import WeeklyRecurringSettingsDto
from ProjectManagerSdk.models.yearlyrecurringsettingsdto import YearlyRecurringSettingsDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class TaskRecurrencyClient:
    """
    API methods related to TaskRecurrency
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def create_weekly_recurring_tasks(self, taskId: str, body: WeeklyRecurringSettingsDto) -> AstroResult[RecurringTaskChangeSetDetailsChangeSetStatusDto]:
        """
        Changes an existing Task into a Recurring Task, so that it will
        recur regularly given the specified rules. A Recurring Task is
        one that must be completed on a specific regular frequency, such
        as Daily, Weekly, Monthly, or Yearly. To create a Recurring
        Task, you must first create a regular Task with the necessary
        information, then call one of the Create Recurring Task APIs. To
        remove an instance of a Recurring Task, call Delete Recurring
        Task and specify one or more instances of the Recurring Task.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task
        body : WeeklyRecurringSettingsDto
            The weekly recurring settings
        """
        path = f"/api/data/tasks/{taskId}/recurring/weekly"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=RecurringTaskChangeSetDetailsChangeSetStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[RecurringTaskChangeSetDetailsChangeSetStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[RecurringTaskChangeSetDetailsChangeSetStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_monthly_recurring_tasks(self, taskId: str, body: MonthlyRecurringSettingsDto) -> AstroResult[RecurringTaskChangeSetDetailsChangeSetStatusDto]:
        """
        Changes an existing Task into a Recurring Task, so that it will
        recur regularly given the specified rules. A Recurring Task is
        one that must be completed on a specific regular frequency, such
        as Daily, Weekly, Monthly, or Yearly. To create a Recurring
        Task, you must first create a regular Task with the necessary
        information, then call one of the Create Recurring Task APIs. To
        remove an instance of a Recurring Task, call Delete Recurring
        Task and specify one or more instances of the Recurring Task.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task
        body : MonthlyRecurringSettingsDto
            The monthly recurring settings
        """
        path = f"/api/data/tasks/{taskId}/recurring/monthly"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=RecurringTaskChangeSetDetailsChangeSetStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[RecurringTaskChangeSetDetailsChangeSetStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[RecurringTaskChangeSetDetailsChangeSetStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_daily_recurring_tasks(self, taskId: str, body: DailyRecurringSettingsDto) -> AstroResult[RecurringTaskChangeSetDetailsChangeSetStatusDto]:
        """
        Changes an existing Task into a Recurring Task, so that it will
        recur regularly given the specified rules. A Recurring Task is
        one that must be completed on a specific regular frequency, such
        as Daily, Weekly, Monthly, or Yearly. To create a Recurring
        Task, you must first create a regular Task with the necessary
        information, then call one of the Create Recurring Task APIs. To
        remove an instance of a Recurring Task, call Delete Recurring
        Task and specify one or more instances of the Recurring Task.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task
        body : DailyRecurringSettingsDto
            The daily recurring settings
        """
        path = f"/api/data/tasks/{taskId}/recurring/daily"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=RecurringTaskChangeSetDetailsChangeSetStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[RecurringTaskChangeSetDetailsChangeSetStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[RecurringTaskChangeSetDetailsChangeSetStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_yearly_recurring_tasks(self, taskId: str, body: YearlyRecurringSettingsDto) -> AstroResult[RecurringTaskChangeSetDetailsChangeSetStatusDto]:
        """
        Changes an existing Task into a Recurring Task, so that it will
        recur regularly given the specified rules. A Recurring Task is
        one that must be completed on a specific regular frequency, such
        as Daily, Weekly, Monthly, or Yearly. To create a Recurring
        Task, you must first create a regular Task with the necessary
        information, then call one of the Create Recurring Task APIs. To
        remove an instance of a Recurring Task, call Delete Recurring
        Task and specify one or more instances of the Recurring Task.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task
        body : YearlyRecurringSettingsDto
            The yearly recurring settings
        """
        path = f"/api/data/tasks/{taskId}/recurring/yearly"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=RecurringTaskChangeSetDetailsChangeSetStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[RecurringTaskChangeSetDetailsChangeSetStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[RecurringTaskChangeSetDetailsChangeSetStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def delete_recurring_tasks(self, taskId: str, option: str) -> AstroResult[ChangeSetStatusDto]:
        """
        Removes one or more instances of a Recurring Task based on the
        `option` you specify: `this` means to remove a single instance,
        `all` means to remove all instances, or `future` means to remove
        all future instances of the Recurring Task. A Recurring Task is
        one that must be completed on a specific regular frequency, such
        as Daily, Weekly, Monthly, or Yearly. To create a Recurring
        Task, you must first create a regular Task with the necessary
        information, then call one of the Create Recurring Task APIs. To
        remove an instance of a Recurring Task, call Delete Recurring
        Task and specify one or more instances of the Recurring Task.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task
        option : str
            Specify `this`, `all`, or `future` to indicate which task
            recurrnces to delete.
        """
        path = f"/api/data/tasks/{taskId}/recurring/{option}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ChangeSetStatusDto, data=json.loads(result.content)['data'])
            return AstroResult[ChangeSetStatusDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ChangeSetStatusDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def validate_recurring_tasks(self, taskId: str, body: RecurringTaskSettingsDto) -> AstroResult[RecurringTaskValidationResultDto]:
        """
        Reviews potential updates to a Recurring Task and report back on
        the list of changes that would occur if this Recurring Task was
        updated with these settings. When making changes to a Recurring
        Task, you may want to investigate the consequences of your
        changes first before finalizing the changes. You can use the
        Validate Recurring Tasks API to examine these changes. When you
        are happy with the changes, call Update Recurring Tasks to
        complete them. A Recurring Task is one that must be completed on
        a specific regular frequency, such as Daily, Weekly, Monthly, or
        Yearly. To create a Recurring Task, you must first create a
        regular Task with the necessary information, then call one of
        the Create Recurring Task APIs. To remove an instance of a
        Recurring Task, call Delete Recurring Task and specify one or
        more instances of the Recurring Task.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task
        body : RecurringTaskSettingsDto
            The new settings
        """
        path = f"/api/data/tasks/{taskId}/recurring/settings/validate"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=RecurringTaskValidationResultDto, data=json.loads(result.content)['data'])
            return AstroResult[RecurringTaskValidationResultDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[RecurringTaskValidationResultDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def update_recurring_tasks(self, taskId: str, body: RecurringTaskSettingsDto) -> AstroResult[RecurringTaskChangeSetDetails]:
        """
        Updates the settings for a Recurring Task and re-generates
        occurrences of the Recurring Task from the new rules. When
        making changes to a Recurring Task, you may want to investigate
        the consequences of your changes first before finalizing the
        changes. You can use the Validate Recurring Tasks API to examine
        these changes. When you are happy with the changes, call Update
        Recurring Tasks to complete them. A Recurring Task is one that
        must be completed on a specific regular frequency, such as
        Daily, Weekly, Monthly, or Yearly. To create a Recurring Task,
        you must first create a regular Task with the necessary
        information, then call one of the Create Recurring Task APIs. To
        remove an instance of a Recurring Task, call Delete Recurring
        Task and specify one or more instances of the Recurring Task.

        Parameters
        ----------
        taskId : str
            The unique identifier of the Task
        body : RecurringTaskSettingsDto
            The new settings
        """
        path = f"/api/data/tasks/{taskId}/recurring/settings"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=RecurringTaskChangeSetDetails, data=json.loads(result.content)['data'])
            return AstroResult[RecurringTaskChangeSetDetails](None, True, False, result.status_code, data)
        else:
            response = AstroResult[RecurringTaskChangeSetDetails](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
