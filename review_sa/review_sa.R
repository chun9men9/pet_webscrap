setwd("C:/Users/cmlim/Dropbox/NYC Data Science/Class/Web Scraping Project/review_sa")
library(tidyverse)
library(tidytext)
library(stringr)
library(dplyr)

#filecsv='one_pos_review.csv'
filecsv='one_neg_review.csv'
  texts=read.csv(filecsv,header = FALSE, stringsAsFactors = FALSE)
  head(texts)
  
  ### Tag Line Number ###
  texts2 <- texts %>%
    #group_by(book) %>%
    mutate(linenumber = row_number())%>%
    ungroup()
  
  texts2
  ### Tokenize each word (separate each word to a Single Row)
  library(tidytext)
  texts3 <- texts2 %>%
    unnest_tokens(word, V1)
  texts3
  
  ###Remove Stop Words
  data("stop_words")
  cleaned_texts <- texts3 %>%
    anti_join(stop_words)
  
  cleaned_texts %>%
    count(word, sort = TRUE)
  ###Retrieve 'Joy' sentiments and store it in nrcjoy
  nrcjoy <- get_sentiments("nrc") %>%
    filter(sentiment == "joy")
  ### List out Words associated with Joy and their Counts
  #cleaned_texts %>%
  #  semi_join(nrcjoy) %>%
  #  count(word, sort = TRUE)
  ### Find a sentiment score for each word using the Bing lexicon
  library(tidyr)
  bing <- get_sentiments("bing")
  
 
  review_sentiment <- cleaned_texts %>%
    inner_join(bing) %>%
    count(word, index = linenumber, #%/% 80, 
          sentiment) %>%
    spread(sentiment, n, fill = 0) %>%
    mutate(sentiment = positive - negative)
  
  ### Finally, plot the trajectory of sentiments as we go along each word
  library(ggplot2)
  
  ggplot(review_sentiment, aes(index,sentiment,fill=(sentiment>0))) +
  geom_bar(stat = "identity", show.legend = FALSE)
    
    #facet_wrap(~book, ncol = 2, scales = "free_x")
  #word_tb <- texts%>%unnest_tokens(word, TXT)
#}

#run_sa('neg_review.csv')
  #ggplot(cleaned_texts, aes(index,sentiment,fill=sentiment)) +
  #  geom_bar(stat = "identity", show.legend = FALSE)