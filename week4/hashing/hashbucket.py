class HashBucket:
    def __init__(self, size, buckets) -> None:
        self.table = [["F"] * (size // buckets) for _ in range(buckets)]
        self.buckets = buckets
        self.overflow = [None] * size
        return

    # insert data into the hash table
    def insert(self, data):
        bucket = self.hash(data)
        if data not in self.table[bucket]:
            if "T" in self.table[bucket]:
                self.table[bucket][self.table[bucket].index("T")] = data
                return
            elif "F" in self.table[bucket]:
                self.table[bucket][self.table[bucket].index("F")] = data
                return
            else:
                # Handle overflow
                for i in range(len(self.overflow)):
                    if self.overflow[i] is None:
                        self.overflow[i] = data
                        return
        return
    
    # delete data from the hash table
    def delete(self, data):
        bucket = self.hash(data)
        if data in self.table[bucket]:
            self.table[bucket][self.table[bucket].index(data)] = "T"
        elif data in self.overflow:
            self.overflow[self.overflow.index(data)] = None
        return
    
    # print content of the hash table
    def print(self):
        for bucket in self.table:
            for i in bucket:
                print(i, end=" ")
        for i in self.overflow:
            if i is not None:
                print(i, end=" ")
        print()
        return

    def hash(self, data):
        sum = 0
        for i in range(len(data)):
            sum += ord(data[i])
        return sum % self.buckets



if __name__ == "__main__":
    table = HashBucket(8, 4)
    table.print()

    table.insert("apple")
    table.insert("orange")
    table.insert("banana")
    table.insert("grapes")
    table.insert("mango")
    table.insert("peach")
    table.insert("apple")
    table.print()

    table.delete("banana")
    table.delete("kiwi")
    table.delete("peach")
    table.print()