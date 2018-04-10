from i3pystatus.core import Status
from battery import BatteryChecker
from clock import Clock
from load import Load
from network import Network
from extip import ExtIp
from openvpn import OpenVPN
from cpu_usage import CpuUsage
from mem import Mem
from disk import Disk
from pulseaudio import PulseAudio
from backlight import Backlight


def main():
    status = Status()
    status.register(Clock, format="%b/%d/%Y %H:%M:%S")
    #status.register(Load)
    status.register(
        BatteryChecker,
        format=
        "{status}{consumption:.2f}W {percentage:.0f}% {remaining:%E%hh:%Mm}",
        alert=True,
        alert_percentage=10,
        status={
            "DIS": "↓",
            "CHR": "↑",
            "FULL": "=",
        },
    )
    status.register(
        Network,
        interface="eth0",
        format_up="{interface}[{v4cidr}] {network_graph}{kbs}KB/s",
        format_down="",
        dynamic_color=True,
        upper_limit=800.0)
    status.register(
        Network,
        interface="wlan0",
        format_up="{essid}[{v4cidr}] {network_graph}{kbs}KB/s",
        format_down="",
        dynamic_color=True,
        upper_limit=800.0)
    #status.register(ExtIp)
    status.register(OpenVPN, vpn_name="0xdeffbeef")
    status.register(CpuUsage, format="CPU: {usage}%")
    status.register(Mem, format="Mem: {percent_used_mem}%")
    #status.register(Disk, path="/home/", format="{avail}/{total}GiB")
    status.register(PulseAudio)
    status.register(
        Backlight, backlight="intel_backlight", format=u"\u263c {percentage}%")
    status.register("spotify")
    status.run()


if __name__ == '__main__':
    import logging
    import os

    logpath = os.path.join(
        os.path.expanduser("~"), ".i3pystatus-%s" % os.getpid())
    handler = logging.FileHandler(logpath, delay=True)
    logger = logging.getLogger("i3pystatus")
    logger.addHandler(handler)
    logger.setLevel(logging.NOTSET)

    main()
