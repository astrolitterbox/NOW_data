pdf(file="predator_herbivore_diversity.pdf")

library(divDyn)

data(stages)
occ = read.table("occ_strat.csv", sep=",", header=TRUE)
occ$mid_ma<- round(apply(occ[,c("NOW_max_ma","NOW_min_ma")], 1, mean), 0) 
#Predators vs. herbivores

pred = occ[occ$order == 'Carnivora' | occ$order == 'Creodonta',]
#nrow(pred)
herb = occ[occ$order == 'Proboscidea'| occ$order == 'Artiodactyla' | occ$order == 'Perissodactyla',]
#nrow(herb)
#diversity by order
sampling_taxon = "genus"
sampling_bin = "stg"


#sqs with 0.6 quorum
subsampling_type = "sqs"
subsampling_q = 0.6
subsampling_taxon = "genus"
subsampling_bin = "stg"

pred_div <-divDyn(pred, bin=sampling_bin, tax=sampling_taxon, om="coll", coll="col")
herb_div <-divDyn(herb, bin=sampling_bin, tax=sampling_taxon, om="coll", coll="col")
sqs_pred <-subsample(pred, coll="col", iter=100, q=subsampling_q, tax=subsampling_taxon, bin=subsampling_bin, type=subsampling_type, duplicates=FALSE)
sqs_herb <-subsample(herb, coll="col", iter=100, q=subsampling_q, tax=subsampling_taxon, bin=subsampling_bin, type=subsampling_type, duplicates=FALSE)
tsplot(stages, shading="series", boxes="sys", xlim=82:93,
ylab="Corrected genus diversity", ylim=c(0,320))
lines(stages$mid[82:93], pred_div$divCSIB[82:93], col="red", lwd=2)
lines(stages$mid[82:93], pred_div$divSIB[82:93], col="orange")
lines(stages$mid[82:93], pred_div$divRT[82:93], col="brown", lwd=0.5)
lines(stages$mid[82:93], herb_div$divSIB[82:93], col="blue")
lines(stages$mid[82:93], herb_div$divCSIB[82:93], col="green", lwd=2)
lines(stages$mid[82:93], herb_div$divRT[82:93], col="darkblue", lwd=0.5)
lines(stages$mid[82:93], sqs_herb$divCSIB[82:93], col="darkgreen", lwd=3)
lines(stages$mid[82:93], sqs_pred$divCSIB[82:93], col="darkred", lwd=3)

#lines(stages$mid[82:95], bin_pred_div$divCSIB, col="orange", lwd=2)
#lines(stages$mid, bin_pred_div$divCSIB, col="red", lwd=2)
legend("topleft", legend=c("Predators", "Herbivores"), col=c("red", "green"), lwd=2, bg="white")

out = data.frame(stages$mid[82:93], herb_div$divCSIB[82:93], pred_div$divCSIB[82:93])
colnames(out) <- c("mid_ma", "pred_div", "herb_div")
write.csv(out,"Pred_herb_stage_level_CSIB_diversity.csv", row.names = FALSE)


#rates

out = data.frame(stages$mid[82:93],pred_div$ori2f3[82:93], pred_div$ext2f3[82:93], herb_div$ori2f3[82:93], herb_div$ext2f3[82:93])
colnames(out) <- c("age", "pred_orig", "pred_ext", "herb_orig", "herb_ext")
write.csv(out,"stage_res_2f3_genera_rates_pred_herb.csv", row.names = FALSE)

tsplot(stages, shading="series", boxes="sys", xlim=82:93,
ylab="Predator and herbivore 2f3 extinction/origination rates", ylim=c(0,2))
lines(stages$mid[82:93], herb_div$ori2f3[82:93], col="darkgreen", lwd=3)
lines(stages$mid[82:93], herb_div$ext2f3[82:93], col="darkblue", lwd=3)

lines(stages$mid[82:93], pred_div$ori2f3[82:93], col="darkred", lwd=3)
lines(stages$mid[82:93], pred_div$ext2f3[82:93], col="black", lwd=3)

#lines(stages$mid[82:95], bin_pred_div$divCSIB, col="orange", lwd=2)
#lines(stages$mid, bin_pred_div$divCSIB, col="red", lwd=2)
legend("topleft", legend=c("Herb. orig.", "Herb. ext.", "Pred.orig", "Pred. ext"), col=c("darkgreen", "darkblue", "darkred", "black"), lwd=2, bg="white")
dev.off()