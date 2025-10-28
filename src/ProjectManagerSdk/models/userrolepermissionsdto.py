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


from ProjectManagerSdk.models.userrolepermissiondto import UserRolePermissionDto
from typing import List
import dataclasses

@dataclasses.dataclass
class UserRolePermissionsDto:
    """
    The permissions available to the role
    """

    invitePeople: UserRolePermissionDto | None = None
    """
    Add people to the account
    """

    editAccountPage: UserRolePermissionDto | None = None
    """
    Edit accounts and billing page
    """

    editSecurityPage: UserRolePermissionDto | None = None
    """
    Edit role security settings
    """

    seeHourlyRatesCostsBudgets: UserRolePermissionDto | None = None
    """
    See hourly rates, costs and budgets
    """

    setTeamHolidays: UserRolePermissionDto | None = None
    """
    Set team holidays
    """

    editTagsSkillsTeams: UserRolePermissionDto | None = None
    """
    Create and edit tags, skills and teams
    """

    editTeamTimesheets: UserRolePermissionDto | None = None
    """
    Edit team timesheets
    """

    approveTimesheets: UserRolePermissionDto | None = None
    """
    Approve timesheets
    """

    editImportantProjectInfo: UserRolePermissionDto | None = None
    """
    Manage project portfolio
    """

    seeExportProject: UserRolePermissionDto | None = None
    """
    Ability to export projects
    """

    seeManageUsers: UserRolePermissionDto | None = None
    """
    Access the Manage Users page
    """

    manageIntegrations: UserRolePermissionDto | None = None
    """
    Manage integrations
    """

    createProjectAndProjectGroups: UserRolePermissionDto | None = None
    """
    Create Projects
    """

    editUsers: UserRolePermissionDto | None = None
    """
    Edit user profiles, roles and emails
    """

    viewPersonalBoard: UserRolePermissionDto | None = None
    """
    View personal board
    """

    editAllProjects: UserRolePermissionDto | None = None
    """
    Access all projects and timesheets
    """

    changeOwnEmail: UserRolePermissionDto | None = None
    """
    Edit own email address
    """


