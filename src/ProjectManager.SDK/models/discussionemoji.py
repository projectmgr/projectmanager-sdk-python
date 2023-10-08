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
class DiscussionEmoji:
    """
    A reaction to a specific comment within a discussion thread.
    """

    name: str | None = None
    """
    The name of the emoji
    """

    userIds: list[str] | None = None
    """
    The list of user IDs of the users who tagged these emoji
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
