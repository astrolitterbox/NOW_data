library(divDyn)
carn_col <- "red"
creo_col <- "orange"
meso_col <- "blue"
prob_col <- "dark grey"
artio_col <- "dark green"
peris_col <- "brown"
colours <- c(carn_col, creo_col, meso_col, prob_col, artio_col, peris_col)


#data(stages)
occ <- read.table("occ_strat.csv", sep=",", header=TRUE)
data(stages)
bin_ddRec <-divDyn(occ, bin="stg", tax="genus")

now_strat <- read.table("NOW_strat.csv", sep=",", header=TRUE)
ddRec <-divDyn(occ, bin="NOW_stg", tax="genus")

#diversity by order
sampling_taxon <- "genus"
sampling_bin <- "NOW_stg"


carn_div <-divDyn(occ[occ$order == 'Carnivora',], bin=sampling_bin, tax=sampling_taxon)
creo_div <-divDyn(occ[occ$order == 'Creodonta',], bin=sampling_bin, tax=sampling_taxon)
meso_div <-divDyn(occ[occ$order == 'Mesonychia',], bin=sampling_bin, tax=sampling_taxon)
prob_div <-divDyn(occ[occ$order == 'Proboscidea',], bin=sampling_bin, tax=sampling_taxon)
artio_div <-divDyn(occ[occ$order == 'Artiodactyla',], bin=sampling_bin, tax=sampling_taxon)
peris_div <-divDyn(occ[occ$order == 'Perissodactyla',], bin=sampling_bin, tax=sampling_taxon)

#lines(now_strat$stage_mid, carn_div$divCSIB, col=carn_col, lwd=2)
#lines(now_strat$stage_mid, creo_div$divCSIB, col=creo_col, lwd=2)
#lines(now_strat$stage_mid, meso_div$divCSIB, col=meso_col, lwd=2)
#lines(now_strat$stage_mid, prob_div$divCSIB, col=prob_col, lwd=2)
#lines(now_strat$stage_mid, artio_div$divCSIB, col=artio_col, lwd=2)
#lines(now_strat$stage_mid, peris_div$divCSIB, col=peris_col, lwd=2)

#legend("topleft", legend=c("Carn.", "Creo.", "Meso.", "Prob.", "Artio.", "Perisso."),col=colours, lwd=2, bg="white")

#sqs with 0.6 quorum
subsampling_type <- "sqs"
subsampling_q <- 0.4
subsampling_taxon <- "genus"
subsampling_bin <- "NOW_stg"

sqs0.6 <-subsample(occ, coll="col", iter=50, q=subsampling_q, tax=subsampling_taxon, bin=subsampling_bin, type=subsampling_type, duplicates=FALSE)
#carn_sqs <-subsample(occ[occ$order == 'Carnivora',], coll="col", iter=50, q=subsampling_q, tax=subsampling_taxon, bin=subsampling_bin, type=subsampling_type, duplicates=FALSE)
#creo_sqs <-subsample(occ[occ$order == 'Creodonta',], coll="col", iter=50, q=subsampling_q, tax=subsampling_taxon, bin=subsampling_bin, type=subsampling_type, duplicates=FALSE)
#meso_sqs <-subsample(occ[occ$order == 'Mesonychia',], coll="col", iter=50, q=subsampling_q, tax=subsampling_taxon, bin=subsampling_bin, type=subsampling_type, duplicates=FALSE)
#prob_sqs <-subsample(occ[occ$order == 'Proboscidea',], coll="col", iter=50, q=subsampling_q, tax=subsampling_taxon, bin=subsampling_bin, type=subsampling_type, duplicates=FALSE)
#artio_sqs <-subsample(occ[occ$order == 'Artiodactyla',], coll="col", iter=50, q=subsampling_q, tax=subsampling_taxon, bin=subsampling_bin, type=subsampling_type, duplicates=FALSE)
#peris_sqs <-subsample(occ[occ$order == 'Perissodactyla',], coll="col", iter=50, q=subsampling_q, tax=subsampling_taxon, bin=subsampling_bin, type=subsampling_type, duplicates=FALSE)


