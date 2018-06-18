import tables as tb

class RunInfo(tb.IsDescription):
    run_number = tb.UInt64Col(pos=0)
    t_min      = tb.UInt64Col(pos=1)
    t_max      = tb.UInt64Col(pos=2)

class MapInfo(tb.IsDescription):
    x_nbins = tb. UInt64Col(pos=0)
    y_nbins = tb. UInt64Col(pos=1)
    x_pitch = tb.Float64Col(pos=2)
    y_pitch = tb.Float64Col(pos=3)
    x_min   = tb.Float64Col(pos=4)
    x_max   = tb.Float64Col(pos=5)
    y_min   = tb.Float64Col(pos=6)
    y_max   = tb.Float64Col(pos=7)