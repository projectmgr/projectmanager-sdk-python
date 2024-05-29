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


from ProjectManagerSdk.models.discussioncommentfiledto import DiscussionCommentFileDto
from ProjectManagerSdk.models.discussionemoji import DiscussionEmoji
from typing import List
import dataclasses

@dataclasses.dataclass
class DiscussionCommentDto:
    """
    Tasks can have discussions attached to them. These discussions can
    include text with simple formatting. Discussion comments are
    formatted using [Markdown](https://www.markdownguide.org/) and users
    should be aware that HTML embedding is not permitted due to the risk
    of cross-site attacks and other embedding challenges.
    """

    id: str | None = None
    """
    The unique ID of the discussion comment.
    """

    discussionCommentId: str | None = None
    """
    Obsolete - use Id instead
    """

    text: str | None = None
    """
    The text of the comment to add to the discussion, in Markdown
    format. Discussion comments are formatted using
    [Markdown](https://www.markdownguide.org/) and users should be aware
    that HTML embedding is not permitted due to the risk of cross-site
    attacks and other embedding challenges.
    """

    authorId: str | None = None
    """
    The unique ID of the resource that wrote this comment.
    """

    authorName: str | None = None
    """
    The unique ID of the resource that wrote this comment.
    """

    createDate: str | None = None
    """
    The timestamp when the comment was created.
    """

    modifyDate: str | None = None
    """
    The timestamp when the comment was modified, if it is different from
    the create date.
    """

    emoji: List[DiscussionEmoji] | None = None
    """
    The list of emoji reactions to this discussion comment, if any. This
    object will be null if no emoji reactions have been recorded on this
    discussion comment.
    """

    files: List[DiscussionCommentFileDto] | None = None
    """
    The list of files associated with this Comment, if any. This field
    will be present when you fetch a single object. When you query for
    multiple objects, this field is not included in results by default.
    To expand this field, specify the name of this field in the
    `$expand` parameter.
    """


