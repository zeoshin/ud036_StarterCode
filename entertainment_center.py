import media
import fresh_tomatoes


# Movie Your Name
yourName = media.Movie(
            "Your Name",
            """Two strangers find themselves linked in a bizarre way.
             When a connection forms, will distance be the only thing
             to keep them apart?""",
            "https://images-na.ssl-images-amazon.com/images/" +
            "M/MV5BODRmZDVmNzUtZDA4ZC00NjhkLWI2M2UtN2M0ZDIzNDcx" +
            "YThjL2ltYWdlXkEyXkFqcGdeQXVyNTk0MzMzODA@._V1_SY100" +
            "0_SX675_AL_.jpg",
            "https://www.youtube.com/watch?v=xU47nhruN-Q"
)


# Movie 5 Centimeters Per Second
fiveCentimetersPerSecond = media.Movie(
            "5 Centimeters Per Second",
            """Told in three interconnected segments, we
             follow a young man named Takaki through his
             life as cruel winters, cold technology, and
             finally, adult obligations and responsibility
             converge to test the delicate petals of love.""",
            "https://images-na.ssl-images-amazon.com/images/" +
            "M/MV5BMTI4MDIyNzQyNl5BMl5BanBnXkFtZTcwNDcyNTk2MQ@@._V1_.jpg",
            "https://www.youtube.com/watch?v=wdM7athAem0"
)

# Movie The Garden of Words
theGardenOfWords = media.Movie(
            "The Garden of Words",
            """A 15-year-old boy and 27-year-old woman find
             an unlikely friendship one rainy day in the
             Shinjuku Gyoen National Garden.""",
            "https://images-na.ssl-images-amazon.com/images/" +
            "M/MV5BNGYwMzQ5MjAtYWFjMy00ZTc1LTlkODQtM2Q5YzYzOWVkYT" +
            "dhXkEyXkFqcGdeQXVyNjY1OTY4MTk@._V1_SY1000_CR0,0,715" +
            "1000_AL_.jpg",
            "https://www.youtube.com/watch?v=HTTRweJ7jVs"
)

# The Girl Who Leapt Through Time
theGirlWhoLeaptThroughTime = media.Movie(
            "The Girl Who Leapt Through Time",
            """A high-school girl named Makoto acquires the power
             to travel back in time, and decides to use it for her
             own personal benefits. Little does she know that she
             is affecting the lives of others just as much as she
             is her own.""",
            "https://images-na.ssl-images-amazon.com/images/" +
            "M/MV5BNzUxODI4MzgtNWZiOC00MmNlLWIyMzctNGE3ZGU0Mzcz" +
            "Mjk4XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SY1000_CR0,0,709," +
            "1000_AL_.jpg",
            "https://www.youtube.com/watch?v=198ejsZWsXc"
)

# list of movies
movies = [
             yourName,
             fiveCentimetersPerSecond,
             theGardenOfWords,
             theGirlWhoLeaptThroughTime
         ]

# open website
fresh_tomatoes.open_movies_page(movies)
