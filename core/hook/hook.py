

def hook(func):

    def wrapper(self, *args, **kwargs):
        from core.desktop_mascot_controller import DesktopMascotController
        hooks = DesktopMascotController.hooks
        if hooks.get(f"on_{func.__name__}_start"):
            for f in hooks[f"on_{func.__name__}_start"]:
                f(self)
        result = func(self, *args, **kwargs)
        if hooks.get(f"on_{func.__name__}_end"):
            for f in hooks[f"on_{func.__name__}_end"]:
                f(self)
        return result
    return wrapper
