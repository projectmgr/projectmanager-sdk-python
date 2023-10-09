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


from ProjectManagerSdk.models.discussionemoji import DiscussionEmoji
from dataclasses import dataclass

@dataclass
class DiscussionDto:
    """
    Tasks can have discussions attached to them. These discussions can
    include text with simple formatting. Discussion comments are
    formatted using [Markdown](https://www.markdownguide.org/) and users
    should be aware that HTML embedding is not permitted due to the risk
    of cross-site attacks and other embedding challenges.
    """

    text: str | None = None
    """
    The text of the comment to add to the discussion, in Markdown
    format. Discussion comments are formatted using
    [Markdown](https://www.markdownguide.org/) and users should be aware
    that HTML embedding is not permitted due to the risk of cross-site
    attacks and other embedding challenges.
    """

    discussionCommentId: str | None = None
    """
    The unique ID of the discussion comment.
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

    emoji: list[DiscussionEmoji] | None = None
    """
    The list of emoji reactions to this discussion comment, if any. This
    object will be null if no emoji reactions have been recorded on this
    discussion comment.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
