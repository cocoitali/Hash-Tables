

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * capacity

# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for character in string:
        hash = ((hash << 5) + hash) + ord(character)
    return hash % max

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    
    current_pair = hash_table.storage[index]

    last_pair = None
    while current_pair is not None and current_pair.key != key: #if none, means we did not find a collision
        last_pair = current_pair
        current_pair = current_pair.next

    if current_pair is None:
        new_pair = Pair(key, value)
        new_pair.next = hash_table.storage[index]
        hash_table.storage[index]= new_pair


    if hash_table.storage[index] is not None:
        print("Warning: overwriting " + str(hash_table.elements[index].key))
    hash_table.storage[index] = pair

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)

    if hash_table.storage[index] is None:
        print ("Warnign: removing non-existent key" + key)
    has_table.storage[index] = None
    
# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)

    if hash_table.storage[index] is None:
        print ("Warning: no value found for key " + key)
        return None
    return hash_table.storage[index]

def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "a", "VALUE FOR A")
    hash_table_insert(ht, "q", "VALUE FOR Q")
    print(hash_table_retrieve(ht, "a"))

    hash_table_insert(ht, "line", "Here today...\n")
    print(ht.elements)
    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")



