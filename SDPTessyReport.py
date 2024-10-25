import openpyxl
import xmltodict
import xml.etree.ElementTree as ET
# importing the required module
import matplotlib.pyplot as plt


file_path = "C:\prj\WUP_ENG_BASE_SDP\SDP\src\SysTimer\Tessy\TESSY_OverviewReport_SDP_SysTimer.xml"

file_path2 = "C:\prj\WUP_ENG_BASE_SDP\SDP\src\XMSG\Tessy\TESSY_OverviewReport_SDP_XMSG.xml"

file_path3 = "C:\prj\WUP_ENG_BASE_SDP\SDP\src\FSCOMP\Tessy\TESSY_OverviewReport_SDP_FailSafeComparator.xml"

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

TotalFuntions = int(dict1['total']) + int(dict2['total']) + int(dict3['total'])
TotalNotExecutedFunctions = int(dict1['notexecuted']) + int(dict2['notexecuted']) + int(dict3['notexecuted'])
TotalFailedFunctions = int(dict1['notok']) + int(dict2['notok']) + int(dict3['notok'])
TotalPassedFunctions = int(dict1['ok']) + int(dict2['ok']) + int(dict3['ok'])

print("Total Tested SDP Functions = " ,TotalFuntions)
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
plt.title('SDP_Layer overall Test Report')
# showing the plot
plt.show()