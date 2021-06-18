# course_project

course project link : https://course-project-0404.herokuapp.com/

In this project you can use the CRUD operations for courses.

A user can regisster through his mail and use the application.

A user can login and logout. 

A user can also reset his password.

A user can get the mail id which is registered by using the username, phone, secret question and secret answer.

User can add the courses which all he wants to the wishlist.

# to register as a user,
/auth/register/     

# to login,
/auth/login/

# to logout,
/auth/logout/

# forgot password on entering your mail id if it exists you will get a token for registered mail,
/auth/password_reset/

# to reset your password put the token whhich you got in mail and new password,
/auth/password_reset/confirm/

# forgot mail
/auth/forgot_email/

# to get all the courses
/courses_details/courses/

# to add the courses to the whishlist
/courses_details/wishlist/

