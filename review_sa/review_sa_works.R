setwd("C:/Users/cmlim/Dropbox/NYC Data Science/Class/Web Scraping Project/review_sa")
library(tidyverse)
library(tidytext)
library(stringr)
library(dplyr)
#run_sa=function(filecsv, cloudname,excludelis=c('')){
filecsv='one_pos_review.csv'
  texts=read.csv(filecsv,header = FALSE, stringsAsFactors = FALSE)
  # head(texts)
  # texts=texts[,1]
  # TXT=paste0(texts[], collapse = "\n")
  # cat(nchar(TXT))
  # texts=read.csv(filecsv,header = FALSE)
  head(texts)
  texts2 <- texts %>%
    #group_by(book) %>%
    mutate(linenumber = row_number())%>%
           #chapter = cumsum(str_detect(text, regex("^chapter [\\divxlc]",
            #                                       ignore_case = TRUE)))) %>%
    ungroup()
  
  texts2
  library(tidytext)
  texts3 <- texts2 %>%
    unnest_tokens(word, V1)
  
  texts3
  
  data("stop_words")
  cleaned_texts <- texts3 %>%
    anti_join(stop_words)
  
  cleaned_texts %>%
    count(word, sort = TRUE)
  
  nrcjoy <- get_sentiments("nrc") %>%
    filter(sentiment == "joy")
  
  cleaned_texts %>%
    semi_join(nrcjoy) %>%
    count(word, sort = TRUE)
  
  library(tidyr)
  bing <- get_sentiments("bing")
  
  review_sentiment <- cleaned_texts %>%
    inner_join(bing) %>%
    count(word, index = linenumber %/% 80, sentiment) %>%
    spread(sentiment, n, fill = 0) %>%
    mutate(sentiment = positive - negative)
  
  library(ggplot2)
  
  ggplot(review_sentiment, aes(c(1:6),sentiment,fill=sentiment)) +
    geom_bar(stat = "identity", show.legend = FALSE)#+
    #facet_wrap(~book, ncol = 2, scales = "free_x")
  #word_tb <- texts%>%unnest_tokens(word, TXT)
#}

#run_sa('neg_review.csv')
