pdf(file="predator_herbivore_diversity_3Myr.pdf")

library(divDyn)

data(stages)
now_strat <- read.table("NOW_strat.csv", sep=",", header=TRUE)
occ = read.table("occ_strat.csv", sep=",", header=TRUE)
occ$mid_ma<- round(apply(occ[,c("NOW_max_ma","NOW_min_ma")], 1, mean), 0) 
#Predators vs. herbivores

pred = occ[occ$order == 'Carnivora' | occ$order == 'Creodonta',]
#nrow(pred)
herb = occ[occ$order == 'Proboscidea'| occ$order == 'Artiodactyla' | occ$order == 'Perissodactyla',]
#nrow(herb)
#diversity by order
#sampling_taxon = "genus"
#sampling_bin = "stg"


#diversity by order

sampling_taxon <- "genus"
sampling_bin <- "NOW_stg"

herbDiv <-divDyn(herb, bin=sampling_bin, tax=sampling_taxon)
predDiv <-divDyn(pred, bin=sampling_bin, tax=sampling_taxon)

tsplot(stages, shading="series", boxes="sys", ylab="Genus-level diversity", ylim=c(0,500), xlim=c(82:95))

#lines(now_strat$stage_mid, sqs0.6$divCSIB, col="black")
lines(now_strat$stage_mid[0:21], herbDiv$divRT[0:21], col="green", lwd=2)
lines(now_strat$stage_mid[0:21], herbDiv$divSIB[0:21], col="darkgreen", lwd=2)
lines(now_strat$stage_mid[0:21], herbDiv$divCSIB[0:21], col="blue", lwd=2)
lines(now_strat$stage_mid[0:21], 400+100*herbDiv$samp3t[0:21], col="black", lwd=2)

lines(now_strat$stage_mid[0:21], predDiv$divRT[0:21], col="red", lwd=2)
lines(now_strat$stage_mid[0:21], predDiv$divSIB[0:21], col="yellow", lwd=2)

lines(now_strat$stage_mid[0:21], predDiv$divCSIB[0:21], col="orange", lwd=2)
lines(now_strat$stage_mid[0:21], 400+100*predDiv$samp3t[0:21], col="brown", lwd=2)
legend("center", legend=c("Herb. RT", "Herb. SIB", "Herb. CSIB", "Herb. completeness", "Pred. RT", "Pred. SIB", "Pred.CSIB", "Pred. completeness"),col=c("green", "darkgreen", "blue", "black", "red", "yellow", "orange", "brown"), lwd=2, bg="white")
abline(h=400)
abline(h=450, lwd=0.5, lty='dashed')
abline(h=500)

out <- data.frame(herbDiv$divCSIB[0:21], predDiv$divCSIB[0:21], now_strat$stage_mid[0:21], now_strat$stage_bottom[0:21], now_strat$stage_top[0:21], herbDiv$samp3t[0:21], predDiv$samp3t[0:21])
colnames(out) <- c("Herbivore CSIB genus-level diversity","Predator CSIB genus-level diversity", "mid_ma", "lower_ma", "top_ma", "Herbivore samp3t completeness", "Predator samp3t completeness")
write.csv(out,"div_3Myr.csv", row.names = FALSE)
#dev.off()

#sqs with 0.6 quorum
subsampling_type = "sqs"
subsampling_q = 0.6
subsampling_taxon = "genus"
subsampling_bin = "stg"

#pred_div <-divDyn(pred, bin=sampling_bin, tax=sampling_taxon, om="coll", coll="col")
#herb_div <-divDyn(herb, bin=sampling_bin, tax=sampling_taxon, om="coll", coll="col")

#sqs_pred <-subsample(pred, coll="col", iter=100, q=subsampling_q, tax=subsampling_taxon, bin=subsampling_bin, type=subsampling_type, duplicates=FALSE)
#sqs_herb <-subsample(herb, coll="col", iter=100, q=subsampling_q, tax=subsampling_taxon, bin=subsampling_bin, type=subsampling_type, duplicates=FALSE)
tsplot(stages, shading="series", boxes="sys", xlim=82:93,
ylab="Corrected genus diversity", ylim=c(0,320))
lines(stages$mid[82:93], predDiv$divCSIB[82:93], col="red", lwd=2)
lines(stages$mid[82:93], predDiv$divSIB[82:93], col="orange")
lines(stages$mid[82:93], predDiv$divRT[82:93], col="brown", lwd=0.5)
lines(stages$mid[82:93], herbDiv$divSIB[82:93], col="blue")
lines(stages$mid[82:93], herbDiv$divCSIB[82:93], col="green", lwd=2)
lines(stages$mid[82:93], herbDiv$divRT[82:93], col="darkblue", lwd=0.5)
#lines(stages$mid[82:93], sqs_herb$divCSIB[82:93], col="darkgreen", lwd=3)
#lines(stages$mid[82:93], sqs_pred$divCSIB[82:93], col="darkred", lwd=3)

#lines(stages$mid[82:95], bin_pred_div$divCSIB, col="orange", lwd=2)
#lines(stages$mid, bin_pred_div$divCSIB, col="red", lwd=2)
legend("topleft", legend=c("Predators", "Herbivores"), col=c("red", "green"), lwd=2, bg="white")

out = data.frame(stages$mid[82:93], herbDiv$divCSIB[82:93], predDiv$divCSIB[82:93])
colnames(out) <- c("mid_ma", "predDiv", "herbDiv")
write.csv(out,"Pred_herb_stage_level_CSIB_diversity_3Myr.csv", row.names = FALSE)


#rates

out = data.frame(stages$mid[82:93],predDiv$ori2f3[82:93], predDiv$ext2f3[82:93], herbDiv$ori2f3[82:93], herbDiv$ext2f3[82:93])
colnames(out) <- c("age", "pred_orig", "pred_ext", "herb_orig", "herb_ext")
write.csv(out,"stage_res_2f3_genera_rates_pred_herb.csv", row.names = FALSE)

tsplot(stages, shading="series", boxes="sys", xlim=82:93,
ylab="Predator and herbivore 2f3 extinction/origination rates", ylim=c(0,2))
lines(stages$mid[82:93], herbDiv$ori2f3[82:93], col="darkgreen", lwd=3)
lines(stages$mid[82:93], herbDiv$ext2f3[82:93], col="darkblue", lwd=3)

lines(stages$mid[82:93], predDiv$ori2f3[82:93], col="darkred", lwd=3)
lines(stages$mid[82:93], predDiv$ext2f3[82:93], col="black", lwd=3)

#lines(stages$mid[82:95], bin_pred_div$divCSIB, col="orange", lwd=2)
#lines(stages$mid, bin_pred_div$divCSIB, col="red", lwd=2)
legend("topleft", legend=c("Herb. orig.", "Herb. ext.", "Pred.orig", "Pred. ext"), col=c("darkgreen", "darkblue", "darkred", "black"), lwd=2, bg="white")
dev.off()