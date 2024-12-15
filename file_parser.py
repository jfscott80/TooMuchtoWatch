from media import Series, Movie
class FileParser:

	def __init__(self, filename):
		self.media_list = []
		self.__process_file(filename)
		
	def __process_line(self, s):
		while True:
			s = s.replace('""','^')
			first_quote = s.find('"')	#look for a quote
			if first_quote == -1:		#if quotes don't exist (-1), break
				break
			second_quote = s.find('"', first_quote + 1)	#look for another quote	starting from index last quote + 1
	     
	        
			s2 = s[:first_quote] + s[first_quote + 1 : second_quote].replace(",",";") + s[second_quote + 1:]
			s = s2
		return s
	
	def __process_file(self, filename):
		
		with open(filename, newline='', encoding='utf-8') as f: 
			
			file = f.readlines()
			for line in file[1:]:
				#print(len(self.media_list))
				processed_line = self.__process_line(line)
				
				show_id, types, title, director, cast, country, date_added, release_year, rating, duration, listed_in, descriprion = processed_line.split(",")

				if types == 'TV Show':
					series = Series(title, director, cast, country, release_year, rating, duration.split(" ")[0], listed_in, descriprion )
					self.media_list.append(series)
				else:
					movie = Movie(title, director, cast, country, release_year, rating, duration.split(" ")[0], listed_in, descriprion )
					self.media_list.append(movie)

	def get_media_list(self):
		return self.media_list