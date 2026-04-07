#Project
#MiNi Social_Network


from datetime import datetime

class MiniSocialNetwork():
    def __init__(self):
        self.users = {}  # username -> {password, posts, following}
        self.current_user = None

    def register(self, username, password):
        if username in self.users:
            print("Username already exists.")
        else:
            self.users[username] = {
                "password": password,
                "posts": [],
                "following": set()
            }
            print(f"User '{username}' registered successfully.")

    def login(self, username, password):
        user = self.users.get(username)
        if user and user["password"] == password:
            self.current_user = username
            print(f"Welcome, {username}!")
        else:
            print("Invalid credentials.")

    def logout(self):
        print(f"User '{self.current_user}' logged out.")
        self.current_user = None

    def post_message(self, content):
        if not self.current_user:
            print("Please log in first.")
            return
        post = {
            "user": self.current_user,
            "content": content,
            "timestamp": datetime.now()
        }
        self.users[self.current_user]["posts"].append(post)
        print("Post created.")

    def follow(self, target_username):
        if not self.current_user:
            print("Please log in first.")
            return
        if target_username not in self.users:
            print("User not found.")
            return
        if target_username == self.current_user:
            print("You can't follow yourself.")
            return
        self.users[self.current_user]["following"].add(target_username)
        print(f"Now following '{target_username}'.")

    def unfollow(self, target_username):
        if not self.current_user:
            print("Please log in first.")
            return
        self.users[self.current_user]["following"].discard(target_username)
        print(f"Unfollowed '{target_username}'.")

    def view_feed(self):
        if not self.current_user:
            print("Please log in first.")
            return
        feed = list(self.users[self.current_user]["posts"])
        for user in self.users[self.current_user]["following"]:
            feed.extend(self.users[user]["posts"])
        feed.sort(key=lambda post: post["timestamp"], reverse=True)
        print("\n--- Your Feed ---")
        if not feed:
            print("No posts yet.")
        else:
            for post in feed:
                timestamp = post["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
                print(f" [{timestamp}]--@{post['user']}: {post['content']}")

    def menu(self):
        while True:
            print("\n=== Mini Social Network ===")
            if not self.current_user:
                print("1. Register\n2. Login\n3. Exit")
                choice = input("Choose an option: ")
                if choice == '1':
                    u = input("Username: ")
                    p = input("Password: ")
                    self.register(u, p)
                elif choice == '2':
                    u = input("Username: ")
                    p = input("Password: ")
                    self.login(u, p)
                elif choice == '3':
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice.")
            else:
                print(f"\nLogged in as @{self.current_user}")
                print("1. Post Message\n2. Follow\n3. Unfollow\n4. View Feed\n5. Logout")
                choice = input("Choose an option: ")
                if choice == '1':
                    content = input("Enter message: ")
                    self.post_message(content)
                elif choice == '2':
                    target = input("Enter username to follow: ")
                    self.follow(target)
                elif choice == '3':
                    target = input("Enter username to unfollow: ")
                    self.unfollow(target)
                elif choice == '4':
                    self.view_feed()
                elif choice == '5':
                    self.logout()
                else:
                    print("Invalid choice.")


app = MiniSocialNetwork()
app.menu()


    
