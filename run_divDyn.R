library(divDyn)

data(stages)
occ = read.table("occ_strat.csv", sep=",", header=TRUE)
nrow(occ)
unique(occ$order)

now_strat = read.table("NOW_strat.csv", sep=",", header=TRUE)


carn_col <- "red"
creo_col <- "orange"
meso_col <- "blue"
prob_col <- "dark grey"
artio_col <- "dark green"
peris_col <- "brown"
colours <- c(carn_col, creo_col, meso_col, prob_col, artio_col, peris_col)

#NOW_stages <- data.frame(occ,stages$mid[82:93])
#colnames(NOW_stages) <- c("num","sys","stage", "bottom", "mid", "top")
#"num","sys","system","series","stage","short","bottom","mid","top","dur","stg","systemCol","seriesCol","col"
#"Name","order","genus","stage","stg","NOW_max_ma","NOW_mid_ma","NOW_min_ma","max_age","mid_age","min_ma","ID","col"

#hist(occ$Mass[occ$Mass  > 0]/1000)

reord <- c("Carnivora","Creodonta","Mesonychia", "Proboscidea", "Artiodactyla", "Perissodactyla")
#Fossil range
tsplot(stages, boxes=c("short","system"), shading="short", xlim=82:95, boxes.col=c("col","systemCol"), labels.args=list(cex=0.5))
fl <- fadlad(occ, bin=c("NOW_max_ma", "NOW_min_ma"), tax="Name")

ranges(occ, tax="Name",  bin=c("NOW_max_ma", "NOW_min_ma"), labs=F, labels.args=list(cex=0.2), filt="include", occs=T, group="order", ranges.args=list(lwd=0.1, col=colours), total.args=list(cex=0.5, col=colours), occs.args=list(cex=0.5, col=colours))
#counts

plotnames <- reord#c("Artiodactyla", "Carnivora", "Creodonta", "Mesonychia", "Perissodactyla", "Proboscidea")

#Sampling statistics

#samp <-sumstat(occ, tax="genus", bin="NOW_mid_ma",coll="col", ref="ID", duplicates=FALSE)
#samp
# Genus-level:
#bins  occs taxa colls refs gappiness
#1  549 20878 1353  3760 3764  1.709096
#Species-level:
#  bins  occs taxa colls refs gappiness
#1  549 23056 4115  3760 3764  1.566333


#proportions

tsplot(stages, shading="series", boxes="sys", xlim=82:93,
ylab="Counts", ylim=c(0,6000))
parts(occ$mid_age, occ$order, labs=F, col=colours, ord=reord)
legend("topleft", inset=c(0.01, 0.1),
legend= plotnames, fill=colours, bg="white")


tsplot(stages, shading="series", boxes="sys", xlim=82:93,
ylab="Proportion of occurrences", ylim=c(0,1))
parts(occ$mid_age, occ$order, prop=T,  labs=F, col=colours, ord=reord)
legend("top", inset=c(0.01, 0.1),
legend= plotnames, fill=colours, bg="white")

tsplot(stages, shading="series", boxes="sys", xlim=82:93,
ylab="Proportion of occurrences", ylim=c(0,600))
parts(occ$NOW_mid_ma, occ$order, prop=F,  labs=F, col=colours, ord=reord)
legend("top", inset=c(0.01, 0.1),
legend= plotnames, fill=colours, bg="white")



# metrics
ddRec <-divDyn(occ, bin="stg", tax="genus", om="coll", coll="col")
# basic plot
tsplot(stages, shading="series", boxes="sys", xlim=82:93,
ylab="Genus richness (diversity)", ylim=c(0,1200))
# lines
lines(stages$mid, ddRec$divSIB, col="red", lwd=2)
lines(stages$mid, ddRec$divCSIB, col="blue", lwd=2)

#lines(stages$mid, ddRec$divSIB, col="green", lwd=2)
# legend
legend("topleft", legend=c("SIB", "CSIB"),
col=c("red", "blue"), lwd=2, bg="white")

#sqs with 0.6 quorum
subsampling_type = "sqs"
subsampling_q = 0.6
subsampling_taxon = "genus"
subsampling_bin = "stg"

sqs0.6 <-subsample(occ, coll="col", iter=100, q=subsampling_q, tax=subsampling_taxon, bin=subsampling_bin, type=subsampling_type, duplicates=FALSE)
#richness with smaller bins
occ$mid_ma<- round(apply(occ[,c("NOW_max_ma","NOW_min_ma")], 1, mean), 0) #1-Myr bins
ddIDbin <- divDyn(occ, tax="genus", bin="mid_ma", revtime=TRUE, om="coll", coll="col")

