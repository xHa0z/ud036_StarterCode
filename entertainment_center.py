import media, fresh_tomatoes

# URL only supports YouTube videos
the_Shawshank_Redemption = media.Movie('The Shawshank Redemption',
                                       'Two imprisoned men bond over a number '
                                       'of years, '
                                       'finding solace and eventual redemption '
                                       'through acts of common decency.',
                                       'https://images-na.ssl-images-amazon.com/'
                                       'images/M/'
                                       'MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU'
                                       '2MjEyMDE@._V1_SY1000_CR0,0,672,1000_AL_.jpg',
                                       'https://youtu.be/K_tLp7T6U1c')


the_Godfather = media.Movie('The Godfather',
                            'The aging patriarch of an organized crime dynasty '
                            'transfers control of his clandestine '
                            'empire to his reluctant son.',
                            'https://images-na.ssl-images-amazon.com/images/M/'
                            'MV5BZTRmNjQ1ZDYtNDgzMy00OGE0LWE4N2YtNTkzNWQ5ZDhlNGJ'
                            'mL2ltYWdlL2ltYWdlXkEyXkFqcGde'
                            'QXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,704,1000_AL_.jpg',
                            'https://youtu.be/sY1S34973zA')

moives_list = [the_Shawshank_Redemption, the_Godfather]
fresh_tomatoes.open_movies_page(moives_list)