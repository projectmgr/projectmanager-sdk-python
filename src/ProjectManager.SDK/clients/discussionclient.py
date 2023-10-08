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
from models.discussioncreatedto import DiscussionCreateDto
from models.discussioncreateresponsedto import DiscussionCreateResponseDto
from models.discussiondto import DiscussionDto

class DiscussionClient:
    """
    API methods related to Discussion
    """
    from projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_task_comments(self, taskId: str) -> AstroResult[list[DiscussionDto]]:
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
            return AstroResult(None, True, False, result.status_code, list[DiscussionDto](result.json(), list[DiscussionDto]))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)

    def create_task_comments(self, taskId: str, body: DiscussionCreateDto) -> AstroResult[DiscussionCreateResponseDto]:
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
            return AstroResult(None, True, False, result.status_code, DiscussionCreateResponseDto(result.json(), DiscussionCreateResponseDto))
        else:
            return AstroResult(result.json(), False, True, result.status_code, None)
