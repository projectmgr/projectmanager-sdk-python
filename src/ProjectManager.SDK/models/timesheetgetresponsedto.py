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
class TimesheetGetResponseDto:
    """
    Created Time entry response data
    """

    id: str | None = None
    date: str | None = None
    notes: str | None = None
    approved: bool | None = None
    hours: float | None = None
    task: TimesheetTaskDto | None = None
    project: TimeSheetProjectDto | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
