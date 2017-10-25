setwd("C:/Users/cmlim/Dropbox/NYC Data Science/Class/Web Scraping Project/review_sa")
library(tidyverse)
library(tidytext)
library(stringr)
library(dplyr)

###Read Positive & Negative Reviews###
filecsv='posneg_review.csv'
texts=read.csv(filecsv,header=TRUE, stringsAsFactors = FALSE)
head(texts)
texts$review_num=as.factor(texts$review_num)
### Tag Line Number ###
texts2 <- texts %>%
  mutate(linenumber = row_number())%>%
  ungroup()

texts2
### Tokenize each word (separate each word to a Single Row)
library(tidytext)
texts3 <- texts2 %>%
  unnest_tokens(word, review_text)
texts3

###Remove Stop Words
data("stop_words")
cleaned_texts <- texts3 %>%
  anti_join(stop_words)

cleaned_texts %>%
  count(word, sort = TRUE)

### Find a sentiment score for each word using the Bing lexicon
library(tidyr)
bing <- get_sentiments("bing")

review_sentiment <- cleaned_texts %>%
  inner_join(bing) %>%
  count(review_num, index = linenumber, 
        sentiment) %>%
  spread(sentiment, n, fill = 0) %>%
  mutate(sentiment = positive - negative)

### Finally, plot the trajectory of sentiments
library(ggplot2)

ggplot(review_sentiment, aes(index,sentiment,fill=(sentiment>0))) +
geom_bar(stat = "identity", show.legend = FALSE) +
xlab('Review Number') +
ylab('Sentiment') +
facet_wrap(~review_num, ncol = 2, scales = "free_x") + 
theme_dark() +
ggtitle('Sentiment Analysis on Negative and Positive Reviews')
