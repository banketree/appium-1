from PageObject import Pages


class TechCollectPage:
    '''
    技术专区详情页的收藏
    isOperate: 操作失败，检查点就失败,kwargs: WebDriver driver, String path(yaml配置参数)
    '''

    def __init__(self, **kwargs):
        self.driver = kwargs["driver"]
        self.path = kwargs["path"]
        self.page = Pages.PagesObjects(driver=self.driver, path=kwargs["path"])

        '''
        操作步骤
         logTest 日记记录器
        '''

    def operate(self, logTest):
        self.page.operate(logTest, 1)

    def checkPoint(self, caseName, logTest, devices):

        self.page.checkPoint(caseName=caseName, logTest=logTest, devices=devices)



if __name__ == "__main__":
    pass
