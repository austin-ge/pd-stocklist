from selenium import webdriver
import os
import pandas as pd
import time

class Table:
  def __init__(self,driver):
    self.driver = driver
  
  def getColumnInfo(self):
    column_info = []
    columns = self.driver.find_elements_by_xpath("//div//tr//th")
    
    for column in columns:
      column_info.append(str(column.text))
    return column_info

  #results from first 25 on page
  
  def getResults(self, index=None):  

    columns = self.getColumnInfo()
    data = {}
    elements = self.driver.find_elements_by_xpath("//tr[@class = 'gridCell']{} ".format("[{}]".format(index) if index else ""))

    for element in elements:
      current_index = elements.index(element) + 1 if not index else index
      parsed_data = {}
      for column in columns:
        value = element.find_element_by_xpath("//tr[@class = 'gridCell'][{}]//td[{}]".format(current_index, columns.index(column) + 1)).text
        parsed_data.update({column: str(value)})
      data.update({current_index: parsed_data})

    return data

  #alternating 25 on page 

  def getResults2(self, index=None):

    columns = self.getColumnInfo()
    data = {}
    elements = self.driver.find_elements_by_xpath("//tr[@class = 'altGridCell']{} ".format("[{}]".format(index) if index else ""))

    for element in elements:
      current_index = elements.index(element) + 1 if not index else index
      parsed_data = {}
      for column in columns:
        value = element.find_element_by_xpath("//tr[@class = 'altGridCell'][{}]//td[{}]".format(current_index, columns.index(column) + 1)).text
        parsed_data.update({column: str(value)})
      data.update({current_index: parsed_data})
      

    return data

#To do make one funtion loop index from xpath

  def next_page2(self):
    button = self.driver.find_element_by_xpath("//tr[@class = 'pagerBar']//td[ 2]")
    button.click()
    
  
  def next_page3(self):
    button = self.driver.find_element_by_xpath("//tr[@class = 'pagerBar']//td[ 3]")
    button.click()
   

  def next_page4(self):
    button = self.driver.find_element_by_xpath("//tr[@class = 'pagerBar']//td[ 4]")
    button.click()
    

  


if '__main__' == __name__:
  Path = 'C:\Program Files (x86)\chromedriver.exe'
  driver = webdriver.Chrome(Path)
  driver.get('https://canopix3d.performancedesigns.com/StockCanopies.aspx')  
  table = Table(driver)
  
  
  
    #take in the dictonaries
  def panda(d1,d2,d3,d4,d5,d6,d7,d8):
    dict1 = d1
    dict2 = d2
    dict3 = d3
    dict4 = d4
    dict5 = d5
    dict6 = d6
    dict7 = d7
    dict8 = d8
    #convert to pandas dataframes
    df1 = pd.DataFrame(dict1)
    df2 = pd.DataFrame(dict2)
    df3 = pd.DataFrame(dict3)
    df4 = pd.DataFrame(dict4)
    df5 = pd.DataFrame(dict5)
    df6 = pd.DataFrame(dict6)
    df7 = pd.DataFrame(dict7)
    df8 = pd.DataFrame(dict8)
    #concat the data frames
    result = pd.concat([df1,df2,df3,df4,df5,df6,df6,df7,df8],ignore_index=True, sort=False, axis=1)
    #transpose the results
    t_results = result.transpose()
    t_results.drop([" ","Territories"], axis = 1, inplace = True) 
    
    return t_results
  
  dict1 = table.getResults()
  dict2 = table.getResults2()
  table.next_page2()
  
  time.sleep(1)
  
  dict3 = table.getResults()
  dict4 = table.getResults2()
  table.next_page3()

  time.sleep(1)

  dict5 = table.getResults()
  dict6 = table.getResults2()
  table.next_page4

  time.sleep(1)

  dict7 = table.getResults()
  dict8 = table.getResults2()


  df = panda(dict1,dict2,dict3,dict4,dict5,dict6,dict7,dict8)
  df.to_csv (r'C:\Users\austi\OneDrive\Desktop\web scraper v4\df.csv', index = False, header=True)

  
  
  print("Done!")