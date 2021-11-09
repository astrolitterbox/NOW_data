library(divDyn)

data(stages)


occ = read.table("occ_strat.csv", sep=",", header=TRUE)
occ$mid_ma<- round(apply(occ[,c("NOW_max_ma","NOW_min_ma")], 1, mean), 0) #1-Myr rounding

ddRec <-divDyn(occ, bin="stg", tax="genus", om="coll", coll="col")
out = data.frame(stages$mid[82:93],ddRec$ori2f3[82:93], ddRec$ext2f3[82:93])

colnames(out) <- c("age", "orig", "ext")
write.csv(out,"stage_res_2f3_genera_rates_stg.csv", row.names = FALSE)

ddRec_hr <-divDyn(occ, tax="genus", bin="mid_ma", revtime=TRUE, om="coll", coll="col")

#Rates
tsplot(stages, shading="series", boxes="sys", xlim=82:93,
ylab="Extinction and origination rates", ylim=c(0,2))
# lines
lines(stages$mid, ddRec$oriProp, col="green", lwd=2)
lines(stages$mid, ddRec$ori2f3, col="blue", lwd=2)
lines(stages$mid, ddRec$ext2f3, col="red", lwd=2)
lines(stages$mid, ddRec$extProp, col="black", lwd=2)


#lines(ddRec_hr$mid_ma, ddRec_hr$oriProp, col="green", lwd=1)
#lines(ddRec_hr$mid_ma, ddRec_hr$ori2f3, col="blue", lwd=1)
#lines(ddRec_hr$mid_ma, ddRec_hr$ext2f3, col="red", lwd=1)

#lines(stages$mid, ddRec$divSIB, col="green", lwd=2)
# legend
legend("topleft", legend=c("oriProp", "ori2f3", "ext2f3", "extProp"),
col=c("green", "blue", "red", "black"), lwd=2, bg="white")
#1 Myr resolution data is useless..
#out = data.frame(ddRec_hr$mid_ma,ddRec_hr$ori2f3, ddRec_hr$ext2f3)
#colnames(out) <- c("age", "orig", "ext")
#write.csv(out,"1_Myr_res_2f3_genera_rates.csv", row.names = FALSE)