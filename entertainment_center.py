import fresh_tomatoes
import movie

the_flash = movie.Movie("The Flash",
                        "The story of a boy",
                        "http://cdn-static.sidereel.com/tv_shows/57093/giant_2x/the-flash.jpg",
                        "https://www.youtube.com/watch?v=f5gmEHbBPWs&t=5s")

justice_league = movie.Movie("JUSTICE LEAGUE",
                            "The story of a man",
                            "https://mfiles.alphacoders.com/638/638377.jpg",
                            "https://www.youtube.com/watch?v=ftDQOV6K158")

logan = movie.Movie("Logan",
                    "Logan Official Trailer",
                    "http://cdn2-www.comingsoon.net/assets/uploads/gallery/untitled-wolverine-sequel/cuaiczwueaaid_w-jpg-large.jpg",
                    "https://www.youtube.com/watch?v=gbug3zTm3Ws")

wonder_woman = movie.Movie("Wonder Woman",
                           "Strong woman",
                           "https://i.paigeeworld.com/user-movie/1461628800000/571e2f62fda29888180e61ab_571fa685fbfb470337cf82c6_320.jpg",
                           "https://www.youtube.com/watch?v=5HUlW21v1fQ")

pirates_of_the_caribbean = movie.Movie("Pirates of the Caribbean",
                                       "Dead Men Tell No Tales",
                                       "https://upload.wikimovie.org/wikipedia/en/2/21/Pirates_of_the_Caribbean,_Dead_Men_Tell_No_Tales.jpg",
                                       "https://www.youtube.com/watch?v=6i77T6KzYxM")

guardians_of_galaxy = movie.Movie("Guardians of the Galaxy Vol. 2",
                                  "Official Trailer - Teaser (2017)",
                                  "http://t3.gstatic.com/images?q=tbn:ANd9GcQWA3pKqv8oaHq4cP6YK3QKpgPbMjoHIzytUlThEF3P8ZAvyeZv",
                                  "https://www.youtube.com/watch?v=wX0aiMVvnvg")

movies = [the_flash, justice_league, logan, wonder_woman, pirates_of_the_caribbean, guardians_of_galaxy]
fresh_tomatoes.open_movies_page(movies)