tsplot(stages, shading="series", boxes="sys", xlim=82:95,
ylab<-"Genus-level diversity", ylim=c(0,400))

lines(now_strat$stage_mid, sqs0.6$divCSIB, col="black")
lines(now_strat$stage_mid, ddRec$divRT, col="green", lwd=2)
lines(now_strat$stage_mid, ddRec$divBC, col="blue", lwd=2)
lines(now_strat$stage_mid, ddRec$divSIB, col="orange", lwd=2)
lines(now_strat$stage_mid, ddRec$divCSIB, col="red", lwd=2)
legend("topleft", legend=c("SQS CSIB", "RT", "BC", "SIB", "CSIB"),col=c("black", "green", "blue", "orange", "red"), lwd=2, bg="white")


tsplot(stages, shading="series", boxes="sys", xlim=82:95,
ylab<-"Three-timer sampling completeness", ylim=c(0,1))
lines(now_strat$stage_mid, ddRec$samp3t, col="red", lwd=2)
#lines(stages$mid, bin_ddRec$divCSIB, col="red", lwd=2)

#lines(stages$mid, ddRec$divRT, col="red", lwd=2)
#lines(stages$mid[82:93], carn_sqs$divCSIB[82:93], col=carn_col, lwd=2)
#lines(stages$mid[82:93], creo_sqs$divCSIB[82:93], col=creo_col, lwd=2)
#lines(stages$mid[82:93], meso_sqs$divCSIB[82:93], col=meso_col, lwd=2)
#lines(stages$mid[82:93], prob_sqs$divCSIB[82:93], col=prob_col, lwd=2)
#lines(stages$mid[82:93], artio_sqs$divCSIB[82:93], col=artio_col, lwd=2)
#lines(stages$mid[82:93], peris_sqs$divCSIB[82:93], col=peris_col, lwd=2)
#legend("topleft", legend=c("Carn.", "Creo.", "Meso.", "Prob.", "Artio.", "Perisso."),col=colours, lwd=2, bg="white")

out <- data.frame(sqs0.6$divCSIB,now_strat$stage_mid)
colnames(out) <- c("div","mid_ma")
write.csv(out,"SQS_3Myr.csv", row.names = FALSE)

#Predators vs. herbivores


pred = occ[occ$order == 'Carnivora' | occ$order == 'Creodonta',]
#nrow(pred)
herb = occ[occ$order == 'Proboscidea'| occ$order == 'Artiodactyla' | occ$order == 'Perissodactyla',]
#nrow(herb)
#diversity by order
sampling_taxon = "genus"
sampling_bin = "NOW_stg"

pred_div <-divDyn(pred, bin=sampling_bin, tax=sampling_taxon)
bin_pred_div <-divDyn(pred, bin="stg", tax=sampling_taxon)
herb_div <-divDyn(herb, bin=sampling_bin, tax=sampling_taxon)
tsplot(stages, shading="series", boxes="sys", xlim=82:95,
ylab="Corrected genus diversity", ylim=c(0,220))
lines(now_strat$stage_mid, pred_div$divCSIB, col="red")
lines(now_strat$stage_mid, pred_div$divSIB, col="orange")
lines(now_strat$stage_mid, herb_div$divCSIB, col="green", lwd=2)

#lines(stages$mid[82:95], bin_pred_div$divCSIB, col="orange", lwd=2)
#lines(stages$mid, bin_pred_div$divCSIB, col="red", lwd=2)
legend("topleft", legend=c("Predators", "Herbivores"), col=c("red", "green"), lwd=2, bg="white")

out = data.frame(now_strat$stage_mid, pred_div$divSIB, herb_div$divCSIB)
colnames(out) <- c("mid_ma", "pred_div", "herb_div")
write.csv(out,"Pred_3Myr.csv", row.names = FALSE)
