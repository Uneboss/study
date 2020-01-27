#Google Play Store reviews
#Uber Driver

library(tidytext)
library(textdata)
library(dplyr)

bing <- get_sentiments("bing")
bing1 <- bing %>% filter(word != "noise")

setwd("C:\\Users\\Desktop\\please")
df <- read.csv("C:/textmining/review_data(3120).csv")

df$comment <- gsub("app|apps","",df$comment)
df$comment <- gsub("uber|ubers","",df$comment)
df$comment <- gsub("issues","issue",df$comment)
df$comment <- gsub("update","",df$comment)


library(tidytext)
text_df <- data.frame(rid=1:nrow(df),text=df$comment)

tidy_text <- text_df %>% unnest_tokens(word,text,token = "ngrams", n = 1)

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


bing_word_counts <- tidy_text %>%
  inner_join(bing1) %>% 
  count(word, sentiment, sort = TRUE) %>%
  ungroup()

library(ggplot2)
bing_word_counts %>%
  group_by(sentiment) %>%
  top_n(20) %>%
  ungroup() %>%
  mutate(word = reorder(word, n)) %>%
  ggplot(aes(word, n, fill = sentiment)) +
  geom_col(show.legend = FALSE) +
  facet_wrap(~sentiment, scales = "free_y") +
  labs(y = "Contribution to sentiment", x = NULL) +
  coord_flip()
