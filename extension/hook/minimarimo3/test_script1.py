

class Extension:

    @staticmethod
    def on_read_start(self):
        # print("on_read_start")
        return "OK!"

    @staticmethod
    def on_read_end(self):
        # print("on_read_end")
        return "OK!"

    @staticmethod
    def on_write_start(self):
        # print("on_write_start")
        return "OK!"

    @staticmethod
    def on_write_end(self):
        # print("on_write_end")
        return "OK!"
