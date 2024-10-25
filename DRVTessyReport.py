import openpyxl
import xmltodict
import xml.etree.ElementTree as ET
# importing the required module
import matplotlib.pyplot as plt


file_path = "C:\prj\WUP_ENG_BASE_SDP\DRV\src\HTRC11001T\Tessy\TESSY_OverviewReport_DRV_HRTCAPI.xml"

file_path2 = "C:\prj\WUP_ENG_BASE_SDP\DRV\src\HTRC11001T\Tessy\TESSY_OverviewReport_DRV_HTRCCMD.xml"

file_path3 = "C:\prj\WUP_ENG_BASE_SDP\DRV\src\HTRC11001T\Tessy\TESSY_OverviewReport_DRV_HTRCSPI.xml"

file_path4 = "C:\prj\WUP_ENG_BASE_SDP\DRV\src\RH4Z2501\Tessy\TESSY_OverviewReport_DRV_RH4Z2501.xml"

tree1 = ET.parse(file_path)

root1 = tree1.getroot()

dict1 = root1[0].attrib

#print(dict1)


tree2 = ET.parse(file_path2)

root2 = tree2.getroot()

dict2 = root2[0].attrib
#print(dict2)

tree3 = ET.parse(file_path3)

root3 = tree3.getroot()

dict3 = root3[0].attrib

#print(dict3)

tree4 = ET.parse(file_path4)

root4 = tree4.getroot()

dict4 = root4[0].attrib


TotalFuntions = int(dict1['total']) + int(dict2['total']) + int(dict3['total']) + int(dict4['total'])
TotalNotExecutedFunctions = int(dict1['notexecuted']) + int(dict2['notexecuted']) + int(dict3['notexecuted'])  + int(dict4['notexecuted'])
TotalFailedFunctions = int(dict1['notok']) + int(dict2['notok']) + int(dict3['notok']) + int(dict4['notok'])
TotalPassedFunctions = int(dict1['ok']) + int(dict2['ok']) + int(dict3['ok']) + int(dict4['ok'])

print("Total Tested DRV Functions = " ,TotalFuntions)
print("Not Executed Functions = " ,TotalNotExecutedFunctions)
print("Failed Functions = " ,TotalFailedFunctions)
print("Passed Functions = " ,TotalPassedFunctions)
#print(dict1.values())

plt.rcParams["figure.figsize"] = [8.50, 4.50]
plt.rcParams["figure.autolayout"] = True

# x axis values
slices = [TotalNotExecutedFunctions,TotalFailedFunctions,TotalPassedFunctions]
# corresponding y axis values
activities = ["Not Executable Functions ","Failed Functions","Passed Functions"]

# color for each label
colors = ['r', 'y', 'g']

# plotting the pie chart

#patches, texts = plt.pie(slices, labels = activities, colors=colors, 
#         shadow = True,autopct='%2.1f%%')

patches = plt.pie(slices, labels = activities, colors=colors, 
         shadow = True,autopct='%1.1f%%')

# plotting legend
#plt.legend(patches,activities,loc="best")
plt.axis('equal')
plt.title('DRV_Layer overall Test Report')
# showing the plot
plt.show()