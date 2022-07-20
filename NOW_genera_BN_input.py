import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#plt.rcParams['figure.figsize'] = [15, 60]

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
taxa = pd.read_csv("Raw_NOW_data/now_export_locsp_2022-04-27.csv", delimiter="\t", na_values = ["\\N", "n", "N"], \
                   dtype={'MAX_AGE': 'float64', 'MIN_AGE': 'float64', 'LIDNUM': 'int'})

#taxa = pd.read_csv("Raw_NOW_data/now_export_2021-11-15.csv", delimiter=",", na_values = ["\\N", "n", "N"], \
#                   dtype={'MAX_AGE': 'float64', 'MIN_AGE': 'float64', 'LIDNUM': 'int'})
                   #dtype={'LAT': 'float64', 'LONG': 'float64'})
#,    usecols=["ORDER", "FAMILY", "GENUS", "SPECIES", "MAX_AGE", "MIN_AGE", "LIDNUM","NAME", "BODYMASS", "DIET_1", "DIET_2", "DIET_3"],                    comment='#', na_values="\\N")
#taxa
#print(taxa)
#print(taxa.isna().any())
taxa = taxa.fillna(-999)
#print(taxa.isna().any())
print(taxa.shape)

with open('Raw_NOW_data/NOW_species_log_2022_04.txt','w') as file:
    line = "Initial no. of occurences:"+str(taxa.shape[0])
    file.write(line)


NA_g = taxa['GENUS']==-999
NA_f = taxa['FAMILY']==-999
empty_f = taxa['FAMILY']=="\\N"
empty_g = taxa['GENUS']=="\\N"

indet_genus = taxa['GENUS']=="indet." 
Indet_genus = taxa['GENUS']=="Indet."
indet_fam = taxa['FAMILY']=="indet." 
empty_lat = taxa['LAT']==-999
empty_long = taxa['LONG']==-999
empty_hypsodonty = taxa['MEAN_HYPSODONTY']==-999
not_genus = taxa['GENUS']=="gen." 
not_genus_1 = taxa['GENUS']=="Gen." 
inc_sedis_g = taxa['GENUS']=="incertae sedis"
inc_sedis_f = taxa['FAMILY']=="incertae sedis"
inc_sedis_ff = taxa['FAMILY']=="incertaesedis"
piscivore = taxa['DIET_2']=="piscivore" #Remove piscivores
inc_sedis_o = taxa['ORDER']=="incertae sedis"
bad_min_age = taxa['MIN_AGE'] == -999
bad_min_age_n = taxa['MIN_AGE'] == "\\N"
bad_max_age = taxa['MAX_AGE'] == -999
nomen_nudum_f = taxa['FAMILY'] == "nomen nudum"
nomen_nudum_g = taxa['GENUS'] == "nomen nudum"
bad_age_max = taxa['MAX_AGE'] > 2
bad_age_min = taxa['MIN_AGE'] > 2
zero_ages = taxa['MAX_AGE']+taxa['MIN_AGE'] == 0
unc_age = (taxa['MAX_AGE'] - taxa['MIN_AGE'])/(taxa.MAX_AGE + taxa.MIN_AGE)/2. > 0.2


#not_ok = indet_sp| NA_sp | empty_s | not_sp|\
not_ok = NA_g|NA_f| indet_genus |Indet_genus| not_genus |not_genus_1|empty_lat|empty_long|empty_g| empty_f \
|indet_fam|inc_sedis_o| inc_sedis_f| inc_sedis_ff|inc_sedis_g | bad_max_age | bad_min_age|zero_ages|unc_age|\
bad_min_age_n| bad_age_max| bad_age_min|nomen_nudum_f | nomen_nudum_g| piscivore | empty_hypsodonty

taxa =taxa[~not_ok]
taxa.MIN_AGE = np.array(taxa.MIN_AGE).astype(float)


#Unify notation of unidentified species accepted_name
#species-level filters
'''
indet_sp = taxa['SPECIES']=="indet." 
NA_sp = taxa['SPECIES']==-999
empty_s = taxa['SPECIES']=="\\N"
not_sp = taxa['SPECIES']=="sp."

unident_sp = indet_sp | NA_sp | empty_s | not_sp
taxa.SPECIES[unident_sp] = "sp."

taxa = taxa[~unident_sp]
print("After initial cleanup:")
print(taxa.shape)

with open('Raw_NOW_data/NOW_species_log_2022_04.txt','a') as file:
    line = "\nAfter initial cleanup:"+str(taxa.shape[0])
    file.write(line)
'''
#Geography cleanup
bad_country_list = list(pd.read_csv("Raw_NOW_data/bad_countries.csv", delimiter=","))
print(bad_country_list)
print(len(taxa))
for i, country in enumerate(bad_country_list):
    filt = taxa["COUNTRY"]==country
    taxa = taxa[~filt]
