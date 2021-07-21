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
#check if dimensions of all arrays match
study_area.shape

#Create array of arrays

#Method 1: using numpy append
# arr_List = []
# arr_List.append(study_area)
# arr_List.append(relief) 
# arr_List.append(pop_2010) 
# arr_List.append(main_roads) 
# arr_List.append(employment_large) 
# arr_List.append(employment_small) 

##Method2: using numpy vstack
# arr_tuple = (study_area, relief, pop_2010, main_roads, employment_large, employment_small)
# arr_array = np.vstack(arr_tuple)
# for arr in arr_array:
# 	print(arr)
# 	dim = arr.shape
# 	print(dim)

##method 3: using numpy.array
arr_stack = np.array([study_area, relief, pop_2010, main_roads, employment_large, employment_small])
for arr in arr_stack:
	print(arr)
	dim = arr.shape
	print(dim)

# %%
#sum population array to  find total population in Kampala, upto 2030
#loop yearly +3% natural pop growth, +2% immigration

#step1: calculate pop2010
pop2010 = np.sum(pop_2010)
print(pop2010)
#calculate pop for each year 2011 to 2030
growth_rate = 0.05 #2+3=5%
pop = pop2010 #1987506

pop_arr = []
def population(pop):
	'''Calculate population'''
	for year in range(2010,2030,1):
		pop = int(pop + (growth_rate * pop2010))
		print(pop)
		pop_arr.append(pop)
	pop_arr.insert(0,int(pop2010)) #insert 2010 pop
	print(pop_arr)

if __name__== '__main__':
	print('main')
	
	population(pop)


# %%
#calculate employment potential map

#%%
#available space map
