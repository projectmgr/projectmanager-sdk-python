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


from typing import List
import dataclasses

@dataclasses.dataclass
class WorkSpacePermissionsDto:
    """
    Information about a currently logged in user. You can call the
    RetrieveMe API to gather information about the current user.
    """

    inviteUser: bool | None = None
    """
    True if this user can Add people to the account
    """

    editAccount: bool | None = None
    """
    True if this user can Edit the accounts and billing page
    """

    editRole: bool | None = None
    """
    True if this user can Edit role security settings
    """

    editAllProjects: bool | None = None
    """
    True if this user can Access all account data
    """

    editCost: bool | None = None
    """
    True if this user can See hourly rates, costs and budgets
    """

    editHoliday: bool | None = None
    """
    True if this user can Set team holidays
    """

    editUserField: bool | None = None
    """
    True if this user can Create and edit tags, skills, and teams
    """

    editAllTimesheets: bool | None = None
    """
    True if this user can Edit team timesheets
    """

    approveTimesheet: bool | None = None
    """
    True if this user can Approve timesheets
    """

    setUpBoardWorkflow: bool | None = None
    """
    True if this user can Set up board workflow
    """

    editProjectField: bool | None = None
    """
    True if this user can Edit project and portfolio settings
    """

    exportProject: bool | None = None
    """
    True if this user can Export projects
    """

    viewUser: bool | None = None
    """
    True if this user can Access the Manage Users page
    """

    editIntegration: bool | None = None
    """
    True if this user can Manage Integrations
    """

    createProject: bool | None = None
    """
    True if this user Can create projects and groups
    """

    editUser: bool | None = None
    """
    True if this user can Edit user profiles, roles and emails
    """

    viewMyBoard: bool | None = None
    """
    True if this user can View personal board
    """


