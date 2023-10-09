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
class WorkSpaceLinksDto:
    """
    TODO - What is this?
    """

    project: str | None = None
    """
    TODO - What is this?
    """

    workSpaceApi: str | None = None
    """
    This is the link to the api for this business, some legacy endpoints
    may need this.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
