my_data_frame <- read.csv(file="prob_values.csv", header=TRUE, sep=",");

all_speakers <- split(my_data_frame,rep(1:17,each=20))

speaker_count = 1

newdf <- as.data.frame(all_speakers[speaker_count])

colnames(newdf) <- c("spkr", "word", "freqs")

counts <- newdf$freqs

wordss<-paste(newdf$word,collapse = ',')
words_list<-list(strsplit(wordss, ",")[[1]])
unlisted <- unlist(words_list)

barplot(counts, main=newdf[1,1], 
        xlab="Words",
        names.arg=as.factor(unlisted))

Sys.sleep(10)
speaker_count = 2

newdf <- as.data.frame(all_speakers[speaker_count])

colnames(newdf) <- c("spkr", "word", "freqs")

counts <- newdf$freqs

wordss<-paste(newdf$word,collapse = ',')
words_list<-list(strsplit(wordss, ",")[[1]])
unlisted <- unlist(words_list)

barplot(counts, main=newdf[1,1], 
        xlab="Words",
        names.arg=as.factor(unlisted))

Sys.sleep(15)
speaker_count = 3

newdf <- as.data.frame(all_speakers[speaker_count])

colnames(newdf) <- c("spkr", "word", "freqs")

counts <- newdf$freqs

wordss<-paste(newdf$word,collapse = ',')
words_list<-list(strsplit(wordss, ",")[[1]])
unlisted <- unlist(words_list)

barplot(counts, main=newdf[1,1], 
        xlab="Words",
        names.arg=as.factor(unlisted))

Sys.sleep(15)
speaker_count = 4

newdf <- as.data.frame(all_speakers[speaker_count])

colnames(newdf) <- c("spkr", "word", "freqs")

counts <- newdf$freqs

wordss<-paste(newdf$word,collapse = ',')
words_list<-list(strsplit(wordss, ",")[[1]])
unlisted <- unlist(words_list)

barplot(counts, main=newdf[1,1], 
        xlab="Words",
        names.arg=as.factor(unlisted))

Sys.sleep(15)
speaker_count = 5
newdf <- as.data.frame(all_speakers[speaker_count])

colnames(newdf) <- c("spkr", "word", "freqs")

counts <- newdf$freqs

wordss<-paste(newdf$word,collapse = ',')
words_list<-list(strsplit(wordss, ",")[[1]])
unlisted <- unlist(words_list)

barplot(counts, main=newdf[1,1], 
        xlab="Words",
        names.arg=as.factor(unlisted))

Sys.sleep(15)
speaker_count = 6

newdf <- as.data.frame(all_speakers[speaker_count])

colnames(newdf) <- c("spkr", "word", "freqs")

counts <- newdf$freqs

wordss<-paste(newdf$word,collapse = ',')
words_list<-list(strsplit(wordss, ",")[[1]])
unlisted <- unlist(words_list)

barplot(counts, main=newdf[1,1], 
        xlab="Words",
        names.arg=as.factor(unlisted))

Sys.sleep(15)
speaker_count = 7

newdf <- as.data.frame(all_speakers[speaker_count])

colnames(newdf) <- c("spkr", "word", "freqs")

counts <- newdf$freqs

wordss<-paste(newdf$word,collapse = ',')
words_list<-list(strsplit(wordss, ",")[[1]])
unlisted <- unlist(words_list)

barplot(counts, main=newdf[1,1], 
        xlab="Words",
        names.arg=as.factor(unlisted))

Sys.sleep(15)
speaker_count = 8

newdf <- as.data.frame(all_speakers[speaker_count])

colnames(newdf) <- c("spkr", "word", "freqs")

counts <- newdf$freqs

wordss<-paste(newdf$word,collapse = ',')
words_list<-list(strsplit(wordss, ",")[[1]])
unlisted <- unlist(words_list)

barplot(counts, main=newdf[1,1], 
        xlab="Words",
        names.arg=as.factor(unlisted))

Sys.sleep(15)
speaker_count = 9

newdf <- as.data.frame(all_speakers[speaker_count])

colnames(newdf) <- c("spkr", "word", "freqs")

