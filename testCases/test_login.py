import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUserEmail()
    password=ReadConfig.getPassword()
    logger=LogGen.logggen()


    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("*******Test_001_Login*******")
        self.logger.info("*******Verify homepage title*******")
        self.driver =setup
        self.driver.get(self.baseURL)
        act_title= self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*******home page passed*******")

        else:
            self.driver.save_screenshot("./Screenshots/test_homePagetitle.png")
            self.driver.close()
            self.logger.error("*******home page failed*******")
            assert  False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("*******verify Login test *******")

        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title= self.driver.title

        if act_title== "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*******Login test pass *******")
            self.driver.close()
        else:
            self.driver.save_screenshot("//Users//pradnyadeshpande//PycharmProjects//nopcommApp//Screenshots" + "test_login.png")
            self.driver.close()
            self.logger.error("*******Login test failed*******")
            assert False

