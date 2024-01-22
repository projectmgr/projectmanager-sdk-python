#
# ProjectManager API for Python
#
# (c) 2023-2024 ProjectManager.com, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     ProjectManager.com <support@projectmanager.com>
# @copyright  2023-2024 ProjectManager.com, Inc.
# @link       https://github.com/projectmgr/projectmanager-sdk-python
#


from dataclasses import dataclass

@dataclass
class ProjectFileTaskDto:

    id: str | None = None
    """
    The unique identifier of this Task.
    """

    shortId: str | None = None
    """
    A short ID that can be used to refer to this Task. This short ID is
    guaranteed to be unique within your Workspace.
    """

    name: str | None = None
    """
    The common name of this Task.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
