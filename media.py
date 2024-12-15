'''
this file handles data gained from file parser, holds media class, movie, series

'''
class Media:
	
	# constructor
	def __init__(self, title, director, cast, country, release_year, rating, genre, description):
		self.title = title
		self.director = director
		self.cast = cast
		self.country = country
		self.release_year = int(release_year)
		self.rating = rating
		self.genre = genre
		self.description = description

	# incrementally build readable string output
	def __str__(self):
		
			s = (f'Title:              {self.title}')
			s += (f'\nDirector:           {self.director}')
			s += (f'\nCast: 		      {self.cast}')
			s += (f'\nCountry:            {self.country}')
			s += (f'\nYear Reseased:      {self.release_year}')
			s += (f'\nRating:             {self.rating}')
			s += (f'\nGenre:              {self.genre}')
			s += (f'\nDescription:        {self.description}')
			return s.replace(";", ",").replace('^', '"')
# media sub-class to handle movie objects - hijack constructor, str methods and add to them
class Movie(Media):
	def __init__(self, title, director, cast, country, release_year, rating, runtime, genre, description):
		Media.__init__(self,title, director, cast, country, release_year, rating, genre, description)
		self.runtime = int(runtime)

	def __str__(self):
		s = Media.__str__(self)
		s += (f'Runtime:    {self.runtime} min')
		return s

# media sub-class to handle tv series objects - hijack constructor, str methods and add to them
class Series(Media):
	def __init__(self, title, director, cast, country, release_year, rating, number_seasons, genre, description):
		Media.__init__(self,title, director, cast, country, release_year, rating, genre, description)
		self.number_seasons = int(number_seasons)


	def __str__(self):
		s = Media.__str__(self)
		s += (f'Number of Seasons:             {self.number_seasons:>10} seasons')
		return s
