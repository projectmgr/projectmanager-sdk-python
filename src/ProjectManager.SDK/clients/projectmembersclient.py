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

from models.astroresult import AstroResult
from models.projectmemberdto import ProjectMemberDto
from models.projectmemberroledto import ProjectMemberRoleDto
import json

class ProjectMembersClient:
    """
    API methods related to ProjectMembers
    """
    from projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_project_members(self, projectId: str, includeAllUsers: bool) -> AstroResult[list[ProjectMemberDto]]:
        """
        Returns a list of membership options for existing members.
        Optionally include users who are not a member yet.

        Parameters
        ----------
        projectId : str
            Reference to the project
        includeAllUsers : bool
            Set to true to include all users in the workspace
        """
        path = f"/api/data/projects/{projectId}/members"
        result = self.client.send_request("GET", path, None, {"includeAllUsers": includeAllUsers}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(None, True, False, result.status_code, list[ProjectMemberDto](**json.loads(result.content)['data']))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)

    def retrieve_user_project_membership(self, projectId: str, userId: str) -> AstroResult[ProjectMemberDto]:
        """
        Return the membership of a project for a user.

        Parameters
        ----------
        projectId : str
            Reference of Project
        userId : str
            Reference of User
        """
        path = f"/api/data/projects/{projectId}/members/{userId}"
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(None, True, False, result.status_code, ProjectMemberDto(**json.loads(result.content)['data']))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)

    def create_user_project_membership(self, projectId: str, userId: str, body: ProjectMemberRoleDto) -> AstroResult[ProjectMemberDto]:
        """
        Creates a membership for a user in a project and assigns the
        user appropriate permissions

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
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(None, True, False, result.status_code, ProjectMemberDto(**json.loads(result.content)['data']))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)

    def update_user_project_membership(self, projectId: str, userId: str, body: ProjectMemberRoleDto) -> AstroResult[ProjectMemberDto]:
        """
        Update existing Project Access Control for user for project

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
        result = self.client.send_request("PUT", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(None, True, False, result.status_code, ProjectMemberDto(**json.loads(result.content)['data']))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)

    def remove_user_project_membership(self, projectId: str, userId: str) -> AstroResult[object]:
        """
        Deletes Project Member

        Parameters
        ----------
        projectId : str
            Reference to Project
        userId : str
            Reference to User
        """
        path = f"/api/data/projects/{projectId}/members/{userId}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(None, True, False, result.status_code, object(**json.loads(result.content)['data']))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)
