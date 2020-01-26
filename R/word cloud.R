library(tidytext)
library(textdata)
library(dplyr)


setwd("C:\\Users\\Desktop\\please")
df <- read.csv("C:\\textmining\\review_data(3120).csv")


df$comment <- gsub("app|apps","",df$comment)
df$comment <- gsub("uber|ubers","",df$comment)
df$comment <- gsub("issues","issue",df$comment)
df$comment <- gsub("update","",df$comment)


library(tidytext)
text_df <- data.frame(rid=1:nrow(df),text=df$comment)
text_df1 <- data.frame(rid=1:nrow(df),text=df$comment, stars = df$stars, helpful = df$helpful)
score1_text <- text_df1 %>% filter(stars=="Rated 1 stars out of five stars") 
score5_text <- text_df1 %>% filter(stars=="Rated 5 stars out of five stars"| stars=="Rated 4 stars out of five stars") 

tidy_text <- text_df %>% unnest_tokens(word,text,token = "ngrams", n = 1)
tidy_score1 <- score1_text %>% unnest_tokens(word,text,token = "ngrams", n = 1)
tidy_score5 <- score5_text %>% unnest_tokens(word,text,token = "ngrams", n = 1)


tidy_text$word <- gsub("app|apps","",tidy_text$word)
tidy_text$word <- gsub("riders|rider|drivers","driver",tidy_text$word)
tidy_text$word <- gsub("rides|riding","ride",tidy_text$word)
tidy_text$word <- gsub("drives|driving","drive",tidy_text$word)
tidy_text$word <- gsub("updates|updating|updated","update",tidy_text$word)
tidy_text$word <- gsub("days|day","",tidy_text$word)
tidy_text$word <- gsub("trips","trip",tidy_text$word)
tidy_text$word <- gsub("uber|ubers","",tidy_text$word)
tidy_text$word <- gsub("issues","issue",tidy_text$word)
tidy_text$word <- gsub("2|5|3|0|1|4","",tidy_text$word)
tidy_text$word <- gsub("times","time",tidy_text$word)

tidy_score1$word <- gsub("app|apps","",tidy_score1$word)
tidy_score1$word <- gsub("riders|rider|drivers|driver","",tidy_score1$word)
tidy_score1$word <- gsub("rides|riding|ride","",tidy_score1$word)
tidy_score1$word <- gsub("drives|driving|drive","",tidy_score1$word)
tidy_score1$word <- gsub("updates|updating|updated|update","",tidy_score1$word)
tidy_score1$word <- gsub("called|calls","call",tidy_score1$word)
tidy_score1$word <- gsub("days|day","",tidy_score1$word)
tidy_score1$word <- gsub("trips|trip","",tidy_score1$word)
tidy_score1$word <- gsub("support","",tidy_score1$word)
tidy_score1$word <- gsub("uber|ubers","",tidy_score1$word)
tidy_score1$word <- gsub("issues","issue","",tidy_score1$word)
tidy_score1$word <- gsub("2|5|3|0|1|4","",tidy_score1$word)
tidy_score1$word <- gsub("times|time","",tidy_score1$word)

tidy_score5$word <- gsub("app|apps","",tidy_score5$word)
tidy_score5$word <- gsub("riders|rider|drivers|driver","",tidy_score5$word)
tidy_score5$word <- gsub("rides|riding|ride","",tidy_score5$word)
tidy_score5$word <- gsub("drives|driving|drive","",tidy_score5$word)
tidy_score5$word <- gsub("updates|updating|update","",tidy_score5$word)
tidy_score5$word <- gsub("days|day","",tidy_score5$word)
tidy_score5$word <- gsub("trips|trip","",tidy_score5$word)
tidy_score5$word <- gsub("support","",tidy_score5$word)
tidy_score5$word <- gsub("uber|ubers","",tidy_score5$word)
tidy_score5$word <- gsub("issues|issue","",tidy_score5$word)
tidy_score5$word <- gsub("2|5|3|0|1|4","",tidy_score5$word)
tidy_score5$word <- gsub("times|time","",tidy_score5$word)


data(stop_words)
tidy_text <- tidy_text %>% anti_join(stop_words)
tidy_score1 <- tidy_score1 %>% anti_join(stop_words)
tidy_score5 <- tidy_score5 %>% anti_join(stop_words)


# word cloud of full review
tidy_text %>%
  anti_join(stop_words) %>%
  count(word,sort = TRUE)%>%
  head(50) %>%
  wordcloud2(size = 3, color = "random-light", fontFamily = 'Tahoma', minRotation = -pi/2, maxRotation = -pi/2)

# word cloud of one point reviews
tidy_score1 %>%
  anti_join(stop_words) %>%
  count(word,sort = TRUE)%>%
  head(50) %>%
  wordcloud2(size = 6, color = "random-light", fontFamily = 'Tahoma', minRotation = -pi/2, maxRotation = -pi/2)

# word cloud of five point reviews
tidy_score5 %>%
  anti_join(stop_words) %>%
  count(word,sort = TRUE)%>%
  head(50) %>%
  wordcloud2(size = 1.2, color = "random-light", fontFamily = 'Tahoma', minRotation = -pi/2, maxRotation = -pi/2)

