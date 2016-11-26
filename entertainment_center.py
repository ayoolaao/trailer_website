import media

toy_story = media.Movie("The Flash",
                        "The story of a boy",
                        "http://cdn-static.sidereel.com/tv_shows/57093/giant_2x/the-flash.jpg",
                        "https://www.youtube.com/watch?v=f5gmEHbBPWs&t=5s")

ayo_story = media.Movie("The Ayoola",
                        "The story of a man",
                        "http://cdn-static.sidereel.com/tv_shows/57093/giant_2x/the-flash.jpg",
                        "https://www.youtube.com/watch?v=f5gmEHbBPWs&t=5s")

print(toy_story.storyline)
print(ayo_story.storyline)