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
from ProjectManagerSdk.models.recurringtaskchangesetdetailschangesetstatusdto import RecurringTaskChangeSetDetailsChangeSetStatusDto
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
        Create Weekly Recurring Tasks

        Parameters
        ----------
        taskId : str
            The unique identifier or short ID of the Task
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
        Create Monthly Recurring Tasks

        Parameters
        ----------
        taskId : str
            The unique identifier or short ID of the Task
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
        Create Daily Recurring Tasks

        Parameters
        ----------
        taskId : str
            The unique identifier or short ID of the Task
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
        Create Yearly Recurring Tasks

        Parameters
        ----------
        taskId : str
            The unique identifier or short ID of the Task
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
        Delete Recurring Tasks

        Parameters
        ----------
        taskId : str
            The unique identifier or short ID of the Task
        option : str
            The options for the deletion
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
