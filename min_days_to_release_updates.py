# Get Minimum Days:

### A programming challenge where you need to determine the minimum number of days required to release updates. The challenge involves two arrays:

### plannedDate[]: An array representing the planned release dates for updates.
### alternateDate[]: An array representing alternative release dates if the planned ones cannot be met.
### The task is to find the minimum days required to release all updates, where updates must be released in the order specified by the plannedDate[] array. 
### If a planned date cannot be met, the alternative date should be used.

### The updates must be launched in the order defined by the planned dates. For each update, you can choose between its planned date and alternate date, but the order must be maintained, meaning you cannot release an update before releasing the previous ones.

### Therefore, when deciding the release date for each update, the chosen date must be on or after the day of the previous update.

######################################################
### SOLUTION
######################################################

def getMinDays(plannedDate, alternateDate):
    n = len(plannedDate)
    current_day = 0  # Initialize the current day

    # Process each update in the order of planned dates
    for i in range(n):
        # Choose the earlier of the planned or alternate date
        earliest_possible_day = min(plannedDate[i], alternateDate[i]) 
        print(plannedDate[i], alternateDate[i], earliest_possible_day)
        # Ensuring that the update happens after the last one (current_day + 1 ensures it's the next valid day)
        current_day = max(current_day + 1, earliest_possible_day)
        print(current_day, earliest_possible_day)
        # However, if the next update's planned date is further in the future, we must wait for that day
        print(current_day, plannedDate[i])
        current_day = max(current_day, plannedDate[i])
        print(current_day)
        print("-------")
    return current_day

# Example usage
plannedDate = [3, 7, 4, 9]
alternateDate = [1, 5, 2, 3]

result = getMinDays(plannedDate, alternateDate)
print(result)  # Output should be 9


