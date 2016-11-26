import media

toy_story = media.Movie("The Flash",
                        "The story of a boy",
                        "http://cdn-static.sidereel.com/tv_shows/57093/giant_2x/the-flash.jpg",
                        "https://www.youtube.com/watch?v=f5gmEHbBPWs&t=5s")

ayo_story = media.Movie("The Ayoola",
                        "The story of a man",
                        "http://cdn-static.sidereel.com/tv_shows/57093/giant_2x/the-flash.jpg",
                        "https://www.youtube.com/watch?v=f5gmEHbBPWs&t=5s")

new_movie = media.Movie("Mr Eazi",
                        "The eazzi man",
                        "http://www.chartsinfrance.net/covers/aHR0cHM6Ly9pLnNjZG4uY28vaW1hZ2UvOWIxYjg2ZWJiNjVhMWYxOTU1NmQzYjBkMDI1ZmRmNGE5N2ZkNmFkOA==.jpg",
                        "https://www.youtube.com/watch?v=vk_4yxkgjAI")

print(ayo_story.storyline)
ayo_story.show_trailer()

new_movie.show_trailer()