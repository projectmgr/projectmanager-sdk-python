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

    id: object | None = None
    date: object | None = None
    notes: object | None = None
    approved: object | None = None
    hours: object | None = None
    task: object | None = None
    project: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
