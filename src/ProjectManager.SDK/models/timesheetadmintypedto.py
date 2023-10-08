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
class TimesheetAdminTypeDto:
    """
    Represents admin task to track time
    """

    id: str | None = None
    """
    admin task id
    """

    name: str | None = None
    """
    admin task name
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
