class HashLinear:
    def __init__(self, size):
        self.table = ["F"] * size

    # insert data into the hash table
    def insert(self, data):
        slot = self.hash(data, len(self.table))
        limit = len(self.table)
        while self.table[slot] != "F" and limit > 0:
            if self.table[slot] == data:
                return
            if self.table[slot] == "T":
                self.table[slot] = data
                return
            slot = (slot + 1) % len(self.table)
            limit -= 1
        if self.table[slot] == "F":
            self.table[slot] = data
        return
    
    # delete data from the hash table
    def delete(self, data):
        slot = self.hash(data, len(self.table))
        limit = len(self.table)
        while self.table[slot] != "F" and limit > 0:
            if self.table[slot] == data:
                self.table[slot] = "T"
                return
            slot = (slot + 1) % len(self.table)
            limit -= 1
        return

    # print content of the hash table
    def print(self):
        for i in range(len(self.table)):
            print(self.table[i], end=" ")
        print()
        return

    def hash(self, data, length):
        sum = 0
        for i in range(len(data)):
            sum += ord(data[i])
        return sum % length


if __name__ == "__main__":
    table = HashLinear(8)
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