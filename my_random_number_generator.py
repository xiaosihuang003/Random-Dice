import time

class My_Random:
    def __init__(self):
        self.seed = None

    def set_seed(self, seed=None):
        """Set the initial seed. If None, use last 4 digits of current time in milliseconds."""
        if seed is None:
            self.seed = int(str(int(time.time() * 1000))[-4:])
        else:
            self.seed = int(seed)

    def dice(self):
        """Generate a dice number 1..6 using the middle-square method."""
        # 1) square the seed
        num = self.seed * self.seed
        # 2) pad to 8 digits with leading zeros
        s = str(num).zfill(8)
        # 3) take the middle four digits as the new seed
        mid = len(s) // 2
        self.seed = int(s[mid - 2: mid + 2])
        # 4) map to 1..6
        return self.seed % 6 + 1