counts <- newdf$freqs

wordss<-paste(newdf$word,collapse = ',')
words_list<-list(strsplit(wordss, ",")[[1]])
unlisted <- unlist(words_list)

barplot(counts, main=newdf[1,1], 
        xlab="Words",
        names.arg=as.factor(unlisted))

Sys.sleep(15)
speaker_count = 10

newdf <- as.data.frame(all_speakers[speaker_count])

colnames(newdf) <- c("spkr", "word", "freqs")

counts <- newdf$freqs

wordss<-paste(newdf$word,collapse = ',')
words_list<-list(strsplit(wordss, ",")[[1]])
unlisted <- unlist(words_list)

barplot(counts, main=newdf[1,1], 
        xlab="Words",
        names.arg=as.factor(unlisted))

Sys.sleep(15)
speaker_count = 11

newdf <- as.data.frame(all_speakers[speaker_count])

colnames(newdf) <- c("spkr", "word", "freqs")

counts <- newdf$freqs

wordss<-paste(newdf$word,collapse = ',')
words_list<-list(strsplit(wordss, ",")[[1]])
unlisted <- unlist(words_list)

barplot(counts, main=newdf[1,1], 
        xlab="Words",
        names.arg=as.factor(unlisted))

Sys.sleep(15)
speaker_count = 12

newdf <- as.data.frame(all_speakers[speaker_count])

colnames(newdf) <- c("spkr", "word", "freqs")

counts <- newdf$freqs

wordss<-paste(newdf$word,collapse = ',')
words_list<-list(strsplit(wordss, ",")[[1]])
unlisted <- unlist(words_list)

barplot(counts, main=newdf[1,1], 
        xlab="Words",
        names.arg=as.factor(unlisted))

Sys.sleep(15)
speaker_count = 13

newdf <- as.data.frame(all_speakers[speaker_count])

colnames(newdf) <- c("spkr", "word", "freqs")

counts <- newdf$freqs

wordss<-paste(newdf$word,collapse = ',')
words_list<-list(strsplit(wordss, ",")[[1]])
unlisted <- unlist(words_list)

barplot(counts, main=newdf[1,1], 
        xlab="Words",
        names.arg=as.factor(unlisted))

Sys.sleep(15)
speaker_count = 14

newdf <- as.data.frame(all_speakers[speaker_count])

colnames(newdf) <- c("spkr", "word", "freqs")

counts <- newdf$freqs

wordss<-paste(newdf$word,collapse = ',')
words_list<-list(strsplit(wordss, ",")[[1]])
unlisted <- unlist(words_list)

barplot(counts, main=newdf[1,1], 
        xlab="Words",
        names.arg=as.factor(unlisted))

Sys.sleep(15)
speaker_count = 15

newdf <- as.data.frame(all_speakers[speaker_count])

colnames(newdf) <- c("spkr", "word", "freqs")

counts <- newdf$freqs

wordss<-paste(newdf$word,collapse = ',')
words_list<-list(strsplit(wordss, ",")[[1]])
unlisted <- unlist(words_list)

barplot(counts, main=newdf[1,1], 
        xlab="Words",
        names.arg=as.factor(unlisted))

Sys.sleep(15)
speaker_count = 16

newdf <- as.data.frame(all_speakers[speaker_count])

colnames(newdf) <- c("spkr", "word", "freqs")

counts <- newdf$freqs

wordss<-paste(newdf$word,collapse = ',')
words_list<-list(strsplit(wordss, ",")[[1]])
unlisted <- unlist(words_list)

barplot(counts, main=newdf[1,1], 
        xlab="Words",
        names.arg=as.factor(unlisted))

Sys.sleep(15)
speaker_count = 17

newdf <- as.data.frame(all_speakers[speaker_count])

colnames(newdf) <- c("spkr", "word", "freqs")

counts <- newdf$freqs

wordss<-paste(newdf$word,collapse = ',')
words_list<-list(strsplit(wordss, ",")[[1]])
unlisted <- unlist(words_list)

barplot(counts, main=newdf[1,1], 
        xlab="Words",
        names.arg=as.factor(unlisted))
