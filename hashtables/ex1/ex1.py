#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    for i,j in enumerate(weights):
        hash_table_insert(ht,j,i)
    
    for i,j in enumerate(weights):
        diff = limit - i
        if hash_table_retrieve(ht,diff) is not None:
            diff_index = hash_table_retrieve(ht,diff)

            if diff_index >= i:
                return [diff_index,i]
            else:
                return [i,diff_index]

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
