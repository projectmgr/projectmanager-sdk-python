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


from dataclasses import dataclass

@dataclass
class DiscussionCreateDto:
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


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
