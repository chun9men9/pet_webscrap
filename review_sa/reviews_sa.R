setwd("C:/Users/cmlim/Dropbox/NYC Data Science/Class/Web Scraping Project/review_sa")
library(tidyverse)
library(tidytext)
library("tm")
library("SnowballC")
library("wordcloud")
library("RColorBrewer")
library(stringr)
#run_sa=function(filecsv, cloudname,excludelis=c('')){
filecsv='neg_review.csv'
  texts=read.csv(filecsv,header = FALSE, stringsAsFactors = FALSE)
  # head(texts)
  # texts=texts[,1]
  # TXT=paste0(texts[], collapse = "\n")
  # cat(nchar(TXT))
  # texts=read.csv(filecsv,header = FALSE)
  head(texts)
  texts=texts[,2]
  pos_texts=paste0(texts[], collapse = "\n")
  nchar(pos_texts)
  docs <- Corpus(VectorSource(texts))
  # Convert the text to lower case
  docs <- tm_map(docs, content_transformer(tolower))
  # Remove numbers
  docs <- tm_map(docs, removeNumbers)
  # Remove english common stopwords
  docs <- tm_map(docs, removeWords, stopwords("english"))
  # Remove your own stop word
  # specify your stopwords as a character vector
  #default_rmv=c("dog","dogs","food","foods",'can','canned')
  #docs <- tm_map(docs, removeWords, c(default_rmv,excludelis) ) 
  # Remove punctuations
  docs <- tm_map(docs, removePunctuation)
  # Eliminate extra white spaces
  docs <- tm_map(docs, stripWhitespace)
  # Text stemming
  # docs <- tm_map(docs, stemDocument)
  dtm <- TermDocumentMatrix(docs)
  m <- as.matrix(dtm)
  v <- sort(rowSums(m),decreasing=TRUE)
  d <- data.frame(word = names(v),freq=v)
  
  word_tb <- d%>%unnest_tokens(word, texts)
#}

#run_sa('neg_review.csv')
