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


from ProjectManagerSdk.models.taskfieldvaluetaskdto import TaskFieldValueTaskDto
from dataclasses import dataclass

@dataclass
class TaskFieldValueDto:
    """
    A model that contains the value for a TaskField.
    """

    id: str | None = None
    """
    The unique identifier of this TaskField.
    """

    shortId: str | None = None
    """
    The unique Short Id of this TaskField.
    """

    value: str | None = None
    """
    The value currently set for this TaskFieldValue.
    """

    createdDate: str | None = None
    """
    Date and time (in UTC) that this TaskField was created.
    """

    modifiedDate: str | None = None
    """
    Date and time (in UTC) that this TaskField was last modified.
    """

    task: TaskFieldValueTaskDto | None = None
    """
    The Task to which this Value belongs.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
