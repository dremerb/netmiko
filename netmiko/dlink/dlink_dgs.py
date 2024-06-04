from typing import Any

from netmiko.dlink.dlink_ds import DlinkDSBase


class DlinkDGSBase(DlinkDSBase):
    def session_preparation(self) -> None:
        """Prepare the session after the connection has been established."""
        self.ansi_escape_codes = True
        self._test_channel_read(pattern=r"#")
        self.set_base_prompt()
        self.disable_paging(command="disable clipaging", cmd_verify=False)


class DlinkDGSSSH(DlinkDGSBase):
    pass


class DlinkDGSTelnet(DlinkDGSBase):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        default_enter = kwargs.get("default_enter")
        kwargs["default_enter"] = "\r\n" if default_enter is None else default_enter
        super().__init__(*args, **kwargs)