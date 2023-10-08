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
class NameDto:
    """
    When uploading a list of names to an API, this data structure
    represents an individual name within the list.
    """

    name: str | None = None
    """
    A name. To determine the meaning of this name, see the field to
    which this value is attached in the parent object.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
