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
from ProjectManagerSdk.models.projectmemberdto import ProjectMemberDto
from ProjectManagerSdk.models.projectmemberroledto import ProjectMemberRoleDto
import json

class ProjectMembersClient:
    """
    API methods related to ProjectMembers
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_new_project_members(self) -> AstroResult[list[ProjectMemberDto]]:
        """
        Returns a list of users that can be added as members of a new
        project, as well as their available project security roles.

        A project member is a user who has access to a specific project.
        Project members are assigned a project security role, which
        controls the level of access they have to the project. Possible
        project security roles include manage, edit, collaborate,
        creator, and guest.

        Parameters
        ----------
        """
        path = "/api/data/projects/members"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(ProjectMemberDto(**dict))
            return AstroResult[list[ProjectMemberDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[ProjectMemberDto]](result.json(), False, True, result.status_code, None)

    def retrieve_project_members(self, projectId: str, includeAllUsers: bool) -> AstroResult[list[ProjectMemberDto]]:
        """
        Returns a list of users that are currently members of a
        specified project, as well as their current project security
        roles and available project security roles. Optionally include
        users who are not currently members of the project, but who are
        available to be added.

        A project member is a user who has access to a specific project.
        Project members are assigned a project security role, which
        controls the level of access they have to the project. Possible
        project security roles include manage, edit, collaborate,
        creator, and guest.

        Parameters
        ----------
        projectId : str
            Reference to the project
        includeAllUsers : bool
            Set to true to include all users in the workspace
        """
        path = f"/api/data/projects/{projectId}/members"
        queryParams = {}
        if includeAllUsers:
            queryParams['includeAllUsers'] = includeAllUsers
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(ProjectMemberDto(**dict))
            return AstroResult[list[ProjectMemberDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[ProjectMemberDto]](result.json(), False, True, result.status_code, None)

    def retrieve_user_project_membership(self, projectId: str, userId: str) -> AstroResult[ProjectMemberDto]:
        """
        Returns the project security role in a specified project for a
        current project member.

        A project member is a user who has access to a specific project.
        Project members are assigned a project security role, which
        controls the level of access they have to the project. Possible
        project security roles include manage, edit, collaborate,
        creator, and guest.

        Parameters
        ----------
        projectId : str
            Reference of Project
        userId : str
            Reference of User
        """
        path = f"/api/data/projects/{projectId}/members/{userId}"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[ProjectMemberDto](None, True, False, result.status_code, ProjectMemberDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ProjectMemberDto](result.json(), False, True, result.status_code, None)

    def create_user_project_membership(self, projectId: str, userId: str, body: ProjectMemberRoleDto) -> AstroResult[ProjectMemberDto]:
        """
        Creates a membership for a user in a specified project, and
        assigns the user the appropriate project access based on the
        specified project security role.

        A project member is a user who has access to a specific project.
        Project members are assigned a project security role, which
        controls the level of access they have to the project. Possible
        project security roles include manage, edit, collaborate,
        creator, and guest.

        Parameters
        ----------
        projectId : str
            Reference to Project
        userId : str
            Reference to User
        body : ProjectMemberRoleDto
            The permission to set
        """
        path = f"/api/data/projects/{projectId}/members/{userId}"
        queryParams = {}
        result = self.client.send_request("POST", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[ProjectMemberDto](None, True, False, result.status_code, ProjectMemberDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ProjectMemberDto](result.json(), False, True, result.status_code, None)

    def update_user_project_membership(self, projectId: str, userId: str, body: ProjectMemberRoleDto) -> AstroResult[ProjectMemberDto]:
        """
        Updates the project access for a current member of a specified
        project by giving the user a new project security role.

        A project member is a user who has access to a specific project.
        Project members are assigned a project security role, which
        controls the level of access they have to the project. Possible
        project security roles include manage, edit, collaborate,
        creator, and guest.

        Parameters
        ----------
        projectId : str
            Reference to Project
        userId : str
            Reference to User
        body : ProjectMemberRoleDto
            The permission to update
        """
        path = f"/api/data/projects/{projectId}/members/{userId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[ProjectMemberDto](None, True, False, result.status_code, ProjectMemberDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[ProjectMemberDto](result.json(), False, True, result.status_code, None)

    def remove_user_project_membership(self, projectId: str, userId: str) -> AstroResult[object]:
        """
        Removes a current project member from a specified project. This
        removes the user's access to that project.

        A project member is a user who has access to a specific project.
        Project members are assigned a project security role, which
        controls the level of access they have to the project. Possible
        project security roles include manage, edit, collaborate,
        creator, and guest.

        Parameters
        ----------
        projectId : str
            Reference to Project
        userId : str
            Reference to User
        """
        path = f"/api/data/projects/{projectId}/members/{userId}"
        queryParams = {}
        result = self.client.send_request("DELETE", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[object](None, True, False, result.status_code, object(**json.loads(result.content)['data']))
        else:
            return AstroResult[object](result.json(), False, True, result.status_code, None)
