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
class ProjectStatusDto:
    """
    A ProjectStatus is a named condition used by your business to
    categorize the completion level of Tasks and Projects within your
    Workspace. You can name your ProjectStatus levels anything you like
    and you can reorganize the order of the ProjectPriority levels at
    any time.
    """

    id: str | None = None
    """
    The unique identifier of this ProjectStatus.
    """

    name: str | None = None
    """
    The name of this ProjectStatus.
    """

    isDeleted: bool | None = None
    """
    Is this a deleted status
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
