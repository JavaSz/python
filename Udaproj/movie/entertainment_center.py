# -*- coding:utf-8 -*-
import media
import fresh_tomatoes


The_God_Father = media.Movie(
    "The Godfather",
    " ",
    "https://img3.doubanio.com/view/photo/l/public/p2190556185.webp",
    "https://www.youtube.com/watch?v=x6B190eJtdA"
)
The_Shaw_shank = media.Movie("Xiao Ri Ben",
                             "laugh",
                             "https://img3.doubanio.com/view/photo/l/public/p1181775734.webp",
                             "https://www.youtube.com/watch?v=HUV-2GmlL8M"
)

leon = media.Movie("Leon",
                             "里昂是幸福也是幸運的",
                             "https://img3.doubanio.com/view/photo/l/public/p511118051.webp",
                             "https://www.youtube.com/watch?v=4NsIGBwwV1o"
)

# print(The_Shaw_shank.show_trailer())
movies = [The_God_Father, The_Shaw_shank, leon]
fresh_tomatoes.open_movies_page(movies)
