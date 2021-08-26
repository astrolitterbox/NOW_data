import numpy as np
import pandas as pd
from scipy.signal import savgol_filter
from matplotlib import pyplot as plt



cli = pd.read_csv("../westerhold.csv", sep=",", header=0, usecols=["age_tuned", "ISOBENd18oLOESSsmoothLongTerm"])
cli = cli.rename(columns={"age_tuned": "age"})

cli["ISOBENd18oLOESSsmoothLongTerm"] = cli["ISOBENd18oLOESSsmoothLongTerm"]/np.max(cli["ISOBENd18oLOESSsmoothLongTerm"])
cli["smoothed"] = savgol_filter(cli["ISOBENd18oLOESSsmoothLongTerm"], 15, 3) # window size 51, polynomial order 3

div = pd.read_csv("SQS_3Myr.csv", sep=",", header = 0, usecols = ["div","mid_ma"])
div = div.rename(columns={"mid_ma":"age"})
div["div"] = div["div"]/np.max(div["div"])
div["age"] = np.round(div["age"], 2)




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
merged = cli.merge(div, on='age')#TODO: merge with climate timeseries after interpolation

interp_bins = np.linspace(66,0,200)

#NOTE: flipping to preserve time direction, differentiating between age and time flow
interp_cli = np.flip(np.interp(interp_bins, merged["age"], merged["smoothed"]))
interp_div = np.flip(np.interp(interp_bins, merged["age"], merged["div"]))
interp = {'age':list(interp_bins), "cli":list(interp_cli), "div":list(interp_div)}
#interp = {'age':list(interp_bins), "cli":list(interp_cli), "div":list(interp_div)}

#interp["age"] = -1*interp["age"]
#interp["age"] = interp["age"] -66#+ np.min(merged["age"])

interp = pd.DataFrame(interp) 

interp.to_csv("cli_div_interp.csv", index=False)

plt.plot(interp["age"], interp["cli"], 'bo-')
plt.plot(interp["age"], interp["div"], 'go-')
plt.savefig("cli_div_interp")

#Predators vs. herbivores

div = pd.read_csv("Pred_3Myr.csv", sep=",", header = 0, usecols = ["mid_ma", "pred_div", "herb_div"])
div = div.rename(columns={"mid_ma":"age"})
div["herb_div"] = div["pred_div"]/np.max(div["herb_div"])
div["pred_div"] = div["pred_div"]/np.max(div["pred_div"])
div["age"] = np.round(div["age"], 2)
interp_bins = np.linspace(66,0,200)


merged = cli.merge(div, on='age')#TODO: merge with climate timeseries after interpolation

#NOTE: flipping to preserve time direction, differentiating between age and time flow
interp_cli = np.flip(np.interp(interp_bins, merged["age"], merged["smoothed"]))
interp_pred = np.flip(np.interp(interp_bins, merged["age"], merged["pred_div"]))
interp_herb = np.flip(np.interp(interp_bins, merged["age"], merged["herb_div"]))
interp = {'age':list(interp_bins), "cli":list(interp_cli), "pred_div":list(interp_pred), "herb_div":list(interp_herb)}
interp = pd.DataFrame(interp) 

interp.to_csv("Pred_interp.csv", index=False)

plt.plot(interp["age"], interp["cli"], 'bo-')
plt.plot(interp["age"], interp["herb_div"], 'go-')
plt.plot(interp["age"], interp["pred_div"], 'ro-')
plt.savefig("cli_pred_interp")
