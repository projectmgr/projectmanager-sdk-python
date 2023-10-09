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
class TaskTagDto:
    """
    A TaskTag is a connection between a Task and a Tag. Each Task can
    have zero, one or many TaskTags associated with it. TaskTags can be
    assigned and removed from the Task to help you classify your Tasks
    and prioritize work.
    """

    id: str | None = None
    """
    The unique identifier of this TaskTag.
    """

    name: str | None = None
    """
    The common name of this TaskTag.
    """

    color: str | None = None
    """
    The color that will be used to represent this Tag visually. This
    color is automatically chosen by the application when a user creates
    a Tag. You can choose specify any color that can be represented
    using HTML RGB syntax such as `#0088FF`, in the format `RRGGBB`. You
    may not use names for colors.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
