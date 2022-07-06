from blog.models import users, posts

# print(users)
# username="akhil"
# password="password"
# user=[user for user in users if user["username"]==username and user["password"]==password]
# if user:
#     print("success")
# else:
#     print("failed")


session={}
def signin_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("invalid user")
    return wrapper
def authentication(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")

    user = [user for user in users if user["username"] == username and user["password"] == password]
    return user
# print(authentication(username="akhil",password="password"))

class LoginView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authentication(username=username,password=password)
        if user:
            session["user"]=user[0]
        # print(session)
class PostListView:
    @signin_required
    def get(self,*args,**kwargs):
        return posts
    @signin_required
    def post(self,*args,**kwargs):
        # print(kwargs)
        userId=session["user"]["id"]
        post=kwargs.get("data")
        post["userId"]=userId
        print(post)
        posts.append(post)
        print("posted successfully")
        print(posts[-1])
class MyPostListView:
    @signin_required
    def get(self, *args, **kwargs):
        # print(session)
        userId=session["user"]["id"]
        my_posts=[post for post in posts if post["userId"]==userId]
        return my_posts

class AddLike:
    @signin_required
    def post(self,*args,**kwargs):
        postid=kwargs.get("postid")
        post=[post for post in posts if post["postId"]==postid]
        if post:
            post=post[0]
            userid=session["user"]["id"]
            post["liked_by"].append(userid)
            print(post["liked_by"])

login=LoginView()
login.post(username="akhil",password="Password@123")
all_post=PostListView()
myposts=MyPostListView()
# print(myposts.get())
my_post={
    "postId":"9","title":"hello good morning","content":"mycontent","liked_by":[]
}
all_post.post(data=my_post)

like=AddLike()
like.post(postid=1)
