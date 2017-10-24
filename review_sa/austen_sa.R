library(janeaustenr)
library(dplyr)
library(stringr)
##read in books and label row_number & chapter number 
original_books <- austen_books() %>%
  group_by(book) %>%
  mutate(linenumber = row_number(),
         chapter = cumsum(str_detect(text, regex("^chapter [\\divxlc]",
                                                 ignore_case = TRUE)))) %>%
  ungroup()

original_books

#separate each word
library(tidytext)
tidy_books <- original_books %>%
  unnest_tokens(word, text)

tidy_books

#Clean out stop words
data("stop_words")
cleaned_books <- tidy_books %>%
  anti_join(stop_words)

#Have a quick look at word counts
cleaned_books %>%
  count(word, sort = TRUE) 

#Do inner joins to get word sentiments
nrcjoy <- get_sentiments("nrc") %>%
  filter(sentiment == "joy")
#And then look at words associated with Joy
tidy_books %>%
  filter(book == "Emma") %>%
  semi_join(nrcjoy) %>%
  count(word, sort = TRUE)



library(tidyr)
bing <- get_sentiments("bing")

janeaustensentiment <- tidy_books %>%
  inner_join(bing) %>%
  count(book, index = linenumber %/% 80, sentiment) %>%
  spread(sentiment, n, fill = 0) %>%
  mutate(sentiment = positive - negative)


library(ggplot2)

ggplot(janeaustensentiment, aes(index, sentiment, fill = book)) +
  geom_bar(stat = "identity", show.legend = FALSE) +
  facet_wrap(~book, ncol = 2, scales = "free_x")