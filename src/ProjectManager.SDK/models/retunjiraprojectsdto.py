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
class RetunJiraProjectsDto:
    """
    The Jira API is intended for use by ProjectManager and its business
    development partners. Please contact ProjectManager's sales team to
    request use of this API.
    """

    id: str | None = None
    """
    The unique identifier of the Jira Project
    """

    name: str | None = None
    """
    The name of jira project
    """

    key: str | None = None
    """
    The key of Jira Project
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
