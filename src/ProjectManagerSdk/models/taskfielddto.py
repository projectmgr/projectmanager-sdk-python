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
class TaskFieldDto:
    """
    A model that contains the value for a TaskField.
    """

    shortId: str | None = None
    """
    The unique Short Id of this TaskField.
    """

    value: str | None = None
    """
    The value currently set for this TaskField for this Task.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
