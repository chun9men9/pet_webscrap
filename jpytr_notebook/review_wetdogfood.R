setwd("C:/Users/cmlim/Dropbox/NYC Data Science/Class/Web Scraping Project/jpytr_notebook")
library("tm")
library("SnowballC")
library("wordcloud")
library("RColorBrewer")

gen_wordcloud=function(filecsv, cloudname,excludelis=c('')){
  texts=read.csv(filecsv,header = FALSE)
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
  default_rmv=c("dog","dogs","food","foods",'can','canned')
  docs <- tm_map(docs, removeWords, c(default_rmv,excludelis) ) 
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
  head(d, 10)
  set.seed(1234)
  pdf(paste0(cloudname,'.pdf'))
  wordcloud(words = d$word, freq = d$freq, min.freq = 1, scale=c(2.5,0.2),use.r.layout=FALSE,
            max.words=100, random.order=FALSE, rot.per=0.35, 
            colors=brewer.pal(8, "Dark2"))
  dev.off()
}

#benefits_exclude=c('artificial')
neg_exclude=c('free','now','likes','one','very','great','love','loves','loved','like','always','absolutely','eatone')
pos_exclude=c('dry','old','one')
neg_title_exclude=c('love','much','quality','cans','products','product','eat',',much','great','good','like','likes','picky')
gen_wordcloud('benefits.csv','benefits')#,benefits_exclude)
gen_wordcloud('neg_review.csv','neg_reviews',neg_exclude)
gen_wordcloud('pos_review.csv','pos_reviews',pos_exclude)
gen_wordcloud('neg_title.csv','neg_titles',neg_title_exclude)
gen_wordcloud('pos_title.csv','pos_titles')
