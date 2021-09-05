import numpy as np
import pandas as pd
from scipy.signal import savgol_filter
from matplotlib import pyplot as plt



cli = pd.read_csv("../westerhold.csv", sep=",", header=0, usecols=["age_tuned", "ISOBENd18oLOESSsmoothLongTerm"])
cli = cli.rename(columns={"age_tuned": "age"})

cli["ISOBENd18oLOESSsmoothLongTerm"] = cli["ISOBENd18oLOESSsmoothLongTerm"]/np.max(cli["ISOBENd18oLOESSsmoothLongTerm"])
cli["smoothed"] = savgol_filter(cli["ISOBENd18oLOESSsmoothLongTerm"], 5, 3) # window size 51, polynomial order 3

#div = pd.read_csv("Pred_3Myr.csv", sep=",", header = 0, usecols = ["div","mid_ma"])
div = pd.read_csv("Pred_3Myr.csv", sep=",", header = 0, usecols = ["mid_ma", "pred_div", "herb_div"])
div = div.rename(columns={"mid_ma":"age"})

#div = pd.read_csv("1Myr_RT_all.csv", sep=",", header = 0, usecols = ["div","mid_ma"])
#div = div.rename(columns={"mid_ma":"age"})
#div["div"] = div["div"]/np.max(div["div"])

div["age"] = np.round(div["age"], 2)
cli["age"] = np.round(cli["age"], 2)


#Predator - herbivore data

div = pd.read_csv("Pred_3Myr.csv", sep=",", header = 0, usecols = ["mid_ma", "pred_div", "herb_div"])
div = div.rename(columns={"mid_ma":"age"})
div["herb_div"] = div["herb_div"]/np.max(div["herb_div"])
div["pred_div"] = div["pred_div"]/np.max(div["pred_div"])

merged = cli.merge(div, on='age')#TODO: merge with climate timeseries after interpolation
#merged.fillna(value=0)
interp_bins = np.linspace(np.max(merged["age"]),np.min(merged["age"]),600)
#NOTE: flipping to preserve time direction, differentiating between age and time flow
interp_cli = np.interp(interp_bins, merged["age"], merged["smoothed"])
interp_pred= np.interp(interp_bins, merged["age"], merged["pred_div"])
interp_herb= np.interp(interp_bins, merged["age"], merged["herb_div"])
interp = {'age':list(-1*interp_bins+np.max(interp_bins)), "smoothed":list(interp_cli), "pred_div":list(interp_pred), "herb_div":list(interp_herb)}

#interp["age"] =np.max(interp["age"])-interp["age"]
#print(interp["age"])


#interp = {'age':list(interp_bins), "cli":list(interp_cli), "div":list(interp_div)}

#interp["age"] = -1*interp["age"]
#interp["age"] = interp["age"] -66#+ np.min(merged["age"])

interp = pd.DataFrame(interp) 
#interp.fillna(value=0)
plt.plot(interp["age"], interp["smoothed"], 'b-')
plt.plot(interp["age"], interp["pred_div"], 'g-')
plt.plot(interp["age"], interp["herb_div"], 'r-')
plt.savefig("SQS_interp")
interp.to_csv("pred_interp.csv", index=False)
exit()

#astro = pd.DataFrame(np.genfromtxt("Lascar.csv", comments="#", delimiter=",", dtype='float'), columns=["age", "ecc", "precession", "obl", "ins" ])
#astro["age"] = astro["age"]/1000
#astro["ins"] = astro["ins"]/np.max(astro["ins"])

#div = pd.read_csv("/home/opit/Desktop/Palaeo/Methods/Upham/SQSresults_PBDB_quorum0p1_bins5Ma_withPiresFrom1.csv",  sep=",", dtype='float', usecols=["Time", "subsampled_richness", "raw_richness"])
#div = div.rename(columns={"Time": "age"})
#div["subsampled_richness"] = div["subsampled_richness"]/np.max(div["subsampled_richness"])
#div["raw_richness"] = div["raw_richness"]/np.max(div["raw_richness"])

#age_tuned,ISOBENbinned_d13Ccount,ISOBENbinned_d13C,ISOBENbinned_d13Cinterp,ISOBENbinned_d18Ocount,ISOBENbinned_d18O,ISOBENbinned_d18Ointerp,ISOBENd13cLOESSsmooth,ISOBENd18oLOESSsmooth,ISOBENLOESSsmooth_pts,ISOBENd13cLOESSsmoothLongTerm,ISOBENd18oLOESSsmoothLongTerm,ISOBENLOESSsmooth_pts


#astro = pd.DataFrame(np.genfromtxt("Lascar.csv", comments="#", delimiter=",", dtype='float'), columns=["age", "ecc", "precession", "obl", "ins" ])
#d18O = pd.DataFrame(np.genfromtxt("mudelsee2014highlat.txt", comments="#", max_rows=3000, delimiter="\t", dtype='float'), columns=["age", "d18Oforams", "min", "max"]) 

#astro['age']/=1000

#merged1 = div.merge(cli, on='age')
merged = cli.merge(div, on='age')
#merged.to_csv("cli_div_merged.csv", index=False)
interp_bins = np.linspace(np.max(merged["age"]),np.min(merged["age"]),600)
#NOTE: flipping to preserve time direction, differentiating between age and time flow
interp_cli = np.interp(interp_bins, merged["age"], merged["smoothed"])
interp_div = np.interp(interp_bins, merged["age"], merged["div"])
interp = {'age':list(-1*interp_bins), "cli":list(interp_cli), "div":list(interp_div)}
#interp = {'age':list(interp_bins), "cli":list(interp_cli), "div":list(interp_div)}


#interp["age"] *=-1*interp["age"]#=np.max(interp["age"])-interp["age"]

#interp["age"] = -1*interp["age"]
#interp["age"] = interp["age"] -66#+ np.min(merged["age"])
interp = pd.DataFrame(interp) 

#interp.to_csv("1Myr_RT_interp.csv", index=False)
plt.plot(interp["age"], interp["cli"], 'bo-')
plt.plot(interp["age"], interp["div"], 'go-')
#plt.savefig("1Myr_RT_interp")
interp.to_csv("SQS_interp.csv", index=False)
plt.savefig("SQS_interp")



