from playwright.sync_api import Page, expect

class NavigationPage:
    def __init__(self, page: Page):
        self.page = page
        self.searchInput = page.get_by_role("textbox", name="Search")
        
        # self.adminNav = page.get_by_role("link", name="Admin")
        # self.pimNav = page.get_by_role("link", name="PIM")
        # self.leaveNav = page.get_by_role("link", name="Leave")
        # self.timeNav = page.get_by_role("link", name="Time")
        # self.recruitmentNav = page.get_by_role("link", name="Recruitment")
        # self.my_infoNav = page.get_by_role("link", name="My Info")
        # self.performanceNav = page.get_by_role("link", name="Performance")
        # self.dashboardNav = page.get_by_role("link", name="Dashboard")
        # self.directoryNav = page.get_by_role("link", name="Directory")
        # self.maintenanceNav = page.get_by_role("link", name="Maintenance")
        # self.claimNav = page.get_by_role("link", name="Claim")
        # self.buzzNav = page.get_by_role("link", name="Buzz")
        
    def navigate_and_verify(self, menu_name: str, expected_url: str):
        link = self.page.get_by_role("link", name = menu_name)
        link.click()
        
        expect(self.page).to_have_url(expected_url)
        
        active_link = self.page.locator(f'a.oxd-main-menu-item.active:has-text("{menu_name}")')
        
        expect(active_link).to_be_visible()
        
        
    def search_menu(self, search: str):
        self.searchInput.fill(search)
        self.page.keyboard.press("Enter")
        
    # def navigate_to_admin(self):
    #     self.adminNav.click()
    #     self.page.wait_for_url("**/admin/viewSystemUsers")
        
    # def navigate_to_pim(self):
    #     self.pimNav.click()
    #     self.page.wait_for_url("**/pim/viewEmployeeList")
        
    # def navigate_to_leave(self):
    #     self.leaveNav.click()
    #     self.page.wait_for_url("**/leave/viewLeaveList")
            
    # def navigate_to_time(self):
    #     self.timeNav.click()
    #     self.page.wait_for_url("**/time/viewEmployeeTimesheet")
                
    # def navigate_to_recruitment(self):
    #     self.recruitmentNav.click()
    #     self.page.wait_for_url("**/recruitment/viewCandidates")
            
    # def navigate_to_my_info(self):
    #     self.my_infoNav.click()
    #     self.page.wait_for_url("**/pim/viewPersonalDetails/**")
                
    # def navigate_to_performance(self):
    #     self.performanceNav.click()
    #     self.page.wait_for_url("**/performance/searchEvaluatePerformanceReview")
        
    # def navigate_to_dashboard(self):
    #     self.dashboardNav.click()
    #     self.page.wait_for_url("**/dashboard/index")
                
    # def navigate_to_directory(self):
    #     self.directoryNav.click()
    #     self.page.wait_for_url("**/directory/viewDirectory")
            
    # def navigate_to_maintenance(self):
    #     self.maintenanceNav.click()
    #     self.page.wait_for_url("**/maintenance/purgeEmployee")
                
    # def navigate_to_claim(self):
    #     self.claimNav.click()
    #     self.page.wait_for_url("**/claim/viewAssignClaim")
                
    # def navigate_to_buzz(self):
    #     self.buzzNav.click()
    #     self.page.wait_for_url("**/buzz/viewBuzz")