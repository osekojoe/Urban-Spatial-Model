#%%
#Run module imports
import numpy as np

#%%
#load arrays
study_area = np.load(r"D:\Codebase\Geoprocessing\inputfiles\Kampala_studyarea.npy")
relief = np.load(r"D:\Codebase\Geoprocessing\inputfiles\Kampala_relief.npy")
pop_2010 = np.load(r"D:\Codebase\Geoprocessing\inputfiles\Kampala_population_2010.npy")
main_roads = np.load(r"D:\Codebase\Geoprocessing\inputfiles\Kampala_mainroads.npy")
employment_large = np.load(r"D:\Codebase\Geoprocessing\inputfiles\Kampala_employment_large.npy")
employment_small = np.load(r"D:\Codebase\Geoprocessing\inputfiles\Kampala_employment_small.npy")

# %%
