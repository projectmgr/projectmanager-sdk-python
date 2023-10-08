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
class TimesheetCreateRequestDto:
    """
    Payload to create time entry
    """

    date: str | None = None
    hours: float | None = None
    taskId: str | None = None
    adminTypeId: str | None = None
    resourceId: str | None = None
    notes: str | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
