#
# ProjectManager API for Python
#
# (c) 2023-2024 ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  2023-2024 ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#

from ProjectManagerSdk.models.astroresult import AstroResult
from ProjectManagerSdk.models.discussioncommentcreatedto import DiscussionCommentCreateDto
from ProjectManagerSdk.models.discussioncommentcreateresponsedto import DiscussionCommentCreateResponseDto
from ProjectManagerSdk.models.discussioncommentdto import DiscussionCommentDto
import json

class DiscussionClient:
    """
    API methods related to Discussion
    """
    from ProjectManagerSdk.projectmanagerclient import ProjectManagerClient

    def __init__(self, client: ProjectManagerClient):
        self.client = client

    def retrieve_task_comments(self, taskId: str) -> AstroResult[list[DiscussionCommentDto]]:
        """
        Retrieve all comments written about a task

        Parameters
        ----------
        taskId : str
            The unique ID number of the task to retrieve comments
        """
        path = f"/api/data/tasks/{taskId}/comments"
        queryParams = {}
        result = self.client.send_request("GET", path, None, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            data = []
            for dict in json.loads(result.content)['data']:
                data.append(DiscussionCommentDto(**dict))
            return AstroResult[list[DiscussionCommentDto]](None, True, False, result.status_code, data)
        else:
            return AstroResult[list[DiscussionCommentDto]](result.json(), False, True, result.status_code, None)

    def create_task_comments(self, taskId: str, body: DiscussionCommentCreateDto) -> AstroResult[DiscussionCommentCreateResponseDto]:
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
        body : DiscussionCommentCreateDto
            The Markdown-formatted text of the comment
        """
        path = f"/api/data/tasks/{taskId}/comments"
        queryParams = {}
        result = self.client.send_request("POST", path, body, queryParams, None)
        if result.status_code >= 200 and result.status_code < 300:
            return AstroResult[DiscussionCommentCreateResponseDto](None, True, False, result.status_code, DiscussionCommentCreateResponseDto(**json.loads(result.content)['data']))
        else:
            return AstroResult[DiscussionCommentCreateResponseDto](result.json(), False, True, result.status_code, None)
