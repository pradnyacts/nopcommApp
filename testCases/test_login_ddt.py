import time

import pytest
from selenium import webdriver
from utilities import XLUtils
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_002_DDT_Login:
    baseURL=ReadConfig.getApplicationURL()
    path=".//Testdata/LoginData.xlsx"

    logger=LogGen.logggen()


    @pytest.mark.regression
    def test_login_ddd(self,setup):
        self.logger.info("*******Test_002_DDT_Login *******")
        self.logger.info("*******verify Login test *******")

        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("no of rows:", self.rows)

        lst_status=[]  #empty list variable

        for r in range(2,self.rows +1):
            self.user = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword((self.password))
            self.lp.clickLogin()
            time.sleep(10)
            act_title= self.driver.title
            exp_titel="Dashboard / nopCommerce administration"

            if act_title== exp_titel:
                if self.exp=='Pass':
                    self.logger.info("*******Passed *******")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp=='Fail':
                    self.logger.info("*******Failed *******")
                    #self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title!= exp_titel:

                if self.exp=='Pass':
                    self.logger.info("*******Failed *******")
                    #self.lp.clickLogout()
                    lst_status.append("Fail")
                elif self.exp=='Fail':
                    self.logger.info("*******Passed *******")
                    #self.lp.clickLogout()
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Loginddt test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Loginddt test Failed")
            self.driver.close()
            assert False

        self.logger.info("********** End of Login DDT-Test completed******")
