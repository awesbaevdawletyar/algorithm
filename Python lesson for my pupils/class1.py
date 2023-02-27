class CommentFromWebSite():
    def __init__(self,date,text,likes):
        self.date=date
        self.text=text
        self.likes=int(likes)
    def showComment(self):
        print(self.date,self.text,self.likes)
    def changeLikes(self):
        self.likes=self.likes+1
    def changeComment(self,new_text):
        self.text=new_text 
    
new_comment=CommentFromWebSite('08/02/1999','First','8')
new_comment2=CommentFromWebSite('10/03/1070','Second',10)
# new_comment2.showComment()
# new_comment.changeLikes()
# new_comment.showComment()
# print(type(new_comment))
# print(new_comment.date)
# print(new_comment.text)
# print(new_comment.likes)
# new_comment.changeComment("Second")
# new_comment.showComment()
