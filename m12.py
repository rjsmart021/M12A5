from flask import Flask

# Video Search Application with Binary Search

videos = [
    {'id': 1, 'title': 'The Art of Coding', 'duration': 32},
    {'id': 2, 'title': 'Exploring the Cosmos', 'duration': 44},
    {'id': 3, 'title': 'Cooking Masterclass: Italian Cuisine', 'duration': 76},
    {'id': 4, 'title': 'History Uncovered: Ancient Civilizations', 'duration': 77},
    {'id': 5, 'title': 'Fitness Fundamentals: Strength Training', 'duration': 59},
    {'id': 6, 'title': 'Digital Photography Essentials', 'duration': 45},
    {'id': 7, 'title': 'Financial Planning for Beginners', 'duration': 40},
    {'id': 8, 'title': "Nature's Wonders: National Geographic", 'duration': 45},
    {'id': 9, 'title': 'Artificial Intelligence Revolution', 'duration': 87},
    {'id': 10, 'title': 'Travel Diaries: Discovering Europe', 'duration': 78}
]

# Task 1 - Implement the binary search algorithm for searching videos by title.
# To run a binary search for video titles, we will first have to make sure they're sorted:

# I initially used a bubble sort to order the videos by title; then I saw the next task requires a merge sort!
# # bubble sort video (by any category; default is set to title)
# def sort_videos(lst, type="title"):
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(lst)-1):
#             if lst[i][type] > lst[i+1][type]:
#                 lst[i], lst[i+1] = lst[i+1], lst[i]
#                 swapped = True
#     return lst

# MERGE sort video (by any category; default is set to title)
def merge_sort_videos(lst, type="title"):
    # divide list in half
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        # recursively break down lists for sorting
        merge_sort_videos(left_half)
        merge_sort_videos(right_half)
        
        # index pointers for each list (left, right, main)
        l, r, m = 0, 0, 0
        # compare values within each list and return to main in sorted order
        while l < len(left_half) and r < len(right_half):
            if left_half[l][type] < right_half[r][type]:
                lst[m] = left_half[l]
                l += 1
            else:
                lst[m] = right_half[r]
                r += 1
            m += 1
        # when one of the halves finishes, thre other fills in the rest of main in order
        while l < len(left_half):
            lst[m] = left_half[l]
            l += 1
            m += 1
        while r < len(right_half):
            lst[m] = right_half[r]
            r += 1
            m += 1

        return lst

# # testing for sorted video list
# sort_videos(videos)
merge_sort_videos(videos)
for i in range(len(videos)):
    print(videos[i])

# binary search for video by title
def search_for_video(video_list, search_term):
    # set pointers at both sides of list
    low = 0
    high = len(video_list) - 1
    while low <= high:
        # set midpoint that will be compared to target value
        mid = (low + high) // 2
        if search_term == video_list[mid]["title"]:
            print(f"{search_term} was found at index {mid}")
            return video_list[mid]
        # if search_term is alphabetically higher than midpoint, move up low pointer
        elif search_term > video_list[mid]["title"]:
            low = mid + 1
        # if search_term is alphabetically lower than midpoint, move down high pointer
        else:
            high = mid - 1
    # if low surpasses high, the list does not contain the search_term
    return f'No video found with title "{search_term}"'

# test
print()
search_for_video(videos, "Exploring the Cosmos")
search_for_video(videos, "History Uncovered: Ancient Civilizations")
search_for_video(videos, "Travel Diaries: Discovering Europe")
search_for_video(videos, "Avengers: Endgame")



# Task 2 - Develop a REST API endpoint using Flask that allows users to search for videos by their titles using the binary search developed in Task 1.
app = Flask(__name__)
app.json.sort_keys = False

@app.route("/")
def home():
    return "Welcome!"

@app.route("/search/<string:title>", methods = ["GET"])
def search_videos(title):
    return search_for_video(videos, title)

# Task 3 - Test the video search functionality: ✅

# Video Sorting with Merge Sort

# Task 1 - Implement the merge sort algorithm in Python to sort videos by their titles: ✅
# Note: I put this function above the binary search, so the binary search would be searching a sorted list


# Task 2 - Develop another REST API endpoint using Flask that allows users to fetch a list of videos sorting alphabetically by their titles

@app.route("/videos")
def view_videos():
    return videos # already sorted by the merge sort implemented above

# Task 3 - Test the video sorting functionality ✅