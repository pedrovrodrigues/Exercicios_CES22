def search_binary(xs, target):
    """ Find and return the index of key in sequence xs """
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:   # If region of interest (ROI) becomes empty
           return -1

        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2

        # Fetch the item at that position
        item_at_mid = xs[mid_index]

        # print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'"
        #       .format(lb, ub, ub-lb, item_at_mid, target))

        # How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index      # Found it!
        if item_at_mid < target:
            lb = mid_index + 1    # Use upper half of ROI next time
        else:
            ub = mid_index        # Use lower half of ROI next time

def merge_a(list1, list2):
    intersection = []
    for x in list1:
        if search_binary(list2, x) != -1:
            intersection.append(x)
            list2.remove(x)
    return intersection

def merge_b(list1, list2):
    exclusives1 = []
    for x in list1:
        if search_binary(list2, x) == -1:
            exclusives1.append(x)
    return exclusives1

def merge_c(list1, list2):
    exclusives2 = []
    for x in list2:
        if search_binary(list1, x) == -1:
            exclusives2.append(x)
    return exclusives2

def merge_d(list1, list2):
    union = merge_b(list1,list2) + merge_c(list1,list2) + merge_a(list1,list2)
    return union

def merge_e(list1, list2):
    inter = merge_a(list1,list2)
    bagdiff = list1
    for x in inter:
        bagdiff.remove(x)
    return bagdiff