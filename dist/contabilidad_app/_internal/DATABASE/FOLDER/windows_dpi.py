

def windows_dpi():
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
        windll.shcore.GetScaleFactorForDevice(0)
    except:
        pass
