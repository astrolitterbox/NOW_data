import numpy as np
import pandas as pd
from scipy.signal import savgol_filter
from matplotlib import pyplot as plt

cli = pd.read_csv("../westerhold.csv", sep=",", header=0, usecols=["age_tuned", "ISOBENd18oLOESSsmoothLongTerm"])
cli = cli.rename(columns={"age_tuned": "age"})
cli["age"]*=-1

CO2_data = pd.read_csv("/home/opit/Desktop/Palaeo/data/ferns/CO2_px", sep="\t")
CO2_age = -1*CO2_data["age"]
CO2_level = CO2_data["CO2"]
temp_data = pd.read_csv("/home/opit/Desktop/Palaeo/data/ferns/temperature_px", sep="\t")
temp_age = -1*temp_data["age"]
temperature = temp_data["temperature"]

magm_data = pd.read_csv("/home/opit/Desktop/Palaeo/data/ferns/magmatism_px", sep="\t")
magm_age = -1*magm_data["age"]
magmatism = magm_data["magmatism"]

cold_data = pd.read_csv("/home/opit/Desktop/Palaeo/data/ferns/cold_px", sep="\t")
cold_age = -1*cold_data["age"]
cold_biomes = cold_data["cold"]

arid_data = pd.read_csv("/home/opit/Desktop/Palaeo/data/ferns/arid_px", sep="\t")
arid_age = -1*arid_data["age"]
arid_biomes = arid_data["arid"]

cli["smoothed"] = savgol_filter(cli["ISOBENd18oLOESSsmoothLongTerm"], 5, 3) # window size 51, polynomial order 3
cli["smoothed"] = cli["smoothed"]/np.max(cli["smoothed"])

