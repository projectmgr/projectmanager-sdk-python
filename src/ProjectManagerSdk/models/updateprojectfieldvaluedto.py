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
class UpdateProjectFieldValueDto:
    """
    A model that contains a new value to be set for a ProjectField.
    """

    value: str | None = None
    """
    The new value to be set for this ProjectField.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
