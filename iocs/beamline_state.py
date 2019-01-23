#!/usr/bin/env python3
from caproto.server import pvproperty, PVGroup, ioc_arg_parser, run
import caproto as ca


class SimpleIOC(PVGroup):
    "An IOC with two simple read/writable PVs"
    scan_id = pvproperty(value=1, mock_record='ai')
    bluesky_baton = pvproperty(value=[""], dtype=ca.ChannelType.STRING)


if __name__ == '__main__':
    ioc_options, run_options = ioc_arg_parser(
        default_prefix='XF31ID:',
        desc="Beamline state for use by bluesky")
    ioc = SimpleIOC(**ioc_options)
    run(ioc.pvdb, **run_options)
