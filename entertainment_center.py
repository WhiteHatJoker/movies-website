import media
import fresh_tomatoes

# Instances of my six favorite movies with titles, storyline, image and youtube

# Ruroini Kensin instance
ruroini_kensin = media.Movie("Ruroini Kenshin",
                             "Kenshin Himura goes up against pure evil Makoto Shishio who is attempting to \
                             overthrow the Meiji government. The fate of the\
                             country hangs in the balance as Kenshin Himura\
                             takes up the sword that he vowed to never\
                             draw again.",
                             "http://ia.media-imdb.com/images/M/MV5BMTkzMzM2NTg1M15BMl5BanBnXkFtZTgwMzczNDgzMjE@._V1_SY317_CR5,0,214,317_AL_.jpg",
                             "https://www.youtube.com/watch?v=5QyfBfY_lLo",
                             2014,
                             5)
# Dark knight instance
dark_knight = media.Movie("Dark Knight Rises",
                          "Eight years after the Joker's reign of anarchy,\
                           the Dark Knight is forced to return from his \
                           imposed exile to save Gotham City from the \
                           brutal guerrilla terrorist Bane with \
                           the help of the enigmatic Selina.",
                          "http://ia.media-imdb.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_SX214_AL_.jpg",
                          "https://www.youtube.com/watch?v=7gFwvozMHR4",
                          2012,
                          4)
# Never back down instance
never_back_down = media.Movie("Never Back Down",
                              "At his new high school, a rebellious teen is\
                              lured into an underground fight club, where \
                              he finds a mentor in a mixed martial arts \
                              veteran.",
                              "http://ia.media-imdb.com/images/M/MV5BMTkzNDg3MTIyMF5BMl5BanBnXkFtZTcwOTAwNDc1MQ@@._V1_SY317_CR1,0,214,317_AL_.jpg",
                              "https://www.youtube.com/watch?v=s8aGqjNM0k4",
                              2008,
                              5)
# Jurassic world instance
jurassic_world = media.Movie("Jurassic World",
                             "A new theme park is built on the original \
                             site of Jurassic Park. Everything is going \
                             well until the park's newest attraction escapes\
                             containment and goes on a killing spree.",
                             "http://ia.media-imdb.com/images/M/MV5BMTQ5MTE0MTk3Nl5BMl5BanBnXkFtZTgwMjczMzk2NTE@._V1_SX214_AL_.jpg",
                             "https://www.youtube.com/watch?v=RFinNxS5KN4",
                             2015,
                             4)
# Southpaw instance
southpaw = media.Movie("Southpaw",
                       "Boxer Billy Hope turns to trainer Tick Willis\
                       to help him get his life back on track after \
                       losing his wife in a tragic accident and his \
                       daughter to child protection services.",
                       "http://ia.media-imdb.com/images/M/MV5BMjI1MTcwODk0MV5BMl5BanBnXkFtZTgwMTgwMDM5NTE@._V1_SX214_AL_.jpg",
                       "https://www.youtube.com/watch?v=Mh2ebPxhoLs",
                       2015,
                       4)
# Descendants instance
descendants = media.Movie("Descendants",
                          "A present-day idyllic kingdom where the\
                          benevolent teenage son of King Adam and \
                          Queen Belle offers a chance of redemption\
                          for the trouble making offspring of Disney's\
                          classic villains.",
                          "http://ia.media-imdb.com/images/M/MV5BMTA5MTE2Mzc5MjReQTJeQWpwZ15BbWU4MDk0Njg2ODUx._V1_SX214_AL_.jpg",
                          "https://www.youtube.com/watch?v=yJCphjtVek0",
                          2014,
                          3)
# Array of instances of movie
movies = [ruroini_kensin, dark_knight, never_back_down,
          jurassic_world, southpaw, descendants]

# Passing the array to open_movies function within fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
