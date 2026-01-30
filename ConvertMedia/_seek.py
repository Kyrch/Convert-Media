import re


# The seek information for our encode
class Seek:
    def __init__(self, input_file: str, ss: str, to: str):
        self.input_file = input_file
        self.ss = ss
        self.to = to

    @staticmethod
    def validate(time: str):
        pattern = re.compile(r"^([0-5]?\d:){1,2}[0-5]?\d(?=\.\d+$|$)|\d+(?=\.\d+$|$)")

        return pattern.match(time)

    # The seek string arguments for our encode
    def get_seek_string(self) -> str:
        # Slow seek for m2ts files
        if self.input_file.endswith(".m2ts"):
            if len(self.ss) > 0 and len(self.to) > 0:
                return f'-i "{self.input_file}" -ss {self.ss} -to {self.to}'
            elif len(self.ss) > 0:
                return f'-i "{self.input_file}" -ss {self.ss}'
        # Fast seek for all other files
        elif len(self.ss) > 0 and len(self.to) > 0:
            return f'-ss {self.ss} -to {self.to} -i "{self.input_file}"'
        elif len(self.ss) > 0:
            return f'-ss {self.ss} -i "{self.input_file}"'
        elif len(self.to) > 0:
            return f'-i "{self.input_file}" -to {self.to}'
        else:
            return f'-i "{self.input_file}"'
