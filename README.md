# TooMuchtoWatch
CS 2150 parse .csv file - allow user to filter

I’ve provided a data file with all of Netflix’s streaming offerings as of late 20211. The file is in
CSV (comma-separated values) format and can be opened in either a spreadsheet or a text editor
to view its contents. The first line of the file includes information on what each column represents.
Each subsequent line is called a record and contains info about a single movie or series.
Each record is divided into fields, which are separated by commas (thus the name “commaseparated values”). The fields used in this project are:
• Type (movie or series) — for this project we’ll assume “movie” means anything that’s not
episodic, including documentaries, stand-up comedy specials, etc.
• Title
• Director
• Cast
• Country
• Release year
• Rating (G, PG, TV-MA, etc.)
• Duration (runtime in minutes for a movie, or number of seasons for a series)
• Genre (action, sci-fi, etc. — the file calls this listed in)
• Description
Note that some fields are absent from some records; these are indicated with an empty string
between the separating commas. Fields that themselves contain commas are placed between double
quotes, to prevent confusion with the commas being used to separate fields from one another.
Double quotes that are meant to be included as part of a field are represented as two consecutive
double quotes (""). 

In this project you’ll be writing some software that parses (reads) the data file and allows the user
to apply and remove filters to customize the results. That should make it easier to pick from the
huge selection of options available! For example, the user may want to see a list of all the movies
released before 2015 that feature Cate Blanchett. This would be expressed using the following three
filters:
1. movie
2. year < 2015
3. cast cate blanchett
The user should be able to add as many filters as they want, and the software should allow the
user to display a list of the media records from the data file that match all the filters. The user
should also be able to remove filters at will. Every time a filter is added or removed, the software
should indicate 1) the currently active filters, and 2) how many items from the data file match all
filters in the filter list.