tsplot(stages, shading="series", boxes="sys", xlim=82:93,
ylab="RT genera in 1 Myr bins", ylim=c(0,450))
lines(ddIDbin$mid_ma, ddIDbin$divRT, col="black", lwd=2)
lines(stages$mid, sqs0.6$divCSIB, col="blue", lwd=2)
lines(ddIDbin$mid_ma, 300+50*ddIDbin$samp3t, col="red", lwd=1)
abline(h=300)
abline(h=350)
#lines(ddIDbin$mid_ma, ddIDbin$divCSIB, col="blue", lwd=2)
#lines(ddIDbin$mid_ma, ddIDbin$divSIB, col="green", lwd=2)
#lines(stages$mid, ddRec$divRT, col="blue", lwd=2)
legend("topleft", legend=c("RT genera in 1 Myr bins", "SQS subsampled genera in stage bins"),col=c("black", "blue"), lwd=c(2), bg="white")


out = data.frame(stages$mid,sqs0.6$divCSIB	)
write.csv(out,"SQS.csv", row.names = TRUE)
#out = data.frame(ddIDbin$divRT,ddIDbin$mid_ma)
#write.csv(out,"1Myr_RT_all.csv", row.names = TRUE)

#Carnivores vs. predators




#diversity by order



carn_div <-divDyn(occ[occ$order == 'Carnivora',], bin="stg", tax="Name")
creo_div <-divDyn(occ[occ$order == 'Creodonta',], bin="stg", tax="Name")
meso_div <-divDyn(occ[occ$order == 'Mesonychia',], bin="stg", tax="Name")
prob_div <-divDyn(occ[occ$order == 'Proboscidea',], bin="stg", tax="Name")
artio_div <-divDyn(occ[occ$order == 'Artiodactyla',], bin="stg", tax="Name")
peris_div <-divDyn(occ[occ$order == 'Perissodactyla',], bin="stg", tax="Name")
tsplot(stages, shading="series", boxes="sys", xlim=82:94,
ylab="Range-through species richness", ylim=c(0,400))
lines(stages$mid[82:93], carn_div$divCSIB[82:93], col=carn_col, lwd=2)
lines(stages$mid[82:93], creo_div$divCSIB[82:93], col=creo_col, lwd=2)
lines(stages$mid[82:93], meso_div$divCSIB[82:93], col=meso_col, lwd=2)
lines(stages$mid[82:93], prob_div$divCSIB[82:93], col=prob_col, lwd=2)
lines(stages$mid[82:93], artio_div$divCSIB[82:93], col=artio_col, lwd=2)
lines(stages$mid[82:93], peris_div$divCSIB[82:93], col=peris_col, lwd=2)


legend("topleft", legend=c("Carn.", "Creo.", "Meso.", "Prob.", "Artio.", "Perisso."),col=colours, lwd=2, bg="white")



#By clade
carn_sqs <-subsample(occ[occ$order == 'Carnivora',], coll="col", iter=50, q=subsampling_q, tax=subsampling_taxon, bin=subsampling_bin, type=subsampling_type, duplicates=FALSE)
creo_sqs <-subsample(occ[occ$order == 'Creodonta',], coll="col", iter=50, q=subsampling_q, tax=subsampling_taxon, bin=subsampling_bin, type=subsampling_type, duplicates=FALSE)
meso_sqs <-subsample(occ[occ$order == 'Mesonychia',], coll="col", iter=50, q=subsampling_q, tax=subsampling_taxon, bin=subsampling_bin, type=subsampling_type, duplicates=FALSE)
prob_sqs <-subsample(occ[occ$order == 'Proboscidea',], coll="col", iter=50, q=subsampling_q, tax=subsampling_taxon, bin=subsampling_bin, type=subsampling_type, duplicates=FALSE)
artio_sqs <-subsample(occ[occ$order == 'Artiodactyla',], coll="col", iter=50, q=subsampling_q, tax=subsampling_taxon, bin=subsampling_bin, type=subsampling_type, duplicates=FALSE)
peris_sqs <-subsample(occ[occ$order == 'Perissodactyla',], coll="col", iter=50, q=subsampling_q, tax=subsampling_taxon, bin=subsampling_bin, type=subsampling_type, duplicates=FALSE)

tsplot(stages, shading="series", boxes="sys", xlim=82:95,
ylab="SQS subsampled genus diversity", ylim=c(0,100))
#lines(stages$mid, ddRec$divRT, col="red", lwd=2)
lines(stages$mid[82:93], carn_sqs$divCSIB[82:93], col=carn_col, lwd=2)
lines(stages$mid[82:93], creo_sqs$divCSIB[82:93], col=creo_col, lwd=2)
lines(stages$mid[82:93], meso_sqs$divCSIB[82:93], col=meso_col, lwd=2)
lines(stages$mid[82:93], prob_sqs$divCSIB[82:93], col=prob_col, lwd=2)
lines(stages$mid[82:93], artio_sqs$divCSIB[82:93], col=artio_col, lwd=2)
lines(stages$mid[82:93], peris_sqs$divCSIB[82:93], col=peris_col, lwd=2)
legend("topleft", legend=c("Carn.", "Creo.", "Meso.", "Prob.", "Artio.", "Perisso."),col=colours, lwd=2, bg="white")


#Species-level SQS
