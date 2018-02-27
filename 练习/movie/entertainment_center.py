import fresh_tomatoes
import media

War_Horse=media.Movie("War Horse",
                      "Albert (Jeremy Irvine) and his beloved horse, Joey, live on a farm in the British countryside. At the outbreak of World War I, Albert and Joey are forcibly parted when Albert's father sells the horse to the British cavalry. Against the backdrop of the Great War, Joey begins an odyssey full of danger, joy and sorrow, and he transforms everyone he meets along the way. Meanwhile Albert, unable to forget his equine friend, searches the battlefields of France to find Joey and bring him home.",
                      "http://t1.gstatic.com/images?q=tbn:ANd9GcQwV-SggUgYZIx57W_NbQco8VxUMZv1V_4VzNmOoJfhqCRKAV07",
                     "https://www.youtube.com/watch?v=ZattjwT-c6k")

#print(War_Horse.storyline)
#War_Horse.show_trailer()
#print(War_Horse.title)
#War_Horse.show_poster()


Flipped=media.Movie("Flipped",
                    "When they meet in second grade, Juli Baker falls instantly in love with her neighbor, Bryce Loski. Bryce, however, does not feel the spark. From that day forward, he (Callan McAuliffe) tries hard to keep brash and unpredictable Juli (Madeline Carroll) at bay. After six years, she begins to feel that she was wrong about him being the love of her life. Unfortunately, that is just about the time that Bryce begins to think he was wrong about Juli, too.",
                    "https://upload.wikimedia.org/wikipedia/zh/3/3a/Flipped_poster.jpg",
                    "https://www.youtube.com/watch?v=GJrVjw446lk&t=60s")

#print(Flipped.storyline)
#Flipped.show_trailer()
#print(Flipped.title)
#Flipped.show_poster()


Wonder=media.Movie("Wonder",
                   "Based on the New York Times bestseller, WONDER tells the incredibly inspiring and heartwarming story of August Pullman, a boy with facial differences who enters fifth grade, attending a mainstream elementary school for the first time.",
                   "https://upload.wikimedia.org/wikipedia/zh/8/85/Wonder_%28film%29.jpg",
                   "https://www.youtube.com/watch?v=Ob7fPOzbmzE")


#print(Wonder.storyline)
#Wonder.show_trailer()
#print(Wonder.title)
#Wonder.show_poster()

The_Chorus=media.Movie("The Chorus",
                         "All started in 1999 as an elderly man who was resting on the couch by Mauchin, a conductor of a large orchestra who returned to his hometown after receiving the call of his mother's death and, in the evening, fifty Babe died a long time gone friend took a photo, a diary came to himThat was the story 50 years ago when they were still in the same parenting school ....",
                         "https://upload.wikimedia.org/wikipedia/zh/3/33/Les_Choristes_movie.jpg",
                         "https://www.youtube.com/watch?v=xPnF6sJAjZs")
#print(The_Chorus.title)
#print(The_Chorus.storyline)
#The_Chorus.show_poster()
#The_Chorus.show_trailer()

This_killer_is_not_too_cold=media.Movie("This killer is not too cold ",
                                        "Lyon Montana ( Jean Reynaud ) is the top Italian professional killer, has been living alone in Little Italy , New York , only a pot of evergreen is his best friend. He said: 'It is always happy, never asked questions, and it is just like me - there is no root.' Although he has great skills, his heart is actually very insecure. Instead of even sleeping in bed, he slept in a chair and placed a pistol next to his hand to keep his opponent ready.",
                                        "https://upload.wikimedia.org/wikipedia/zh/2/26/%E8%BF%99%E4%B8%AA%E6%9D%80%E6%89%8B%E4%B8%8D%E5%A4%AA%E5%86%B7.jpg",
                                        "https://www.youtube.com/watch?v=DcsirofJrlM")

#print(This_killer_is_not_too_cold.title)
#print(This_killer_is_not_too_cold.storyline)
#This_killer_is_not_too_cold.show_poster()
#This_killer_is_not_too_cold.show_trailer()


The_Shawshank_Redemption=media.Movie("The Shawshank Redemption",
                                     "In 1947, a young Portland banker, Andy Dufranne ( Tim Robbins ), was accused of killing his wife and her husband , each sentenced to life imprisonment of two and entered Shark Prison , Maine (Xiaoshan Ke prison). On the other hand, Reed ( Morgan Freeman ) , a prisoner at Sharksburgh Prison, who applied for parole after being sentenced to 20 years in prison and was dismissed, happened to have seen the arrival of new prisoners in the Shark Fort Prison as well Including Andy. The new prisoners have to meet with Chief Warren Norton and prison guard Captain Haley before entering prison. That night, one of the prisoners cries because they can not adapt to the dark conditions of the prison and is then killed by Captain Haley.",
                                     "https://upload.wikimedia.org/wikipedia/zh/a/af/Shawshank_Redemption_ver2.jpg",
                                     "https://www.youtube.com/watch?v=6hB3S9bIaco")

#print(The_Shawshank_Redemption.title)
#print(The_Shawshank_Redemption.storyline)
#The_Shawshank_Redemption.show_poster()
#The_Shawshank_Redemption.show_trailer()



movies=[War_Horse,Flipped,Wonder,The_Chorus,This_killer_is_not_too_cold,The_Shawshank_Redemption]
#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_PATINGS)

print(media.Movie.__doc__)

