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
from ProjectManagerSdk.models.monthlyrecurringsettingsdto import MonthlyRecurringSettingsDto
from ProjectManagerSdk.models.recurringtaskchangesetdetails import RecurringTaskChangeSetDetails
from ProjectManagerSdk.models.weeklyrecurringsettingsdto import WeeklyRecurringSettingsDto
from ProjectManagerSdk.models.yearlyrecurringsettingsdto import YearlyRecurringSettingsDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class NptRecurrencyClient:
    """
    API methods related to NptRecurrency
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def create_weekly_recurring_npts(self, taskId: str, body: WeeklyRecurringSettingsDto) -> AstroResult[RecurringTaskChangeSetDetails]:
        """
        Create Weekly Recurring Npts

        Parameters
        ----------
        taskId : str
            The unique identifier or short ID of the Npt Tasks
        body : WeeklyRecurringSettingsDto
            The weekly recurring settings
        """
        path = f"/api/data/npt/{taskId}/recurring/weekly"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=RecurringTaskChangeSetDetails, data=json.loads(result.content)['data'])
            return AstroResult[RecurringTaskChangeSetDetails](None, True, False, result.status_code, data)
        else:
            response = AstroResult[RecurringTaskChangeSetDetails](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_monthly_recurring_npts(self, taskId: str, body: MonthlyRecurringSettingsDto) -> AstroResult[RecurringTaskChangeSetDetails]:
        """
        Create Monthly Recurring Npts

        Parameters
        ----------
        taskId : str
            The unique identifier or short ID of the Npt Tasks
        body : MonthlyRecurringSettingsDto
            The monthly recurring settings
        """
        path = f"/api/data/npt/{taskId}/recurring/monthly"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=RecurringTaskChangeSetDetails, data=json.loads(result.content)['data'])
            return AstroResult[RecurringTaskChangeSetDetails](None, True, False, result.status_code, data)
        else:
            response = AstroResult[RecurringTaskChangeSetDetails](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_daily_recurring_npts(self, taskId: str, body: DailyRecurringSettingsDto) -> AstroResult[RecurringTaskChangeSetDetails]:
        """
        Create Daily Recurring Npts

        Parameters
        ----------
        taskId : str
            The unique identifier or short ID of the Npt Tasks
        body : DailyRecurringSettingsDto
            The daily recurring settings
        """
        path = f"/api/data/npt/{taskId}/recurring/daily"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=RecurringTaskChangeSetDetails, data=json.loads(result.content)['data'])
            return AstroResult[RecurringTaskChangeSetDetails](None, True, False, result.status_code, data)
        else:
            response = AstroResult[RecurringTaskChangeSetDetails](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_yearly_recurring_npts(self, taskId: str, body: YearlyRecurringSettingsDto) -> AstroResult[RecurringTaskChangeSetDetails]:
        """
        Create Yearly Recurring Npts

        Parameters
        ----------
        taskId : str
            The unique identifier or short ID of the Npt Tasks
        body : YearlyRecurringSettingsDto
            The yearly recurring settings
        """
        path = f"/api/data/npt/{taskId}/recurring/yearly"
        queryParams = {}
        result = self.client.send_request("POST", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=RecurringTaskChangeSetDetails, data=json.loads(result.content)['data'])
            return AstroResult[RecurringTaskChangeSetDetails](None, True, False, result.status_code, data)
        else:
            response = AstroResult[RecurringTaskChangeSetDetails](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def delete_recurring_npts(self, taskId: str, option: str) -> AstroResult[DeletedTasksDto]:
        """
        Delete Recurring Npts

        Parameters
        ----------
        taskId : str
            The unique identifier or short ID of the Npt Tasks
        option : str
            The options for the deletion
        """
        path = f"/api/data/npt/{taskId}/recurring/{option}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=DeletedTasksDto, data=json.loads(result.content)['data'])
            return AstroResult[DeletedTasksDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[DeletedTasksDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
