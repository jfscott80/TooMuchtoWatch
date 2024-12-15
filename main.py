'''
This project has been written by and submitted on behalf of:

Monika Coates
mcoates1@memphis.edu

and

John Scott U00832531
jfscott@memphis.edu



this file is run by user
- functions are set to handle different aspects of the user interface menus
- reads data file with file parser.py
- creates master list of all objects in the media class from media.py
- creates a filter list for user to add or remove from to filter
objects out of master list into current list
'''


from file_parser import FileParser
from Filter import FilterList

def main_menu():
	print("\n(a)dd a new filter")
	print("(r)emove a filter")
	# apply filters to current list
	filter_list.apply_filters(list_finder())
	current_list = filter_list.get_filtered_list()
	print(f"(d)isplay filtered media ({len(current_list)} found)")
	print("(e)xit")
	user_choice = input("\nEnter your choice: ").lower()
	while user_choice != "a" and user_choice != "r" and user_choice != "e" and user_choice != "d":
		user_choice = input("Incorrect value. Choose (a)dd, (r)emove, (d)isplay, or (e)xit ").lower()
	return user_choice

def filters_menu():
	print()
	print('You can use one of the following filters:')
	print("movie ")
	print("series")
	print("title ")
	print("director")
	print("cast ")
	print("country ")
	print("genre")
	print("rating")
	print("year")
	print("runtime")
	print("general")
	user_filter = input("\nEnter your filter: ")
	return user_filter	

# remove function helper, gains further user input
def drop_filter():
	print(filter_list)
	try:	# FilterList object remove method requires an integer
		user_selection = int(input("Enter filter number to remove: "))
		return user_selection
	except ValueError:	# exception handling prints error message and returns itself
		print('(error please enter a number)')
		return drop_filter()

# call to convert file to media objects, find master list and current list
def list_finder():
	my_parser = FileParser("netflix_titles.csv")
	# This finds the master list of media objects
	master_list = my_parser.get_media_list()
	# initialize current list
	current_list = my_parser.get_media_list()
	return current_list



# function acts as main user interface, calls other functions and class methods as necessary to guide user 
def user_menu():
# initialize to begin loop
	user_choice = ""
	user_selection = ""

	# loop continues program until asked to exit
	while user_choice != 'e':
		user_choice = main_menu()

		# If user wants to add a filter
		if user_choice == "a":
			user_filter = filters_menu()
			filter_list.add(user_filter)

		elif user_choice == "d":
			filter_list.apply_filters(list_finder())
			current_list = filter_list.get_filtered_list()
			print("\nDisplaying", len(current_list), "medias")
			for m in current_list:
				print()
				print(m)
			user_choice = ""

		elif user_choice == "r":
			if filter_list.count == 0:
				print('\n(error) - no items to be removed')

			else:
				# allow user to pick filter by number
				user_selection = drop_filter()
				# check user input for valid entry
				y = 0
				while user_selection > filter_list.count:
					if y < 2:
						print('(error: Please select a number listed)')
						# user_selection out of range handling
						y += 1
						# print(filter_list)
						user_selection = drop_filter()
					else:	# break this loop if error persists
						print('(error returning to main menu)')
						user_menu()

				filter_list.remove(user_selection)
				filter_list.apply_filters(list_finder()) 
				print(filter_list)


# This is list of filters added by user
filter_list = FilterList()

# call function to let the user interact with the program
current_list = list_finder()
user_menu()

