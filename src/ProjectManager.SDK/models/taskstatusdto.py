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
class TaskStatusDto:
    """
    A TaskStatus is a named status level used by your business to
    determine how to measure the progress of Tasks. You can define your
    own named status levels that are appropriate for your business and
    determine which status levels are considered done.
    """

    id: str | None = None
    projectId: str | None = None
    name: str | None = None
    order: int | None = None
    isDone: bool | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
