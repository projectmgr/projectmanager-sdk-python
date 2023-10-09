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
class AstroError:
    """
    Information about an error that occurred within the ProjectManager
    API.
    """

    technicalError: str | None = None
    """
    A technical description of the error that occurred. Not suitable for
    display to end users.
    """

    additionalErrors: list[str] | None = None
    """
    If additional errors beyond the main error in `Message` occurred,
    they will be listed here as individual messages.
    """

    message: str | None = None
    """
    A description of the error that occurred. If your application has a
    user interface, show this message to explain what went wrong.
    """


    def to_dict(self) -> dict:
        return dataclass.asdict(self)
