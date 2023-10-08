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

from ProjectManager.SDK.astro_result import AstroResult
from ProjectManager.SDK.models.errorresult import ErrorResult
from ProjectManager.SDK.astroresult import AstroResult
from ProjectManager.SDK.models.discussioncreatedto import DiscussionCreateDto
from ProjectManager.SDK.models.discussioncreateresponsedto import DiscussionCreateResponseDto
from ProjectManager.SDK.models.discussiondtolist import DiscussionDtoList

class DiscussionClient:
    """
    API methods related to Discussion
    """
    from ProjectManager.SDK.project_manager_client import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_task_comments(self, taskId: str) -> AstroResult[AstroResult[DiscussionDtoList]]:
        """
        Retrieve all comments written about a task

        Parameters
        ----------
        taskId : str
            The unique ID number of the task to retrieve comments
        """
        path = f"/api/data/tasks/{taskId}/discussions"
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), DiscussionDtoList), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_task_comments(self, taskId: str, body: DiscussionCreateDto) -> AstroResult[AstroResult[DiscussionCreateResponseDto]]:
        """
        Adds a Markdown-formatted comment to a task.

        Tasks can have discussions attached to them. These discussions
        can include text with simple formatting. Discussion comments are
        formatted using [Markdown](https://www.markdownguide.org/) and
        users should be aware that HTML embedding is not permitted due
        to the risk of cross-site attacks and other embedding
        challenges.

        Parameters
        ----------
        taskId : str
            The unique ID number of the task being commented upon
        body : DiscussionCreateDto
            The Markdown-formatted text of the comment
        """
        path = f"/api/data/tasks/{taskId}/discussions"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult(True, result.status_code, AstroResult.from_json(result.json(), DiscussionCreateResponseDto), None)
        else:
            return AstroResult(False, result.status_code, None, ErrorResult.from_json(result.json()))
