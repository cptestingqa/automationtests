from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
import re
import os
import random
from operator import contains
from itertools import imap, repeat
import calendar
import csv
import win32clipboard
from pytz import timezone
import pytz
import time
import calendar
from datetime import datetime, time, date
from datetime import datetime
from datetime import date
import time
import datetime
import os
import socket
import xlrd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
from sys import exit 


class CommonLibrary:
    def __init__(self):
           pass

    def get_chrome_browser_options(self):
        dictionary= {'profile.default_content_settings.popups':'0'} 
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("test-type")
        #chrome_options.add_argument("-incognito")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options=chrome_options
        return chrome_options

    def click_element_using_javascript(self,locator,n=1):
        selenium = BuiltIn().get_library_instance('Selenium2Library')
        n = int(n)
        try:
          elements = selenium._element_find(locator, False, True)                    
          #selenium.execute_javascript("document.getElementById('submit').click();")
          cnt = len(elements)
          print "elements"
          print elements
          print "cnt:"+ str(cnt)
          selenium._current_browser().execute_script("arguments[0].click();", elements[n-1])
          print "Click Done"
          return True
        except Exception as exp:
          print "Got exception in read_multiple_testdata keyword.Error: "+str(exp)
          return False

    def get_ms_excel_file_sheet_names(self,filepath):
        """Return The list of excel file sheet names Using The Specified File filepath"""
        workbook = xlrd.open_workbook(filepath)
        return workbook.sheet_names()

    def get_ms_excel_file_rows_count(self,filepath,sheetName=None):
        """Return The Total No Rows In MS Excel File Using The Specified File filepath"""
        workbook = xlrd.open_workbook(filepath)
        snames=workbook.sheet_names()
        if sheetName==None:
            sheetName=snames[0]      
        if self.validate_the_sheet_in_ms_excel_file(filepath,sheetName)==False:
            return -1
        worksheet=workbook.sheet_by_name(sheetName)
        return worksheet.nrows

    
    def validate_the_sheet_in_ms_excel_file(self,filepath,sheetName):
        """Returns the True if the specified work sheets exist in the specifed MS Excel file else False"""
        workbook = xlrd.open_workbook(filepath)
        snames=workbook.sheet_names()
        sStatus=False        
        if sheetName==None:
            return True
        else:
            for sname in snames:
                if sname.lower()==sheetName.lower():
                    wsname=sname
                    sStatus=True
                    break
            if sStatus==False:
                print "Error: The specified sheet: "+str(sheetName)+" doesn't exist in the specified file: "+str(filepath)
        return sStatus
    
    def get_row_number_from_ms_excel_based_cell_value(self,filepath,celldata,sheetName=None):
        """Returns the row number of the given text in the MS Excel file """
        workbook = xlrd.open_workbook(filepath)
        snames=workbook.sheet_names()
        if sheetName==None:
            sheetName=snames[0]      
        if self.validate_the_sheet_in_ms_excel_file(filepath,sheetName)==False:
            return -1
        worksheet=workbook.sheet_by_name(sheetName)
        noofrows=worksheet.nrows
        for rowno in range(0,noofrows-1):
            row=worksheet.row(rowno)
            for colno in range(0,len(row)):
                cellval=worksheet.cell_value(rowno,colno)
                if celldata.lower()==cellval.lower():
                    return rowno+1
        return 0
        
    def get_ms_excel_row_values_into_list(self,filepath,rowNumber,sheetName=None):
        """Returns the list of values given row in the MS Excel file """
        workbook = xlrd.open_workbook(filepath)
        snames=workbook.sheet_names()
        tempList=[]
        if sheetName==None:
            sheetName=snames[0]      
        if self.validate_the_sheet_in_ms_excel_file(filepath,sheetName)==False:
            return tempList
        worksheet=workbook.sheet_by_name(sheetName)
        noofrows=worksheet.nrows
        tempList=[]
        for rowno in range(0,noofrows):
            row=worksheet.row(rowno)
            for colno in range(0,len(row)):
                cellval=worksheet.cell_value(rowno,colno)
                if int(rowNumber)==int(int(rowno)+1):
                    tempList.append(cellval)
        return tempList
        
    def get_ms_excel_column_values_into_list(self,filepath,colNumber,sheetName=None):
        """Returns the list of values given column in the MS Excel file """
        workbook = xlrd.open_workbook(filepath)
        snames=workbook.sheet_names()
        tempList=[]
        if sheetName==None:
            sheetName=snames[0]      
        if self.validate_the_sheet_in_ms_excel_file(filepath,sheetName)==False:
            return tempList
        worksheet=workbook.sheet_by_name(sheetName)
        noofrows=worksheet.nrows
        tempList=[]
        for rowno in range(0,noofrows-1):
            row=worksheet.row(rowno)
            for colno in range(0,len(row)):
                cellval=worksheet.cell_value(rowno,colno)
                if int(colNumber)==int(int(colno)+1):
                    tempList.append(cellval)
        return tempList
    
    def get_current_time(self):
        """Return the Current date value"""
        return time.strftime("%H-%M-%S")

    def get_ms_excel_cell_value(self,filepath,rowNumber,colNumber,sheetName=None):
        """Returns the cell value of given row and column in the MS Excel file """
        workbook = xlrd.open_workbook(filepath)
        snames=workbook.sheet_names()
        if sheetName==None:
            sheetName=snames[0]      
        if self.validate_the_sheet_in_ms_excel_file(filepath,sheetName)==False:
            return None
        worksheet=workbook.sheet_by_name(sheetName)
        cellval=worksheet.cell_value(int(int(rowNumber)-1),int(int(colNumber)-1))
        return cellval
    def get_unique_id(self):
        """Returns Unique Value by adding Time Stamp """
        return 'test'+str(time.localtime().tm_year)+str(time.localtime().tm_mon)+str(time.localtime().tm_mday)+str(time.localtime().tm_hour)+str(time.localtime().tm_min)+str(time.localtime().tm_sec)
    def get_time_stamp(self):
        """Returns the Current Date and Time """
        return datetime.datetime.now(timezone('EST')).strftime('%a %m/%d/%Y %I:%M %p')
                  
    def close_alert_message(self):
        """Returns 'True'if any alert message displayed returns 'False' if not"""
        selenium = BuiltIn().get_library_instance('Selenium2Library')
        try:
            selenium.get_alert_message()
            return True
        except:
            return False
    
    def verify_element_present(self,locator):
        """Returns 'True' if the element found with the 'locator' in the corresponding page else returns 'False'
        """
        selenium = BuiltIn().get_library_instance('Selenium2Library')
        return selenium._is_element_present(locator)

    def verify_element_visible(self,locator):
        """Returns 'True' if the element visible with the 'locator' in the corresponding page else returns 'False'
        """
        selenium = BuiltIn().get_library_instance('Selenium2Library')
        return selenium._is_visible(locator)
    def select_window_by_title(self,windowtitle):
        """Select a window by window title"""
        selenium = BuiltIn().get_library_instance('Selenium2Library')
        #browser = selenium._current_browser()
        windows=selenium.get_window_titles()
        for window in windows:
            if window==windowtitle:
                selenium.select_window(window)

    def string_should_contain(self,string,substring):
        """Returns True if The string contains substring else False' """
        ind=string.find(substring)
        if ind>=0:
            return True
        return False

    def get_random_number_in_given_range(self,start,stop):
        """ Returns the random from given range"""
        return random.randint(int(start),int(stop))