time=np.asarray([-0.330242336039629, -0.990727008118887,-1.6512116801981451,-2.3116963522774028,-2.9721810243566607,-3.632665696435919,-4.293150368515176,-4.953635040594435,-5.614119712673693,-6.2746043847529505,-6.935089056832209,-7.595573728911467,-8.256058400990726,-8.916543073069983,-9.577027745149241,-10.2375124172285,-10.897997089307758,-11.558481761387016,-12.218966433466273,-12.879451105545531,-13.53993577762479,-14.200420449704048,-14.860905121783306,-15.521389793862564,-16.18187446594182,-16.84235913802108,-17.502843810100337,-18.163328482179594,-18.823813154258854,-19.48429782633811,-20.14478249841737,-20.805267170496627,-21.465751842575884,-22.126236514655144,-22.7867211867344,-23.44720585881366,-24.107690530892917,-24.768175202972174,-25.428659875051434,-26.08914454713069,-26.74962921920995,-27.410113891289207,-28.070598563368463,-28.731083235447723,-29.39156790752698,-30.05205257960624,-30.712537251685497,-31.373021923764757,-32.03350659584401,-32.693991267923266,-33.35447594000252,-34.01496061208179,-34.67544528416104,-35.3359299562403,-35.996414628319556,-36.65689930039881,-37.317383972478076,-37.97786864455733,-38.63835331663659,-39.298837988715846,-39.9593226607951,-40.619807332874366,-41.28029200495362,-41.94077667703288,-42.601261349112136,-43.26174602119139,-43.922230693270656,-44.58271536534991,-45.24320003742917,-45.903684709508425,-46.56416938158768,-47.224654053666946,-47.8851387257462,-48.54562339782546,-49.206108069904715,-49.86659274198397,-50.527077414063235,-51.18756208614249,-51.84804675822175,-52.508531430301005,-53.16901610238026,-53.829500774459525,-54.48998544653878,-55.15047011861804,-55.810954790697295,-56.47143946277655,-57.131924134855815,-57.79240880693507,-58.45289347901433,-59.113378151093585,-59.77386282317284,-60.434347495252105,-61.09483216733136,-61.75531683941062,-62.415801511489875,-63.07628618356914,-63.73677085564839,-64.39725552772765,-65.05774019980691,-65.71822487188616])
rate=np.asarray([1.029123636112514, 1.029123636112514,1.029123636112514,0.3789265204296123,0.3789265204296123,0.11419400689800367,0.11419400689800367,0.5636389409228388,0.5636389409228388,0.32982053062615446,0.32949164297795364,0.32949164297795364,0.12539306507560585,0.12539306507560585,0.4341202140839964,0.4341202140839964,0.10126106420655115,0.2994158705488097,0.2994158705488097,0.2994158705488097,0.18611318434080906,0.18611318434080906,0.1862896700509312,0.18629825213965923,0.1865052055516262,0.18653201927022167,0.18653201927022167,0.1865403625628284,0.1865403625628284,0.18653201927022167,0.1862896700509312,0.18620183825527833,0.18620183825527833,0.18623268468404774,0.18628280512329032,0.18628280512329032,0.18628413642133945,0.18672075567439228,0.18673969263861986,0.18683204359629002,0.18683204359629002,0.18695525672346083,0.187137607431063,0.1873252999381213,0.1873252999381213,0.18732529993812136,0.18734115532064524,0.18734175794063382,0.18878052222008063,0.18882072695518332,0.18889443611702028,0.1907379653187818,0.1907379653187818,0.18734115532064524,0.18733895935873557,0.1873164148634899,0.1873164148634899,0.18711819223380904,0.18709268916451338,0.18709268916451338,0.18713051812489243,0.20009250193657394,0.3410214717252881,0.10760019470577022,0.10760019470577022,0.10916575996614822,0.10972066521229455,0.11033223187086774,0.19199025123215946,0.25169117433225563,0.270332814653959,0.270332814653959,0.2773280295889199,0.31326980911211844,0.31219305934249875,0.29421175068069194,0.2936551014080215,0.2952063737488167,0.2992885581698877,0.3000364906789144,0.3000364906789144,0.299983064847678,0.2992953646417233,0.2908790837823944,0.2908790837823944,0.29087624653600086,0.2908790837823944,0.2908790837823944,0.29117275363878276,0.29118196724799605,0.29118196724799605,0.29117275363878276,0.29118196724799605,0.2917258485137522,0.3005926872174767,0.3023198668456615,0.31228946364852106,1.0736057841491324,1.0715304237351,1.0658546530499882])
minHPD=np.asarray([0.9567819072044728, 0.9567819072044728,0.9567819072044728,0.3345469511957294,0.3345469511957294,0.07941250463004343,0.07941250463004343,0.4951097368249899,0.4951097368249899,0.29164802816731583,0.29164802816731583,0.29164802816731583,0.09013142577624939,0.09013142577624939,0.36138885722153535,0.36138885722153535,0.05553772772201938,0.25892898210578724,0.26089577174622175,0.26089577174622175,0.16925274794182987,0.16925274794182987,0.16949439982932474,0.16959125402186062,0.16959125402186062,0.16959125402186062,0.16959125402186062,0.16959125402186062,0.16959125402186062,0.16959125402186062,0.1692168169871146,0.1692249924448977,0.1687898911703862,0.1687898911703862,0.16860557782172353,0.16860557782172353,0.168623936427675,0.168623936427675,0.16860557782172353,0.16848347218677348,0.1678654948236707,0.16803468683454284,0.16740738844322936,0.1692249924448977,0.16860557782172353,0.16860557782172353,0.16925274794182987,0.16848347218677348,0.17063213191808052,0.17063213191808052,0.1719135172551022,0.17317344783834948,0.17308420398377333,0.13049224627008374,0.13141303260372517,0.13141303260372517,0.13124260504998764,0.13141303260372517,0.1331608935930446,0.1331608935930446,0.129769407956197,0.1692249924448977,0.17600127198189208,0.043585185009586476,0.04915865547197608,0.04922330953502922,0.04922330953502922,0.049484603573307966,0.07213073790657573,0.148067733038049,0.1418259100512344,0.1418259100512344,0.1418259100512344,0.2619899715107632,0.2620458551600042,0.12220189376921278,0.12994509015013836,0.14646145082704048,0.23948525372472795,0.23948525372472795,0.23948525372472795,0.23948525372472795,0.24088834310346954,0.13483781578869897,0.13483781578869897,0.13519228709701833,0.1403560989205137,0.1403560989205137,0.14006357231995056,0.14006357231995056,0.14020852060604486,0.14006357231995056,0.13483781578869897,0.1325692596161041,0.1460162503766977,0.16216456603867405,0.16216456603867405,0.54516409776491,0.5525904975340589,0.5525904975340589])
maxHPD=np.asarray([1.0982090233016815, 1.0982090233016815,1.0982090233016815,0.4278053542165692,0.4278053542165692,0.15594685402153113,0.15594685402153113,0.6367838655596935,0.6367838655596935,0.3706425022512089,0.37105922406772546,0.37105922406772546,0.16945804695321381,0.16945804695321381,0.5099403497357281,0.5099403497357281,0.1512222122278266,0.33596907927826036,0.3377584788988559,0.3376350611306454,0.19976210386523705,0.19976210386523705,0.19783226383525115,0.19782187867484802,0.19765277098826842,0.19765277098826842,0.19765277098826842,0.19765277098826842,0.19765277098826842,0.19765277098826842,0.1993246009490758,0.2005512626959449,0.2005512626959449,0.2005512626959449,0.20047313176799722,0.20047313176799722,0.2005512626959449,0.2005512626959449,0.20125070003508247,0.20125070003508247,0.2013956145819328,0.20321281698600752,0.20791696176101393,0.21171063632405102,0.21166765681952968,0.21171063632405102,0.212607897923699,0.21313130558577362,0.2986863664943364,0.2987788777668157,0.30159563209337586,0.43531041607428655,0.43531041607428655,0.21946976099637108,0.21993318102176757,0.21993318102176757,0.21969563924630875,0.21946976099637108,0.21993318102176757,0.2206100531271638,0.21946976099637108,0.5747926730339028,0.5612469802609558,0.19991751746244846,0.19991751746244846,0.19985202445290118,0.19985202445290118,0.2005512626959449,0.32644827388938646,0.33140370844828393,0.3267084986772165,0.3267084986772165,0.32935829102097336,0.6299431052560978,0.6299431052560978,0.37336156895459977,0.37036664373051265,0.36188084184065406,0.42483078391737544,0.41656333287262065,0.41656333287262065,0.4175407695055589,0.432211053182867,0.34334571289974664,0.34328907791497104,0.34334571289974664,0.34612399702866203,0.34612399702866203,0.34697296484089835,0.34731933806074805,0.34731933806074805,0.34795680372767307,0.3431811120440526,0.34612399702866203,0.8244246072345988,0.8871316980493358,1.1850285416604776,1.5840765066040723,1.5840765066040723,1.5840765066040723])
unc = (maxHPD - minHPD)/4

interp_bins = np.linspace(-66, 0,10)
print(np.all(np.diff(interp_bins) > 0))

#NOTE: flipping to preserve time direction, differentiating between age and time flow
interp_cli = np.interp(interp_bins, cli["age"], cli["smoothed"])
interp_temp = np.interp(interp_bins, temp_age, temperature)
interp = {'age':list(interp_bins), "smoothed":list(interp_cli), "temperature":list(interp_temp)}
interp = pd.DataFrame(interp) 

print(interp_bins)
print(interp_temp)

#interp.fillna(value=0)
plt.plot(interp["age"], interp["smoothed"], 'b-')
plt.plot(interp["age"], interp["temperature"], 'b.')
#plt.plot(interp["age"], interp["herb_div"], 'r-')
plt.savefig("PyRate/img/data_interp")
interp.to_csv("PyRate/data_interp.csv", index=False)