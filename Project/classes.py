class person(object):
    # Properties
    def __init__(self, bio: str, accountname, followers: int = 0, following: int = 0, 
                 posts: int = 0, list_of_post: list = [], follower_list: list = [], following_list: list = []): 
        
        self.followers = 0
        self.following = 0
        # Do linked list instaed 
        self.posts = 0
        self.bio = bio
        self.accountname = accountname
        self.list_of_post = []
        self.follower_list = []
        self.following_list = []

    # Posting
    def post(self, content, hashtags = []):
        # Create a new post object
        # If the list is empty, we set the key to 0
        
        if self.list_of_post == []:
          key = 0
        # The key of the previous post increment by 1
        else:
          key = self.list_of_post[-1].key + 1

        post2 = post(key, "", content, self.accountname, hashtags)

        self.list_of_post.append(post2)

        # Increment the number of posts by 1
        self.posts = self.posts + 1
        
        print(post2.content)
        for hashtag in post2.hashtag:
            print("#" + post2.hashtag)

    # Deleting the post
    # Note: post_index determines which post to delete in the list
    def delete(self, key):
        # Delete the post object
        for post in self.list_of_post:
          if post.key == key:
            self.list_of_post.remove(post)
        self.posts = len(self.list_of_post)

    # MOVE LIKE/ DISTAKE FUNCTION TO POST CLASS
    # Liking a post / Unliking a post
    def like(self, key, post_owner, post_liker):
        # Identify the right post
        target = post_owner.list_of_post[key]

        # Action
        if post_liker.accountname not in target.likes_by_user:
          # If the person hasn't liked the post, we add the user to the list
          target.likes_by_user.append(post_liker.accountname)
        else:
          target.likes_by_user.remove(post_liker.accountname) 

    # Disliking a post
    def dislike(self, key, post_owner, post_disliker):
        # Identify the right post
        target = post_owner.list_of_post[key]
        if post_disliker.accountname not in target.dislikes_by_user:
          # If the person hasn't disliked the post, we add the user to the list
          target.dislikes_by_user.append(post_disliker.accountname)
        else:
          target.dislikes_by_user.remove(post_disliker.accountname)
    
    # Follow an account & Unfollow an account
    # Note: Unlike function like() and dislike(), one cannot follow itself 

    def follow(self, account):
        # If the person has not yet followed the account
        if self.accountname not in account.follower_list:
          # Add the account into the following list
          self.following_list.append(account.accountname)
          # Increment the total following by 1
          self.following += 1
          
          # Add the follower into the list 
          account.follower_list.append(self.accountname)
          # Increment the total follower by 1
          account.followers += 1
        
        else: # Unfollow
          self.following_list.remove(account.accountname)
          self.following -= 1
          account.follower_list.remove(self.accountname)
          account.followers -= 1


class post():
    # Properties
    def __init__(self, key, comments, content, accountname, likes_by_user = [], dislikes_by_user = [], hashtag = []):
        self.key = key
        self.dislikes_by_user = []
        self.likes_by_user = []
        self.content = content
        self.comments = []
        self.hashtag = hashtag
        self.accountname = accountname

    def display_likes(self):
      return (len(self.likes_by_user))

    def display_dislikes(self):
      return (len(self.dislikes_by_user))



