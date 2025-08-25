class My_Random:
    def __init__(self):
        self.seed = None

    def set_seed(self, seed: int):
        """Set the initial seed (must be a 4-digit integer)"""
        seed_str = str(seed).zfill(4)
        self.seed = int(seed_str)

    def dice(self) -> int:
        """Return a random number 1-6 and update the seed"""
        if self.seed is None:
            raise ValueError("Please call set_seed(seed) first to set the initial value")
        
        # (b) Square the seed
        squared = self.seed * self.seed
        
        # (c) Pad with leading zeros to make 8 digits
        squared_str = str(squared).zfill(8)
        
        # (d) Take the middle four digits as new seed
        new_seed = int(squared_str[2:6])
        self.seed = new_seed
        
        # (e) Return dice number (mod 6 + 1)
        return (new_seed % 6) + 1