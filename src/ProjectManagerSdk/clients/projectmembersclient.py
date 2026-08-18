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
from ProjectManagerSdk.models.projectaccessdto import ProjectAccessDto
from ProjectManagerSdk.models.projectmemberdto import ProjectMemberDto
from ProjectManagerSdk.models.projectmemberroledto import ProjectMemberRoleDto
from typing import List
from ProjectManagerSdk.tools import remove_empty_elements
import dataclasses
import json
import dacite

class ProjectMembersClient:
    """
    API methods related to ProjectMembers
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_new_project_members(self) -> AstroResult[List[ProjectMemberDto]]:
        """
        Returns a list of users that can be added as members of a new
        project, as well as their available project security roles. A
        project member is a user who has access to a specific project.
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
                data.append(dacite.from_dict(data_class=ProjectMemberDto, data=dict))
            return AstroResult[List[ProjectMemberDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[ProjectMemberDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def retrieve_projects_the_user_is_a_member_of(self) -> AstroResult[List[ProjectAccessDto]]:
        """
        Returns a list of project permissions the user is a member of

        Parameters
        ----------
        """
        path = "/api/data/projects/membership"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(dacite.from_dict(data_class=ProjectAccessDto, data=dict))
            return AstroResult[List[ProjectAccessDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[ProjectAccessDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def retrieve_project_members(self, projectId: str, includeAllUsers: bool) -> AstroResult[List[ProjectMemberDto]]:
        """
        Returns a list of users that are currently members of a
        specified project, as well as their current project security
        roles and available project security roles. Optionally include
        users who are not currently members of the project, but who can
        be added. A project member is a user who has access to a
        specific project. Project members are assigned a project
        security role, which controls the level of access they have to
        the project. Possible project security roles include manage,
        edit, collaborate, creator, and guest.

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
                data.append(dacite.from_dict(data_class=ProjectMemberDto, data=dict))
            return AstroResult[List[ProjectMemberDto]](None, True, False, result.status_code, data)
        else:
            response = AstroResult[List[ProjectMemberDto]](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def retrieve_user_project_membership(self, projectId: str, userId: str) -> AstroResult[ProjectMemberDto]:
        """
        Returns the project security role in a specified project for a
        current project member. A project member is a user who has
        access to a specific project. Project members are assigned a
        project security role, which controls the level of access they
        have to the project. Possible project security roles include
        manage, edit, collaborate, creator, and guest.

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
            data = dacite.from_dict(data_class=ProjectMemberDto, data=json.loads(result.content)['data'])
            return AstroResult[ProjectMemberDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ProjectMemberDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def create_or_update_user_project_membership(self, projectId: str, userId: str, body: ProjectMemberRoleDto) -> AstroResult[ProjectMemberDto]:
        """
        Creates or updates (upserts) a user's membership in a specified
        project. If the user is not yet a member they are added; if they
        are already a member their project security role is replaced.
        The role is optional. When the role is omitted for a new member,
        a default role is applied based on the user's workspace access:
        users who can edit all projects become a Manager, guest users
        become a Guest, and everyone else becomes an Editor. When the
        role is omitted for a user who is already a member, their
        current role is left unchanged. A project member is a user who
        has access to a specific project. Project members are assigned a
        project security role, which controls the level of access they
        have to the project. Possible project security roles include
        manage, edit, collaborate, creator, and guest.

        Parameters
        ----------
        projectId : str
            Reference to Project
        userId : str
            Reference to User
        body : ProjectMemberRoleDto
            The permission to set. The role is optional.
        """
        path = f"/api/data/projects/{projectId}/members/{userId}"
        queryParams = {}
        result = self.client.send_request("PUT", path, remove_empty_elements(dataclasses.asdict(body)), queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = dacite.from_dict(data_class=ProjectMemberDto, data=json.loads(result.content)['data'])
            return AstroResult[ProjectMemberDto](None, True, False, result.status_code, data)
        else:
            response = AstroResult[ProjectMemberDto](None, False, True, result.status_code, None)
            response.load_error(result)
            return response

    def remove_user_project_membership(self, projectId: str, userId: str) -> AstroResult[object]:
        """
        Removes a current project member from a specified project. This
        removes the user's access to that project. A project member is a
        user who has access to a specific project. Project members are
        assigned a project security role, which controls the level of
        access they have to the project. Possible project security roles
        include manage, edit, collaborate, creator, and guest.

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
            data = dacite.from_dict(data_class=object, data=json.loads(result.content)['data'])
            return AstroResult[object](None, True, False, result.status_code, data)
        else:
            response = AstroResult[object](None, False, True, result.status_code, None)
            response.load_error(result)
            return response