print("After geography cleanup:")
print(taxa.shape)


    
#Order cleanup
print(np.unique(taxa["ORDER"]))
reject_orders = list(pd.read_csv("Raw_NOW_data/reject_orders_leave_Primates.csv", delimiter=","))
for i, taxon in enumerate(reject_orders):
    filt = taxa["ORDER"]==taxon
    taxa = taxa[~filt]
    print(len(taxa))

#Order cleanup after exploratory analysis, due to low number of entries
print(np.unique(taxa["ORDER"]))
reject_orders = list(pd.read_csv("Raw_NOW_data/reject_orders_low_number.csv", delimiter=","))
for i, taxon in enumerate(reject_orders):
    filt = taxa["ORDER"]==taxon
    taxa = taxa[~filt]
    print(len(taxa))    


#Mass scale:
#for i, family in enumerate(np.unique(taxa.FAMILY)): 
    #print("Family: ", family, "Mass ", np.mean(taxa[taxa.FAMILY == family].BODYMASS))
    
taxa.BODYMASS = taxa.BODYMASS/1000.


    
with open('Raw_NOW_data/NOW_genera_BN_log.txt','w') as file:
    line = "\nAfter order cleanup:"+str(taxa.shape[0])
    file.write(line)
    line = "\nRemaining orders: "+str(np.unique(taxa["ORDER"]))
    file.write(line)
    line = "\nNo. of remaining families: "+str(len(np.unique(taxa["FAMILY"])))
    file.write(line)

    reject_families = ['Tapiridae', 'Tapiroidea', 'Enaliarctidae', 'Amphicynodontidae', 'Odobenidae', 'Otariidae', 'Phocidae']

for i, taxon in enumerate(reject_families):
    filt = taxa["FAMILY"]==taxon
    taxa = taxa[~filt]
    print("Family rejection:", taxon, len(taxa))

    
with open('Raw_NOW_data/NOW_genera_BN_log','a') as file:
    line = "\nAfter selected family cleanup:"+str(taxa.shape[0])
    file.write(line)
    line = "\nNo. of remaining families: "+str(len(np.unique(taxa["FAMILY"])))
    file.write(line)
 
#name = pd.read_csv("Raw_NOW_data/species_names.csv", delimiter=",")
#accepted_name = taxa.GENUS+" "+taxa.SPECIES
#accepted_name[unident_sp] = taxa.GENUS
#accepted_name.to_csv("Raw_NOW_data/species_names.csv", index=False, sep=',', header=True)


mean_age = (taxa.MAX_AGE + taxa.MIN_AGE)/2.
taxa = taxa.merge(mean_age.to_frame(name="MEAN_AGE"), left_index=True, right_index=True)

out = taxa[['LIDNUM', 'MEAN_AGE', 'FAMILY', 'MEAN_HYPSODONTY']]

out.to_csv("Raw_NOW_data/NOW_genera_BN.csv", index=False, sep=',', header=True)     
#taxa.to_csv("Raw_NOW_data/species_level_coordinates.csv", index=False, sep=',', header=True, columns = ["LAT", "LONG"])

localities = np.unique(out.LIDNUM)
families = np.unique(out.FAMILY)
fam_header = ""
for f in families:
    fam_header = fam_header+", "+f
with open('Raw_NOW_data/BN_genera_input.csv', 'w') as file:
    line = "MEAN_AGE, MEAN_HYPSODONTY"+fam_header+"\n"
    file.write(line)


for loc in localities:
    line = ""
    #print("Locality: ", loc)
    if np.where(out["LIDNUM"] == loc)[0].shape[0] > 1:
        current_loc = out["LIDNUM"] == loc
        loc_families = out.loc[current_loc].FAMILY.tolist()
        loc_age = out.loc[current_loc].MEAN_AGE
        
        loc_hypsodonty = out.loc[current_loc].MEAN_HYPSODONTY

        age = str(np.unique(loc_age)[0])    
        hyp = str(np.unique(loc_hypsodonty)[0])
        fam_str = ""
        for i in families:
            if i in loc_families:
                fam_str = fam_str + ", "+str(1) 
            else:
                fam_str = fam_str + ", "+str(0)             
            
        line = age+", "+hyp+fam_str+"\n"
        with open('Raw_NOW_data/BN_genera_input.csv', 'a') as file:
            file.write(line)




