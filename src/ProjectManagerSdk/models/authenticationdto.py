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
class AuthenticationDto:
    """
    Set the connection status of an integration
    """

    connected: bool | None = None
    """
    Set to true if the connection was successful. False is not supported
    right now.
    """

    authScheme: object | None = None
    """
    Authenication scheme
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
