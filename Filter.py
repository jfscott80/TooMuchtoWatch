'''
this file builds filter objects for the user
conditionals built for several specific types of filters listed in menu on main.py 
alternate generalized filter conditionals provided
'''
import media

# create a filter class
class Filter:
	# constructor
	def __init__(self, filter_string):
		self.name = filter_string
		values = filter_string.split()
		self.format = values[0]
		if self.format == "movie" or self.format == "series":
			self.operator = None
			self.value = None
		elif self.format == "year" or self.format == "runtime":# and len(self.format) == 3:
			self.operator = values[1]
			self.value = int(values[2])
		else:
			self.value = ' '.join(values[1:])
			self.operator = None

# create a class to handle all filter operations once the user creates the filters
class FilterList:
	def __init__(self):
		self.filters = []
		self.count = 0

	def __str__(self):
		result = '\nCurrent Filters\n-----------------\n'
		i = 1
		for f in self.filters:
			result += f'{i}. {f.name}\n'
			i += 1

		return result

	# add filter to filter list
	def add(self, data):
		self.filtered_list = []
		self.filters.append(Filter(data))
		self.count += 1

	# remove filter from list on menu by number
	def remove(self, number):
		if len(self.filters) > 0:
			# next line accounts for discrepancy between listed number and index
			self.filters.pop(number - 1)
			self.count -= 1




	def apply_filters(self, media_list):
		self.filtered_list = media_list.copy()
		
		for filter in self.filters:
			temp_filterd_list = []
			if filter.format.lower() == "movie":
				for m in self.filtered_list:
					if isinstance(m, media.Movie):
						temp_filterd_list.append(m)
				self.filtered_list = temp_filterd_list

			elif filter.format.lower() == "series":
				for m in self.filtered_list:
					if isinstance(m, media.Series):
						temp_filterd_list.append(m)
				self.filtered_list = temp_filterd_list
				
			elif filter.format.lower() == "title":
				for m in self.filtered_list:
					if filter.value.lower() in m.title.lower():
						temp_filterd_list.append(m)
				self.filtered_list = temp_filterd_list

			elif filter.format.lower() == "director":
				for m in self.filtered_list:
					if filter.value.lower() in m.director.lower():
						temp_filterd_list.append(m)
				self.filtered_list = temp_filterd_list

			elif filter.format.lower() == "cast":
				for m in self.filtered_list:
					if filter.value.lower() in m.cast.lower():
						temp_filterd_list.append(m)
				self.filtered_list = temp_filterd_list

			elif filter.format.lower() == "country":
				for m in self.filtered_list:
					if filter.value.lower() in m.country.lower():
						temp_filterd_list.append(m)
				self.filtered_list = temp_filterd_list

			elif filter.format.lower() == "rating":
				for m in self.filtered_list:
					if filter.value.lower() == m.rating.lower():
						temp_filterd_list.append(m)
				self.filtered_list = temp_filterd_list
					
			elif filter.format.lower() == "genre":
				for m in self.filtered_list:
					if filter.value.lower() in m.genre.lower():
						temp_filterd_list.append(m)
				self.filtered_list = temp_filterd_list

			elif filter.format.lower() == "description":
				for m in self.filtered_list:
					if filter.value.lower() in m.description.lower():
						temp_filterd_list.append(m)
				self.filtered_list = temp_filterd_list

			elif filter.format == "year":
				if filter.operator == "<":
					for m in self.filtered_list:
						if m.release_year < filter.value:
							temp_filterd_list.append(m)
					self.filtered_list = temp_filterd_list

				elif filter.operator == ">":
					for m in self.filtered_list:
						if m.release_year > filter.value:
							temp_filterd_list.append(m)
					self.filtered_list = temp_filterd_list
      		
				elif filter.operator == "<=":
					for m in self.filtered_list:
						if m.release_year <= filter.value:
							temp_filterd_list.append(m)
					self.filtered_list = temp_filterd_list
      		
				elif filter.operator == ">=":
					for m in self.filtered_list:
						if m.release_year >= filter.value:
							temp_filterd_list.append(m)
					self.filtered_list = temp_filterd_list
      		
				elif filter.operator == "=":
					for m in self.filtered_list:
						if m.release_year == filter.value:
							temp_filterd_list.append(m)
					self.filtered_list = temp_filterd_list
      		

			elif filter.format == "runtime":
				if filter.operator == "<":
					for m in self.filtered_list:
						if isinstance(m, media.Movie) and m.runtime < filter.value:
							temp_filterd_list.append(m)
					self.filtered_list = temp_filterd_list
      		
				elif filter.operator == ">":
					for m in self.filtered_list:
						if isinstance(m, media.Movie) and m.runtime > filter.value:
							temp_filterd_list.append(m)
					self.filtered_list = temp_filterd_list
      		
				elif filter.operator == "<=":
					for m in self.filtered_list:
						if isinstance(m, media.Movie) and m.runtime <= filter.value:
							temp_filterd_list.append(m)
					self.filtered_list = temp_filterd_list
      		
				elif filter.operator == ">=":
					for m in self.filtered_list:
						if isinstance(m, media.Movie) and m.runtime >= filter.value:
							temp_filterd_list.append(m)
					self.filtered_list = temp_filterd_list
      		
				elif filter.operator == "=":
					for m in self.filtered_list:
						if isinstance(m, media.Movie) and m.runtime == filter.value:
							temp_filterd_list.append(m)
					self.filtered_list = temp_filterd_list
 
			# user created general filter, search all categories
			elif filter.format == "general":
				for m in self.filtered_list:
					if filter.value.lower() in m.title.lower():
						temp_filterd_list.append(m)
					elif filter.value.lower() in m.director.lower():
						temp_filterd_list.append(m)
					elif filter.value.lower() in m.cast.lower():
						temp_filterd_list.append(m)
					elif filter.value.lower() in m.country.lower():
						temp_filterd_list.append(m)
					elif filter.value.lower() == m.rating.lower():
						temp_filterd_list.append(m)
					elif filter.value.lower() in m.genre.lower():
						temp_filterd_list.append(m)
					elif filter.value.lower() in m.description.lower():
						temp_filterd_list.append(m)
						if filter.value.lower() in m.description.lower():
							temp_filterd_list.append(m)

				# load to filtered list of objects						
				self.filtered_list = temp_filterd_list



	def get_filtered_list(self):
		return self.filtered_list
