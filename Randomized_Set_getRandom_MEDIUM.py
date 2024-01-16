# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity

class RandomizedSet(object):

    def __init__(self):
        self.set_dict = {}
        self.set_list = []
        
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.set_dict.keys():
            return False
        else:
            self.set_dict[val] = len(self.set_list)
            self.set_list.append(val)
            return True  
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.set_dict:
            return False
        current_last_item_list = self.set_list[-1]
        index_of_ele_to_pop = self.set_dict[val]     

        self.set_dict[current_last_item_list] = index_of_ele_to_pop
        self.set_list[index_of_ele_to_pop] = current_last_item_list

        self.set_list[-1] = val
        self.set_list.pop()
        self.set_dict.pop(val)
        return True
        
    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.set_list)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()



#To keep in mind the thing is since for insert and delete we can simply maintain a dictionary since it uses hashmap by searching for keys and values
#but for finding the random value we cannot use set or dicionary since they are not indexed, so we maintain a list on the side as we remove and insert elements'
#so as to save ourselves from converting a dictionary at the end to a list, and randomize the list for getRandom()
